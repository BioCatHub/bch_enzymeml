from bchenzymml.models.biocathub_model import BioCatHubModel
from bchenzymml.write_read_enzymeml.read_enzymeml.build_biocathub_model.build_user import BuildUser


class BuildBioCatHubModel(BuildUser):

    def __init__(self, enzml_model):
        super().__init__(enzml_model)
        self.user = self.build_user()
    

    
    def build_generals(self):
        print(self.enzml_model)
        model = BioCatHubModel(title = "Hallo")
        model_dict = model.dict(exclude_none=True)
        return model_dict