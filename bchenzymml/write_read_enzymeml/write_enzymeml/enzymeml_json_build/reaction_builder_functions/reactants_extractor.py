


class BCHReactantsExtractor:
    '''
        Extracts the reactants from the biocathub object.

        There are at least two different entities which require the reactants from the biocathub object. 
        - enzymeml reactants
        - enzymeml reactions

        These objects need different contents of the biocathub reagents object:
        - The enzymeml reactants, only need the name, conentration etc. and no reaction specifics
        - The enzymeml reaction need a small subset ob the enzymeml reactants and the connetion with the reaction

        Attributes
        ----------
        bch_dict: dict dictionary with the structure of the biocathub data model

        Methods
        -------
        
    '''

    def __init__(self, bch_dict:dict):
        self.bch_dict = bch_dict

    
    def extract_enzymes(self):

        try:
            enzymes = self.bch_dict["enzymes"]
            return enzymes
        
        except Exception as err:
            print("error")
            print(self.bch_dict["title"])
            raise

        
    def extract_all_reactants(self):

        enzymes = self.extract_enzymes()
        reactants_list = []
        for i in enzymes:
            educts = i["reaction"]["educts"]
            for j in educts:
                reactants_list.append(j)
            for k in i["reaction"]["products"]:
                reactants_list.append(k)
    
        return reactants_list

    
    def qery_reactants_list(self, existing_list, entry):
        '''
            querys if a reactant is alredy existing in the reactants list to prevent the collection of doublets

            Attributes
            ---------
                existing list:list; the list containing the already collected reactants
                entry: dict; Reactant object to be checked if already exiting in the existing_list
            
            Returns
            --------
                query_result:bool; returns if a entry name is already present (true) or if the name cannot be found in the existing list

        '''

        query_list = [name["name"] for name in existing_list]
        query_result = entry["name"] in query_list
        return query_result

    
    def add_reactant(self, existing_list, entry):
        '''
            adds the id to a new reactant element.

            Attributes
            ----------
                existing list:list; the list containing the already collected reactants
                entry: dict; Reactant object to be checked if already exiting in the existing_list
        
        '''

        new_id = len(existing_list)
        entry["id"] = "s"+str(new_id)
        return entry


    
    def build_reactants_dict(self):
        '''
            the reactants extracted need to be collected in one list, checked for duplicated and assigned with identifieres

            Attributes
            ----------
                None

            Return
            -------
                reactants_list:list; List containing the reactants described with identifiers and without of doublets
        '''

        reactants = self.extract_all_reactants()
        reactants_list = []

        for reac in reactants:
            
            if len(reactants_list) <= 0:   
                reactants_list.append(self.add_reactant(reactants_list, reac))
                
            elif len(reactants_list) >= 0:
                if not self.qery_reactants_list(reactants_list, reac):
                    reactants_list.append(self.add_reactant(reactants_list, reac))

        #print("reactants_list",reactants_list)
        
        return reactants_list



        