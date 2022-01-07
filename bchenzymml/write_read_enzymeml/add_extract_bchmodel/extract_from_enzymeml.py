from libcombine import CombineArchive

import json

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
        archive.initializeFromArchive("assets/test.omex")
        experiment = False

        for i in range(archive.getNumEntries()):
            entry = archive.getEntry(i)
            if entry.getLocation() == "biocathub.json": # TODO #8
                archive.extractEntry(entry.getLocation(), "assets/biocathub.json")
                with open("assets/biocathub.json") as extract:
                    experiment = json.load(extract)
                    print("Hallo ", experiment)
                    return experiment
                break
            else:
                print("falscher Eintrag")
            return experiment
        