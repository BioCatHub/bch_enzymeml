from bchenzymml.models.zenodo_update_model import ZenodoMetadata

class ZenodoMetadataParser:

    def __init__(self, bch_model):
        self.bch_model = bch_model

    
    def parse_model(self):
        '''
            Extracts the information from the Biocathub model nessecary to describe the upload to Zenodo
        
        '''
        
        user = self.extract_creator()

        print(self.bch_model["title"])

        zenodo_metadata = ZenodoMetadata(   title=self.bch_model["title"], 
                                            upload_type="dataset", 
                                            description=self.bch_model["description"], 
                                            creators=[{"name": user["name"], "affiliation": user["institute"]}], 
                                            keywords=["biocatalysis"])
        print(zenodo_metadata.dict())
        metadata_container = {"metadata":zenodo_metadata.dict()}
        return metadata_container

    def extract_creator(self):

        '''
            Extracts the user from the biocathub model and returns the user in the Zenodo format as one entry: lastname, firstname
        
        '''

        user_entry = self.bch_model["user"]
        first_name = user_entry["firstName"]
        last_name = user_entry["lastName"]
        zenodo_creator = {"name":last_name + first_name, "institute":user_entry["institution"]}
        return zenodo_creator