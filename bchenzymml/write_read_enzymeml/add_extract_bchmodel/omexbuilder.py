# System imports
from io import BytesIO
import json
import zipfile
import os

# Thrid pary imports
import libcombine

class OmexBuilder:
    ''''
        This class creates empty omex archieves, adds the biocathub model and stores the archieve locally in the ./assets folder

        attr:
            bch_model: dict
        
        methods:

        return:
            omex_archieve: binary --> omex archive as binary format
    '''

    def __init__(self,bch_model):
        self.bch_model = bch_model

    
    def save_bch_model_local(self):
        '''
            Creates a file named "Biocathub.json" based on the bch_model and stores it locally on the server

            args: 
                bch_model: dict

            return:
                None
        '''

        with open("assets/biocathub.json", "w") as bch_model_file:
            bch_model_json = json.dumps(self.bch_model)
            bch_model_file.write(bch_model_json)
    
    def create_omex_archive(self):
        '''
            adds the bch_model to omex archive and stores the archive in ./assets/BiocatHub.omex
            arg:
                None
            
            return:
                None
        '''
        archive = libcombine.CombineArchive()
        self.save_bch_model_local()
        archive.addFile("assets/biocathub.json", "biocathub.json", libcombine.KnownFormats.lookupFormat("json"))
        archive.writeToFile("assets/BioCatHub.omex")


    

