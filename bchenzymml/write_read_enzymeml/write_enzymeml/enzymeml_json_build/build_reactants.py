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

   
    def build_reactant_classes(self): #TODO #36
        '''
            builds the pydantic models based on the submitted values
        '''
        try:
            reactants_list = BCHReactantsExtractor(self.bch_dict).build_reactants_dict()
            reactants_dict={}
        except Exception as Err:
            print("Fehler im reactantsextractor", err)
            raise
        
        for i in reactants_list:            
            unit = UnitBuilder().convert_from_bch_to_enzymeml(i["unit"]) #TODO #33
            try:
                #print("Went well before")
                index = str(reactants_list.index(i))
                #print("Went well after")
            except Exception as Err:
                print("indexing Error in build_reactant_classes", Err)

            try:
                reactant_base = self.check_completeness(i)
                #print("Went well before in new reactant", reactant_base)
                new_reactant = ReactantsDetail.from_orm(Reactantcls(reactant_base["name"], 
                                                                    reactant_base["id"],
                                                                    "v1",
                                                                    "meta_id"+index,
                                                                    reactant_base["concentration"],
                                                                    unit,
                                                                    reactant_base["smiles"]))
                reactants_dict["reactant"+index] = new_reactant.dict()
                #print("Went well after in new reactant", new_reactant)
                
            except Exception as err:
                print("Reactants_builder error", err)
                raise
            #print("BLOOOOOOOOOOOOOOOOOOOOOOOOOO")
            #print(reactants_dict)
            return reactants_dict
            

    def build_reactants(self):
    
        try:
            #print("Haaaaaaaaaaaaaaaaaaaaaaaaaaallo")
            reactants = self.build_reactant_classes()
            return reactants
        
        except Exception as err:
            print("error in build_reactants")
            # raise Exception("Error in Vessels")
            raise

    def check_completeness(self, reactant):
        '''
        checks if the submitted reactant elements of biocathub are complete, and refills them with placeholder not given, if missing

        Args:
            reactant (dict): A reactant object 

        Returns

            reactant_to_test (dict): A reactant object with missing fields annotated as _not given_
        '''

        reactant_to_test = reactant

        checklist = ["name", "id", "concentration", "smiles"]

        for i in checklist:
            if i not in reactant_to_test:
                if i == "concentration":
                    reactant_to_test[i]=0.0    
                reactant_to_test[i]="not given"
            else:
                pass
        return reactant_to_test