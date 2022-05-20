import bchenzymml.zenodo_adapter.upload_enzymeml_to_zenodo as upload_adapter
import bchenzymml.zenodo_adapter.zenodo_connector

'''


data_test = {
    "metadata": {
        "title": "EnzymeML document new",
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


def test_upload():
    new_upload = upload_adapter.EnzymeMLUploader(test_file, data_test)
    upload = new_upload.upload_enzyme_ml()
    print(upload)



def test_upload():
    print("Uploaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaad")
    newUpload = upload_adapter.EnzymeMLUploader(test_file, data_test)
    
'''