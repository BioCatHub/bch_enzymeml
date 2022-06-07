import bchenzymml.zenodo_adapter.upload_enzymeml_to_zenodo as upload_adapter
import bchenzymml.zenodo_adapter.zenodo_connector as connector




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

def get_entries():

    all_entries= connector.ZenodoConnector("path")
    deposits = all_entries.get_all_entries()
    depositions = []
    for element in deposits:
        metadata = element['metadata']
        creator = metadata['creators'][0]
        deposition = {
            'id': element['id'],
            'title': metadata['title'],
            'date': metadata['publication_date'],
            'name': creator['name'],
            'affiliation': creator['affiliation'],
            'link': element['links']['html']
        }
        depositions.append(deposition)
    return depositions

def test_names_of_entries():
    payload = get_entries()
    for i in payload:
        print(i["title"])


