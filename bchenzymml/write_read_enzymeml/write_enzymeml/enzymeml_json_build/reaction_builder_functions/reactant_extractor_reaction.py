from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.reaction_builder_functions.reactants_extractor import BCHReactantsExtractor
from bchenzymml.models.enzymeml_reactions import ReagentDetail
from bchenzymml.models.enzymeml_classes import ReagentDetailscls


class ReactionExtractor(BCHReactantsExtractor): # TODO #27
    
    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

    
    def extract_reaction_participants(self):
        enzymes = self.extract_enzymes()

        reaction_participants={}

        for i in enzymes:
            index = enzymes.index(i)
            reaction = i["reaction"]
            reaction_dict = {}
            educts = reaction["educts"]
            products = reaction["products"]
            educts_list = []
            products_list=[]

            for j in educts:
                educts_dict= {}
                educts_dict["name"] = j["name"]
                educts_dict["stoichiometry"] = 1
                educts_dict["constant"] = False
                educts_dict["ontology"] = "SBO:0000176"

                educts_list.append(educts_dict)

            for k in products:
                products_dict = {}
                products_dict["name"] = j["name"]
                products_dict["stoichiometry"] = 1
                products_dict["constant"] = False
                products_dict["ontology"] = "SBO:0000176"

                products_list.append(products_dict)

            reaction_dict["name"] = reaction["value"]
            reaction_dict["educts"] = educts_list
            reaction_dict["products"] = products_list

            reaction_participants["reaction"+str(index)] = reaction_dict

        return reaction_dict

            

            
