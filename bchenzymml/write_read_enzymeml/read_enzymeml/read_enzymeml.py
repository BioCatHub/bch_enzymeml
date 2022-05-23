from flask import Flask, request, send_file
from flask_restx import Namespace, Resource, Api, fields
from libcombine import *

import json
import os

from bchenzymml.write_read_enzymeml.add_extract_bchmodel.omexbuilder import OmexBuilder
from bchenzymml.write_read_enzymeml.add_extract_bchmodel.extract_from_enzymeml import ExtractFromEnzymeML

namespace = Namespace("api/read_enzymeml", description="Route whicht reads EnzymeML documents and returns the content to BioCatHub")


@namespace.route("")
class EnzymeMLReader(Resource):
    '''
        Accepts post request to read in EnzymeML documents. The documents are extracted via the request model and stored locally in assets/test.omex
        !!Note!!! 
        The file needs to be stored locally, because the libcombine library (needed to read and write EnzymeML documents) is not only accepts file paths and no bytestreams!
    '''
    @namespace.doc()
    def post(self):

        archive = request.files["enzymeML"]
        if os.path.exists("file.omex"):
            os.remove("file.omex")
        archive.save('assets/file.omex')
                
        archive_path = "assets/file.omex"
        
        bch_model = ExtractFromEnzymeML(archive_path).extract_bch_model()

        print("success", bch_model)
        return bch_model



