from bchenzymml.models.enzymeml_model_generals_creator import CreatorDetail, CreatorContainer 
from bchenzymml.models.enzymeml_classes import Creatorcls



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
            creator_details = CreatorDetail.from_orm(Creatorcls(c["firstName"], c["lastName"], c["email"], "c1"))
            print(type(creator_details.dict()))
            print("creator dict*************",creator_details.dict()) #TODO #25
            c_container = CreatorContainer (__root__={"vessel1":creator_details.dict()})
            print("*******************Creaotr container:", c_container.__root__["vessel1"].dict())
            return c_container.__root__
        
        except Exception as err:
            # raise Exception("Error in Vessels")
            raise

