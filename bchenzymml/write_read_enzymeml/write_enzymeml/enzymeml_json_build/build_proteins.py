from bchenzymml.models.enzymeml_protein import ProteinDetail, ProteinContainer
from bchenzymml.models.enzymeml_classes import Proteincls
from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder
from bchenzymml.Exceptions.enzymeml_write_exceptions import VesselError, ProteinKeyError, CreatorError, ReactantsError, ReactionsError



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
        protein_dict = {}
        for i in range(len(proteins)):
            p = self.check_completeness(proteins[i])
            unit = UnitBuilder().convert_from_bch_to_enzymeml(p["unit"])
            try:
                protein = ProteinDetail.from_orm(Proteincls(p["name"],
                                                            "p"+str(i),
                                                            "v1",
                                                            "meta"+str(i),
                                                            p["concentration"],
                                                            True,
                                                            unit,
                                                            "SBO:0000176",
                                                            p["sequence"],
                                                            p["ecNumber"] #TODO #31

                                                            ))

                protein_dict["protein"+str(i)] = protein.dict()
            except KeyError as error:
                raise ProteinKeyError(str(error.args[0]))
        return protein_dict

    def check_completeness(self, protein):
        '''
        checks if the submitted Protein elements of biocathub are complete, and refills them with placeholder not given, if missing

        Args:
            protein (dict): A protein or enzyme object of the BioCatHub model

        Returns

            protein_to_test (dict): A protein or enzyme object of the BioCatHub model, with missing fields annotated as _not given_
        '''

        checklist = ["name","concentration","sequence", "ecNumber"]
        protein_to_test = protein

        for i in checklist:
            if i not in protein_to_test:
                protein_to_test[i]="not given"
            else:
                pass
        return protein_to_test





