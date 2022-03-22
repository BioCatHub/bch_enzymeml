from bchenzymml.models.enzymeml_protein import ProteinDetail, ProteinContainer
from bchenzymml.models.enzymeml_classes import Proteincls
from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder



class ProteinBuilder:
    '''
        Builds the EnzymeML_Json protein dictionary
    
        Args
        ----
        bch_dict: dict; Dictionary with the structure of the BioCatHub model

        Returns
        -------
        enzmL_proteins: dict; Protein object with the structure of the EnzymeML_json vessel model

    '''

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

    def extract_proteins(self): 
        '''
            extracts the protein object from the bch_dict dictionary
        '''

        proteins = self.bch_dict["enzymes"]
        return proteins   
    
    def build_proteins(self):

        try:
            proteins = self.extract_proteins()
            #print(proteins)

            
            protein_dict = {}

            for i in range(len(proteins)):

                
                p = proteins[i]
                unit = UnitBuilder().convert_from_bch_to_enzymeml(p["unit"])
                protein = ProteinDetail.from_orm(Proteincls(p["name"],
                                                            "p"+str(i), 
                                                            "v1", 
                                                            "meta"+str(i),
                                                            p["concentration"],
                                                            True, 
                                                            unit, 
                                                            "SBO:0000176", 
                                                            p["sequence"], 
                                                            p["ecNumber"]))
                
                protein_dict["protein"+str(i)] = protein.dict()

            
            protein_container = ProteinContainer(__root__=protein_dict)

            #print("der protein Container ist",protein_container )

            return protein_container.__root__

        except Exception as e:
            raise




        '''

        try:
            p = self.extract_proteins()
            protein_details = ProteinDetail.from_orm(Proteincls(p["name"], "p0", "v1", "meta_p0", p["concentration"], True, p["unit"],"SBO:0000176", p["sequence"], p["ecNumber"]))
            p_container = ProteinContainer(__root__={"protein1":protein_details.dict()})
            return p_container.__root__
        
        except Exception as err:
            raise
        '''