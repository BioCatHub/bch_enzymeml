from bchenzymml.models.biocathub_model import BioCatHubModel, Vessel


class BuildVessel:
    
    def __init__(self, enzml_model):
        self.enzml_model = enzml_model

    def build_vessel(self):
        try:
            vessel = self.enzml_model["vessels"]["v0"]
            vessel_type = vessel["name"]
            vessel_volume = vessel["volume"]
            vessel_volume_unit = vessel["unit"]
            new_vessel = Vessel(type=vessel_type, unit=vessel_volume_unit, volume=vessel_volume, others=[])
            print(new_vessel)
            return new_vessel.dict()
        except:
            print("no vessel")
            raise
