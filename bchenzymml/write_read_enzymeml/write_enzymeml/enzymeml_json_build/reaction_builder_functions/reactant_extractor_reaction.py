from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.reaction_builder_functions.reactants_extractor import BCHReactantsExtractor
from bchenzymml.models.enzymeml_reactions import ReagentDetail
from bchenzymml.models.enzymeml_classes import ReagentDetailscls
from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder


class ReactionExtractor(BCHReactantsExtractor): # TODO #27
    
    def __init__(self, bch_dict):
        self.bch_dict = bch_dict
        self.reagent_list = self.build_reactants_dict() 
        self.condition = bch_dict["condition"]

    
    def query_reagent_identifier(self, reagent):
        '''
            Queries the identifier needed to describe reactants in the enzymeml reaction object based on the reactants_list generated in the build_reactants_dict() method

            Args
            ----
                reagent:dict; dictionary containing information about one reagent
                reagent_list; list containing all the reactants
            
            Returns
            -------
                id: Str; id of the respecive reagent        
        '''

        for i in self.reagent_list:

            if i["name"] == reagent["name"]:
                return i["id"]
            else:
                pass

    
    
    def extract_reaction_participants(self):
        enzymes = self.extract_enzymes()
        
        reaction_participants={}

        
        for i in enzymes:
            index = enzymes.index(i)
            reaction = i["reaction"]
            reaction_dict = {}
            educts_list = []
            products_list=[]

            for j in reaction["educts"]:
                new_educt = ReagentDetail.from_orm(ReagentDetailscls(
                                                                        self.query_reagent_identifier(j),
                                                                        1,
                                                                        False,
                                                                        "SBO:0000176"
                ))
                educts_list.append(new_educt.dict())

            for j in reaction["products"]: # TODO #34 
                new_product = ReagentDetail.from_orm(ReagentDetailscls(
                                                                        self.query_reagent_identifier(j),
                                                                        1,
                                                                        False,
                                                                        "SBO:0000176" #TODO #35
                ))
                products_list.append(new_product.dict())
            

            try:
                reaction_dict["name"] = reaction["value"]
            except Exception as Err:
                reaction_dict["name"] = "not defined"

            reaction_dict["educts"] = educts_list
            reaction_dict["products"] = products_list
            reaction_dict["id"] = "r"+str(index)
            reaction_dict["meta_id"] = "meta_r"+str(index)
            reaction_participants["reaction"+str(index)] = reaction_dict
        
        #print("Reaction participants")

        return reaction_participants

    
    def extract_conditions(self):

        cond = {}
        cond["reversible"] = True
        cond["temperature"] = self.condition["temp"]
        cond["temperature_unit"] = UnitBuilder().convert_from_bch_to_enzymeml(self.condition["unit"])
        cond["ph"] = self.condition["ph"]

        return cond

    def extract_reaction_dict(self):

        
        reaction_dict = {}

        try:
            reaction_dict["conditions"] = self.extract_conditions()
        except Exception as e:
            print("Eroor in extracting conditions", e)
        try:
            reaction_dict["participants"] = self.extract_reaction_participants()
        except Exception as e:
            print("Eroor in extracting participants", e)
        return reaction_dict
        
        
            


            

            
