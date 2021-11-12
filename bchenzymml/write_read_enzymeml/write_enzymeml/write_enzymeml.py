from flask import Flask, request, send_file
from flask_restx import Namespace, Resource, Api, fields

from bchenzymml.write_read_enzymeml.add_extract_bchmodel.omexbuilder import OmexBuilder
from assets.bch_test_model import model

namespace = Namespace("api/create_enzymeml", description="Route whicht creates Enzymeml documents and returns them in form of omex archives")

BCH_MODEL:dict = model

@namespace.route("")
class EnzymeMLwriter(Resource):
    @namespace.doc()
    def post(self):
        archive = OmexBuilder(BCH_MODEL)
        archive.create_omex_archive()
        return "success"