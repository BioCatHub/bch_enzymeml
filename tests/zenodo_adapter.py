import bchenzymml.zenodo_adapter.upload_enzymeml_to_zenodo as upload_adapter

'''

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


def test_upload():
    new_upload = upload_adapter.EnzymeMLUploader(test_file, data_test)
    upload = new_upload.upload_enzyme_ml()
    print(upload)

'''