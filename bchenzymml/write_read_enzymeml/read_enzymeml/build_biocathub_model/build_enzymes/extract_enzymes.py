

class EnzymeExtractor:
    
    def __init__(self, enzml_model):
        self.enzml_model = enzml_model

    def get_enzymes(self):
        enzymes = self.enzml_model["proteins"]
        for i in enzymes:
            print("enzme", enzymes["p0"])
        self.get_reactions()

    def get_reactions(self):
        reactions = self.enzml_model["reactions"]
        for i in reactions:
            print("reaction",reactions[i])

    