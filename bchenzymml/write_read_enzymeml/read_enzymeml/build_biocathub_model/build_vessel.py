from bchenzymml.models.biocathub_model import BioCatHubModel, Vessel


class BuildVessel:
    
    def __init__(self, enzml_model):
        self.enzml_model = enzml_model

    def build_vessel(self):
        try:
            vessel = self.enzymeM["vessel"]
        except:
            print("no vessel")