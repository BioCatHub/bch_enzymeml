# System imports
from io import BytesIO
import json
import zipfile
import os
import shutil

# Thrid pary imports
import libcombine

# self imports

from assets.configurations import Configurations

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
        self.config = Configurations.get_configuarations()

    
    def save_bch_model_local(self):
        '''
            Creates a file named "Biocathub.json" based on the bch_model and stores it locally on the server

            args: 
                bch_model: dict

            return:
                None
        '''

        with open(self.config["enzymeml"]["biocathub_model_path_local"], "w") as bch_model_file:
            bch_model_json = json.dumps(self.bch_model)
            bch_model_file.write(bch_model_json)
            print("mooooooooooodelk",self.bch_model)
            print("paht", self.config["enzymeml"]["biocathub_model_path_local"])
    
    def create_omex_archive(self):
        '''
            adds the bch_model to omex archive and stores the archive in ./assets/BiocatHub.omex
            arg:
                None
            
            return:
                None
        '''
        try:

            if os.path.exists(self.config["enzymeml"]["biocathub_model_path_local"]):
                os.remove(self.config["enzymeml"]["biocathub_model_path_local"])  
            self.save_bch_model_local()
            newArchive = libcombine.CombineArchive()
            newArchive.addFile(self.config["enzymeml"]["biocathub_model_path_local"], self.config["enzymeml"]["biocathub_paht_in_omex_archive"], libcombine.KnownFormats.lookupFormat("json"))
            newArchive.writeToFile(self.config["enzymeml"]["path_updated_by_biocathub_model"])
        except Exception as err:
            print("error in reading enzymeml")
            print(err)
            raise

    def add_bch_model_to_omex_archive(self):
        if os.path.exists(self.config["enzymeml"]["biocathub_model_path_local"]):
            os.remove(self.config["enzymeml"]["biocathub_model_path_local"])
        self.save_bch_model_local()
        archive = libcombine.CombineArchive()
        path = "assets/enzymemlContainer"
        archive.addFile(path+"/experiment.xml", "./experiment.xml",libcombine.KnownFormats_lookupFormat("sbml"), True)
        archive.addFile(path+"/data/m0.csv", "./data/data.csv",libcombine.KnownFormats_lookupFormat("csv"))
        archive.addFile(path+"/metadata.rdf", "./matadata.rdf",libcombine.KnownFormats_lookupFormat("rdf"))
        archive.addFile(path+"/metadata_1.rdf", "./matadata_1.rdf",libcombine.KnownFormats_lookupFormat("rdf"))
        archive.addFile(path+"/metadata_2.rdf", "./matadata_2.rdf",libcombine.KnownFormats_lookupFormat("rdf"))
        archive.addFile(self.config["enzymeml"]["biocathub_model_path_local"], self.config["enzymeml"]["biocathub_paht_in_omex_archive"], libcombine.KnownFormats.lookupFormat("json"))
        archive.writeToFile(self.config["enzymeml"]["path_updated_by_biocathub_model"])
        if os.path.exists("assets/enzymemlContainer"):
            shutil.rmtree("assets/enzymemlContainer")
        if os.path.exists("assets/container.zip"):
            os.remove("assets/container.zip")       

        '''
        
        try:
            if os.path.exists(self.config["enzymeml"]["path_updated_by_biocathub_model"]):
                os.remove(self.config["enzymeml"]["path_updated_by_biocathub_model"])
            archive = libcombine.CombineArchive()
            archive.initializeFromArchive(self.config["enzymeml"]["path_incoming_pyenzyme"])
            self.save_bch_model_local()
          
            archive.addFile(self.config["enzymeml"]["biocathub_model_path_local"], self.config["enzymeml"]["biocathub_paht_in_omex_archive"], libcombine.KnownFormats.lookupFormat("json"))
  
            archive.writeToFile(self.config["enzymeml"]["path_updated_by_biocathub_model"])
        except Exception as err: 
            print("error adding the biocathub model")
            print(err)
            raise
    '''




    

