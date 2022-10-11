from flask import Flask, request, send_file
from flask_restx import Namespace, Resource, Api, fields, abort
from werkzeug.exceptions import BadRequest, HTTPException
import os
import json


from bchenzymml.zenodo_adapter.zenodo_connector import ZenodoConnector

from bchenzymml.write_read_enzymeml.add_extract_bchmodel.omexbuilder import OmexBuilder
from assets.bch_test_model import model
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.enzymeml_json_builder import EnzymeMLJSONNuilder
from bchenzymml.pyenzyme_adapter.pyenzyme_adapter import PyenzmeAdapter
from bchenzymml.write_read_enzymeml.add_extract_bchmodel.extract_from_enzymeml import ExtractFromEnzymeML
import bchenzymml.zenodo_adapter.upload_enzymeml_to_zenodo as upload_adapter

from bchenzymml.zenodo_adapter.upload_enzymeml_to_zenodo import EnzymeMLUploader
from bchenzymml.zenodo_adapter.zenodo_metadata_parser import ZenodoMetadataParser
from assets.configurations import Configurations


namespace = Namespace("enzml/zenodo", description="Route whicht handles the connection to Zenodo as well as the upload and download of EnzymeML documents")
config = Configurations.get_configuarations()

#@namespace.route("/getallexperiments")
@namespace.route("")
class ZenodoExtractor(Resource):
    @namespace.doc()
    def get(self):
        print("hallo")
        experiments = ZenodoConnector("path").extract_deposits_for_dashboard_table(key = False)
        print(experiments)
        return experiments
    
    def post(self):
        print("post request to zenodo")
        key_json = request.get_json()
        print(key_json)
        key = key_json["access_token"]
        experiments = ZenodoConnector("path").extract_deposits_for_dashboard_table(key)
        print(experiments)
        return experiments



@namespace.route("/getexperiment")
class ZenodoSlicer(Resource):
    @namespace.doc()
    def get(self):
        id = request.args.get('id')
        print("******************************* experiment id is", id)
        enzml = ZenodoConnector("path").get_individual_entry(id)

        #print(enzml)
        try:
            if os.path.exists(config["enzymeml"]["path_updated_by_biocathub_model"]):
                os.remove(config["enzymeml"]["path_updated_by_biocathub_model"])
            with open(config["enzymeml"]["path_updated_by_biocathub_model"], "wb") as omex_archive:
                omex_archive.write(enzml)
            #new_enzml = ExtractFromEnzymeML("assets/assets/zenodo-enzml.omex").extract_bch_model()
            new_enzml = ExtractFromEnzymeML(config["enzymeml"]["path_updated_by_biocathub_model"]).extract_bch_model()
            print("Success")
            print(new_enzml)
            return new_enzml
        except Exception as err:
            print(err)
            print("Nononono")
            return "nonono"

    def post(self):
        data = request.get_json()
        id = data["id"]
        key = data["access_token"]
        print("******************************* experiment id is", id)
        enzml = ZenodoConnector("path").get_individual_entry(id, key)

        #print(enzml)
        try:
            if os.path.exists(config["enzymeml"]["path_updated_by_biocathub_model"]):
                os.remove(config["enzymeml"]["path_updated_by_biocathub_model"])
            with open(config["enzymeml"]["path_updated_by_biocathub_model"], "wb") as omex_archive:
                omex_archive.write(enzml)
            #new_enzml = ExtractFromEnzymeML("assets/assets/zenodo-enzml.omex").extract_bch_model()
            new_enzml = ExtractFromEnzymeML(config["enzymeml"]["path_updated_by_biocathub_model"]).extract_bch_model()
            #print("Success")
            return new_enzml
        except Exception as err:
            print(err)
            print("Nononono")
            return "nonono"

@namespace.route("/publishexperiment")
class ZenodoPublisher(Resource):
    @namespace.doc()
    def post(self):
        try:
            payload_bianry = request.get_data()
            
            payload_json = payload_bianry.decode()
            payload = json.loads(payload_json)
            print(payload["access_token"])
            if os.path.exists("assets/BioCatHub_enzml.omex"):
                os.remove("assets/BioCatHub_enzml.omex")
            enzml_json = EnzymeMLJSONNuilder(payload["experiment"]).build_enzymeml_json()
            print("enzml json",enzml_json)
            PyenzmeAdapter(enzml_json).send_to_pyenzyme_create()
            OmexBuilder(payload["experiment"]).add_bch_model_to_omex_archive()
        #except Exception as err:


        #try:
            metadata_zenodo = ZenodoMetadataParser(payload["experiment"]).parse_model()
            print("der acces token ist", payload["access_token"])

            EnzymeMLUploader(config["enzymeml"]["path_updated_by_biocathub_model"], metadata_zenodo).upload_enzyme_ml(payload["access_token"])

        except Exception as err:
            print(err)
            print("ZenodoUploadFailed")
            print("Error in publishing EnzymeML")
            abort(400, "not model", value="error")
            raise


        
