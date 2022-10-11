from libcombine import CombineArchive

import json
import os

class ExtractFromEnzymeML:
    ''' 
        This class handles the extraction of files from omex Archives. 
        !! Note !!
        Libcombine (https://github.com/sbmlteam/libcombine) stores extracted files by default locally. The extracted files will be stored in the assets folder of this library

        ------------
        attr:
        file: str 
            path of the enzymeML document from which files have to be extracted
    '''

    def __init__(self, file_path):
        self.file_path = file_path

    def extract_bch_model(self):
        '''
            function screening the submitted enzymeml document for the biocathub.json file. Upon finding the file the following workflow takes place:
            - Extracting biocathub.json to the assets folder with the path assets/biocathub.json
            - reading in the file and converting it to a binary format 
            - returning the binary format

            Parameters
            ------------
            None

            Returns
            ----------
            the biocathub.json file as binary 
        '''

        archive = CombineArchive()
        archive.initializeFromArchive(self.file_path) #TODO #32
        experiment = False
        if os.path.exists("assets/biocathub.json"):
                os.remove("assets/biocathub.json")
        for i in range(archive.getNumEntries()):
            entry = archive.getEntry(i)
            #print("number of entries is",archive.getNumEntries() )
            if entry.getLocation() == "biocathub.json": # TODO #8
                archive.extractEntry(entry.getLocation(), "assets/biocathub.json")
                with open("assets/biocathub.json") as extract:
                    experiment = json.load(extract)
                    #print("the xperiment is:", experiment)
                    return experiment
                break
            else:
                pass
        