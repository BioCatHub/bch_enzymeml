from bchenzymml.models.enzymeml_reactants import ReactantsDetail
from bchenzymml.models.enzymeml_classes import Reactantcls
from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.reaction_builder_functions.reactants_extractor import BCHReactantsExtractor



class ReactantsBuilder:
    '''
        Builds the EnzymeML_Json reactant dictionary.

            This class extracts at frist all the reactants from the enzyme objects of BioCatHub and combines them in the EnzymeML reactants objects.
    
        Args
        ----
        bch_dict: dict; Dictionary with the structure of the BioCatHub model

        Returns
        -------
        enzmL_reactants: dict; Creator object with the structure of the EnzymeML_json vessel model

    '''

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

   
    def build_reactant_classes(self):
        '''
            builds the pydantic models based on the submitted values
        '''
        try:
            reactants_list = BCHReactantsExtractor(self.bch_dict).build_reactants_dict()
        except Exception as Err:
            print("Fehler im reactantsextractor", err)
            raise
        reactants_dict={}
        for i in reactants_list:            
            unit = UnitBuilder().convert_from_bch_to_enzymeml(i["unit"]) #TODO #33
            try:
                print("Went well before")
                index = str(reactants_list.index(i))
                print("Went well after")
            except Exception as Err:
                print("indexing Error in build_reactant_classes", Err)

            try:
                print("Went well before in new reactant")
                new_reactant = ReactantsDetail.from_orm(Reactantcls(i["name"], 
                                                                    i["id"],
                                                                    "v1",
                                                                    "meta_id"+index,
                                                                    i["concentration"],
                                                                    unit,
                                                                    i["smiles"]))
                reactants_dict["reactant"+index] = new_reactant.dict()
                print("Went well after in new reactant")
            except Exception as err:
                print("Reactants_builder error", err)
                raise
        
        #print("******** reactants_dict*******",reactants_dict)
        print(reactants_dict)
        return reactants_dict

    def build_reactants(self):
        

        try:
            reactants = self.build_reactant_classes()
            return reactants
        
        except Exception as err:
            print("error in build_reactants")
            # raise Exception("Error in Vessels")
            raise