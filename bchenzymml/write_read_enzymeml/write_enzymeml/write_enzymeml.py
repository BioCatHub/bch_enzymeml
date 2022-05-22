from flask import Flask, request, send_file
from flask_restx import Namespace, Resource, Api, fields, abort
from werkzeug.exceptions import BadRequest, HTTPException

from bchenzymml.write_read_enzymeml.add_extract_bchmodel.omexbuilder import OmexBuilder
from assets.bch_test_model import model
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.enzymeml_json_builder import EnzymeMLJSONNuilder
from bchenzymml.pyenzyme_adapter.pyenzyme_adapter import PyenzmeAdapter

namespace = Namespace("api/create_enzymeml", description="Route whicht creates Enzymeml documents and returns them in form of omex archives")

BCH_MODEL:dict = model

name:str = None
@namespace.route("")
class EnzymeMLwriter(Resource):
    @namespace.doc()
    def post(self):
        
        try:
            payload = request.get_json()
            print(type(payload), payload)
        except Exception as err:
            return "no data in the post request"

        try:
            enzml_json = EnzymeMLJSONNuilder(payload).build_enzymeml_json()
            new_archive = PyenzmeAdapter(enzml_json).send_to_pyenzyme_create()
            archive = OmexBuilder(payload).add_bch_model_to_omex_archive()
            file_path = "assets/BioCatHub.omex"
            file_name = "experiment.omex"
        
            return send_file(file_path,
                                as_attachment=True,
                                mimetype="application/omex",
                                attachment_filename=file_name)
            
        except Exception as err:
            abort(400, 'My custom message', custom='value')
    
        
        