from bchenzymml.models.enzymeml_reactions import ReactionDetail
from bchenzymml.models.enzymeml_classes import Reactioncls
from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder
import bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.measurement_builder_functions.replicates_mapper



class MeasurementBuilder:
    '''
        Builds the EnzymeML_Json reaction dictionary.

        Args
        ----
        bch_dict: dict; Dictionary with the structure of the BioCatHub model

        Returns
        -------
        enzmL_measurements: dict; Reaction object with the structure of the EnzymeML_json measurement model

    '''

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict


    def measurement_extractor(self):
        pass

    def reaction_extractors(self):

        reactions_list = []
        #print(reactions_list)
        
        reactions = {}

        for i in reactions_list["participants"]:
            entry = reactions_list["participants"][i]
            #print(entry)
            conditions = reactions_list["conditions"]

            new_reaction = ReactionDetail.from_orm(Reactioncls(
                                                                entry["name"], 
                                                                conditions["reversible"],
                                                                conditions["temperature"],
                                                                conditions["temperature_unit"],
                                                                conditions["ph"],
                                                                entry["id"], 
                                                                entry["meta_id"],
                                                                entry["educts"],
                                                                entry["products"]
                                                                ))
            reactions[i]=new_reaction.dict()
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