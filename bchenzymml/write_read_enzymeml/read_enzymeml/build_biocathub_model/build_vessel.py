from bchenzymml.models.biocathub_model import BioCatHubModel, Vessel


class BuildVessel:
    
    def __init__(self, enzml_model):
        self.enzml_model = enzml_model

    def build_vessel(self):
        try:
            vessel = self.enzml_model["vessels"]
            new_vessel = Vessel(type="vessel", unit="mmol/L", volume=1, others=[])
            print(new_vessel)
            return new_vessel.dict()
        except:
            print("no vessel")