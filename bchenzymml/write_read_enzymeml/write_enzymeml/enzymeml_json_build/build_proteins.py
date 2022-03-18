from bchenzymml.models.enzymeml_protein import ProteinDetail, ProteinContainer, Protein
from bchenzymml.models.enzymeml_classes import Proteincls



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

        proteins = self.extract_proteins()
        print(proteins)



        '''

        try:
            p = self.extract_proteins()
            protein_details = ProteinDetail.from_orm(Proteincls(p["name"], "p0", "v1", "meta_p0", p["concentration"], True, p["unit"],"SBO:0000176", p["sequence"], p["ecNumber"]))
            p_container = ProteinContainer(__root__={"protein1":protein_details.dict()})
            return p_container.__root__
        
        except Exception as err:
            raise
        '''