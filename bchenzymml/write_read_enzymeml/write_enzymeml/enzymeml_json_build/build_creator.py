from bchenzymml.models.enzymeml_model_generals_creator import CreatorDetail
from bchenzymml.models.enzymeml_classes import Creatorcls
from bchenzymml.Exceptions.enzymeml_write_exceptions import CreatorError



class CreatorBuilder:
    '''
        Builds the EnzymeML_Json creator dictionary
    
        Args
        ----
        bch_dict: dict; Dictionary with the structure of the BioCatHub model

        Returns
        -------
        enzmL_creator: dict; Creator object with the structure of the EnzymeML_json vessel model

    '''

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

    def extract_creator(self):
        '''
            extracts the vessel object from the bch_dict dictionary
        '''

        vessels = self.bch_dict["user"]
        return vessels
    
    def build_creator(self):

        try:
            c = self.extract_creator()
            creator_details = CreatorDetail.from_orm(Creatorcls(c["firstName"], c["lastName"], c["email"], "a0"))
            #TODO #25
            
            creator_dict = {"creator1":creator_details.dict()}
    
            return creator_dict
        
        except Exception as err:
            # raise Exception("Error in Vessels")
            raise CreatorError

