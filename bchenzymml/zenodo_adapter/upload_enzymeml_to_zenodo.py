import bchenzymml.zenodo_adapter.zenodo_connector as  zc

token = {'access_token': 'h2VjvzgwrHAFLrQR3L0OhlsYPI8YE6H7VVHlTKWXfyCexOcIH0h8cMzZAtBq'}
url = "https://sandbox.zenodo.org/api/deposit/depositions"
headers = {"Content-Type": "application/json"}


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

test_file = "NewEnzymeML.omex"



class EnzymeMLUploader:

    def __init__(self, enzyme_ml, metadata):
        self.enzyme_ml = enzyme_ml
        self.metadata = metadata

    def upload_enzyme_ml(self):
        upload = zc.ZenodoConnector(url, token, self.enzyme_ml)
        self.read_in_binary(self.enzyme_ml)
        upload.upload_enzymeml(data_test, headers)
    
    def read_in_binary(self):
        '''
            Reads in the Bytestring of the EnzymeML document
        '''

        enzyme_ml_binary = open(test_file, 'rb')
        upload_dict = {"file":enzyme_ml_binary}
        return upload_dict




