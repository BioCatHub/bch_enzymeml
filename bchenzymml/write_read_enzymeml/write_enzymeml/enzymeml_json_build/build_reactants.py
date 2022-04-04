from bchenzymml.models.enzymeml_reactants import ReactantsDetail
from bchenzymml.models.enzymeml_classes import Reactantcls




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

    def reactant_extractors(self):
        enzymes = self.bch_dict["enzymes"]
        reactants_list = []
        for i in enzymes:
            educts = i["reaction"]["educts"]
            for j in educts:
                reactants_list.append(j)
            products = i["reaction"]["products"]
            for k in products:
                reactants_list.append(k)

        #print("************* reactants**********", reactants_list)

        return reactants_list

    
    def build_reactant_classes(self):
        '''
            builds the pydantic models based on the submitted values
        '''

        reactants_list = self.reactant_extractors()
        reactants_dict={}
        for i in reactants_list:
            new_reactant = ReactantsDetail.from_orm(Reactantcls(i["name"], 
                                                                "s"+str(reactants_list.index(i)),
                                                                "v1",
                                                                "meta_id"+str(reactants_list.index(i)),
                                                                i["concentration"],
                                                                "mmole",
                                                                i["smiles"]))
            reactants_dict["reactant"+str(reactants_list.index(i))] = new_reactant.dict()
        
        print("******** reactants_dict*******",reactants_dict)

        return reactants_dict

    def build_reactants(self):
        

        try:
            reactants = self.build_reactant_classes()
            return reactants
        
        except Exception as err:
            # raise Exception("Error in Vessels")
            raise