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

namespace = Namespace("api/zenodo", description="Route whicht handls the connection to Zenodo as well as the upload and download of EnzymeML documents")


@namespace.route("/getallexperiments")
class ZenodoExtractor(Resource):
    @namespace.doc()
    def get(self):
        print("hallo")
        experiments = ZenodoConnector("path").extract_deposits_for_dashboard_table()
        print(experiments)
        return experiments



@namespace.route("/getexperiment")
class ZenodoSlicer(Resource):
    @namespace.doc()
    def get(self):
        id = request.args.get('id')
        enzml = ZenodoConnector("path").get_individual_entry(id)
        #print(enzml)
        try:
            with open("assets/zenodo-enzml.omex", "wb") as omex_archive:
                omex_archive.write(enzml)
            new_enzml = ExtractFromEnzymeML("assets/assets/zenodo-enzml.omex").extract_bch_model()
            if os.path.exists("assets/zenodo-enzml.omex"):
                os.remove("assets/zenodo-enzml.omex")
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
        test_file="BioCatHub_omex_update.omex"

        data_test = {
        "metadata": {
        "title": "Yeah!!!",
        "upload_type": "dataset",
        "description": "EnzymeML document",
        "creators": [
            {"name": "Doe, John", "affiliation": "Zenodo"}
        ],
        "keywords":["enzymes", "biocatalysis"],
        "doi":""
        }
        }

        try:
            payload_bianry = request.get_data()
            payload_json = payload_bianry.decode()
            payload = json.loads(payload_json)
            if os.path.exists("assets/BioCatHub_enzml.omex"):
                os.remove("assets\BioCatHub_enzml.omex")
                enzml_json = EnzymeMLJSONNuilder(payload).build_enzymeml_json()
                PyenzmeAdapter(enzml_json).send_to_pyenzyme_create()
                OmexBuilder(payload).add_bch_model_to_omex_archive()
        except Exception as err:
            abort(400, "not model", value="error")

        try:
            metadata_zenodo = ZenodoMetadataParser(payload).parse_model()
            EnzymeMLUploader("assets\BioCatHub_enzml.omex", metadata_zenodo).upload_enzyme_ml()
        
        except Exception as err:
            print(err)
            print("ZenodoUploadFailed")
            raise

        data_test = {
        "metadata": {
        "title": "EnzymeML document new",
        "upload_type": "dataset",
        "description": "EnzymeML document",
        "creators": [
            {"name": "Doe, John", "affiliation": "Zenodo"}
        ],
        "keywords":["enzymes", "biocatalysis"],
        "doi":""
        }
        }

        return "chek"
    
        #upload_adapter.EnzymeMLUploader(test_file, data_test)

        
