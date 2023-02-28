from bchenzymml.models.biocathub_model import BioCatHubModel
from bchenzymml.write_read_enzymeml.read_enzymeml.build_biocathub_model.build_user import BuildUser
from bchenzymml.write_read_enzymeml.read_enzymeml.build_biocathub_model.build_vessel import BuildVessel
from bchenzymml.write_read_enzymeml.read_enzymeml.build_biocathub_model.build_condition import BuildCondition
from bchenzymml.write_read_enzymeml.read_enzymeml.build_biocathub_model.build_enzymes.extract_enzymes import EnzymeExtractor

class BuildBioCatHubModel(BuildUser, BuildVessel, BuildCondition, EnzymeExtractor):

    def __init__(self, enzml_model):
        super().__init__(enzml_model)
        self.user = self.build_user()
        self.vessel = self.build_vessel()
        self.condition = self.build_condition()
        self.enzymes = self.get_enzymes()
    

    
    def build_generals(self):
        #print(self.enzml_model)
        #print("condition is", self.condition)
        model = BioCatHubModel(title = "Hallo", vessel=self.vessel, condition=self.condition)
        model_dict = model.dict(exclude_none=True)
        print("the model is", model)
        return model_dict