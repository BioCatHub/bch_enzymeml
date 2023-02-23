from bchenzymml.models.biocathub_model import BioCatHubModel, User


class BuildUser:
    
    def __init__(self, enzml_model):
        self.enzml_model = enzml_model

    def build_user(self):
        try:
            creators = self.enzml_model["creators"]
            print(self.enzml_model["name"])
            print("the creators are")
        except:
            print("no creators")