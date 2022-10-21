from flask import Flask, request, send_file
from flask_restx import Namespace, Resource, Api, fields, abort
from werkzeug.exceptions import BadRequest, HTTPException
import os

from bchenzymml.write_read_enzymeml.add_extract_bchmodel.omexbuilder import OmexBuilder
from assets.bch_test_model import model
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.enzymeml_json_builder import EnzymeMLJSONNuilder
from bchenzymml.pyenzyme_adapter.pyenzyme_adapter import PyenzmeAdapter
from assets.configurations import Configurations

namespace = Namespace("enzml/create_enzymeml", description="Route whicht creates Enzymeml documents and returns them in form of omex archives")

BCH_MODEL:dict = model
config = Configurations.get_configuarations()

name:str = None
@namespace.route("")
class EnzymeMLwriter(Resource):
    @namespace.doc()
    def post(self):
        
        try:
            payload = request.get_json()
            #print(type(payload), payload)
        except Exception as err:
            abort(400, 'My custom message', custom='value')
        try:
            if os.path.exists(config["enzymeml"]["path_incoming_pyenzyme"]):
                os.remove(config["enzymeml"]["path_incoming_pyenzyme"])
            if os.path.exists(config["enzymeml"]["path_updated_by_biocathub_model"]):
                os.remove(config["enzymeml"]["path_updated_by_biocathub_model"])
            
            enzml_json = EnzymeMLJSONNuilder(payload).build_enzymeml_json()
            PyenzmeAdapter(enzml_json).send_to_pyenzyme_create()
            OmexBuilder(payload).add_bch_model_to_omex_archive()
            file_path = config["enzymeml"]["path_updated_by_biocathub_model"]
            file_name = "experiment.omex"
            
        
            return send_file(file_path,
                                as_attachment=True,
                                mimetype="application/omex",
                                attachment_filename=file_name)

        except Exception as error:
            updates_path = config["enzymeml"]["path_updated_by_biocathub_model"]
            if os.path.exists(updates_path):
                os.remove(updates_path )
            print("Error in build process", error, "file:", __name__)
            OmexBuilder(payload).create_omex_archive()
            file_path = updates_path 
            file_name = "experiment.omex"
        
            return send_file(file_path,
                                as_attachment=True,
                                mimetype="text/xml",
                                attachment_filename=file_name)
            
        
    
        
        