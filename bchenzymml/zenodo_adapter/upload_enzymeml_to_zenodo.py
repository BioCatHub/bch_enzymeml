import bchenzymml.zenodo_adapter.zenodo_connector as  zc
from assets.configurations import Configurations

token = {'access_token': 'h2VjvzgwrHAFLrQR3L0OhlsYPI8YE6H7VVHlTKWXfyCexOcIH0h8cMzZAtBq'}
url = "https://sandbox.zenodo.org/api/deposit/depositions"
headers = {"Content-Type": "application/json"}
config = Configurations.get_configuarations()

data_test = {
    "metadata": {
        "title": "New EnzymeML!",
        "upload_type": "dataset",
        "description": "EnzymeML document",
        "creators": [
            {"name": "Doe, John", "affiliation": "Zenodo"}
        ],
        "keywords":["enzymes", "biocatalysis"],
        "doi":""
    }
}

test_file = "assets/zenodo/BioCatHubomexupdate.omex"



class EnzymeMLUploader:
    '''
        Reads in the EnzymeML file and the metadata and returns them. The metadata are returned as dict
        the file as bytestream

        args:
            enzyme_ml: string; path to the enzymeML document to be uploaded
            metadata: dict; dict containing metadata nessecary for the upload
    

    '''

    def __init__(self, enzyme_ml, metadata):
        self.enzyme_ml = enzyme_ml
        self.metadata = metadata
        self.config = Configurations.get_configuarations()

    def upload_enzyme_ml(self):

        ''' 
            instanciates the zenodo connector class and calls the upload_enzymml method

            args:
                None
            
            returns:
                response: JSON; response code from Zenodo.
        '''

        upload = zc.ZenodoConnector(self.enzyme_ml)
        file_payload = self.read_in_binary()
        upl = upload.upload_enzymeml(self.metadata, headers, file_payload)
        return upl

    
    def read_in_binary(self):
        '''
            Reads in the Bytestring of the EnzymeML document and returns the binary

            args:
                self.enzyme_ml: String; path to the enzymeml file
    
            returns:
                upload_dict: dict; dictionary containing the binary of the enzymeml document

        '''
        enzyme_ml_binary = open(self.config["enzymeml"]["path_updated_by_biocathub_model"], 'rb')
        upload_dict = {"file":enzyme_ml_binary}
        return upload_dict




