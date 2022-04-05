from bchenzymml.models.enzymeml_reactants import ReactantsDetail
from bchenzymml.models.enzymeml_classes import Reactantcls
from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder



class ReactionBuilder:
    '''
        Builds the EnzymeML_Json reaction dictionary.

        Args
        ----
        bch_dict: dict; Dictionary with the structure of the BioCatHub model

        Returns
        -------
        enzmL_reactions: dict; Reaction object with the structure of the EnzymeML_json reaction model

    '''

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

    def reaction_extractors(self):


        reactions = []
        for i in self.bch_dict["enzymes"]:
            reactions.append(i["reaction"])
            #print("Die Reaction ist:", i["reaction"])
        
        return reactions

        #print("************* reactants**********", reactants_list)


    
    def build_reactant_classes(self):
        '''
            builds the pydantic models based on the submitted values
        '''


    def build_reactions(self):
        

        try:
            reactions = self.reaction_extractors()
            return reactions
        
        except Exception as err:
            # raise Exception("Error in Vessels")
            raise