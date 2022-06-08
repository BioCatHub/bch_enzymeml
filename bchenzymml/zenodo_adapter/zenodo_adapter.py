from flask import Flask, request, send_file
from flask_restx import Namespace, Resource, Api, fields, abort
from werkzeug.exceptions import BadRequest, HTTPException
import os


from bchenzymml.zenodo_adapter.zenodo_connector import ZenodoConnector

from bchenzymml.write_read_enzymeml.add_extract_bchmodel.omexbuilder import OmexBuilder
from assets.bch_test_model import model
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.enzymeml_json_builder import EnzymeMLJSONNuilder
from bchenzymml.pyenzyme_adapter.pyenzyme_adapter import PyenzmeAdapter

namespace = Namespace("api/zenodo", description="Route whicht handls the connection to Zenodo as well as the upload and download of EnzymeML documents")



name:str = None
@namespace.route("/getallexperiments")
class ZenodoExtractor(Resource):
    @namespace.doc()
    def get(self):
        experiments = ZenodoConnector("path").extract_deposits_for_dashboard_table()
        print(experiments)
        return experiments

'''
@namespace.route("/getexperiment")
class ZenodoSlicer(Resource):
    @namespace.doc()
    def get(self):
        id = request.args.get('id')
        print("tralalalala",id)
        print("Request rocks")
        print(id)
        return "hallo"
'''     
        
