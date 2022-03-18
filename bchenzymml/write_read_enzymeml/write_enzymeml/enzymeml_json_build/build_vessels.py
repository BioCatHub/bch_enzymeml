from bchenzymml.models.enzymeml_vessel import VesselDetail, VesselContainer, Vessel 
from bchenzymml.models.enzymeml_classes import Vesselcls
from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder



class VesselBuilder:
    '''
        Builds the EnzymeML_Json vessel dictionary
    
        Args
        ----
        bch_dict: dict; Dictionary with the structure of the BioCatHub model

        Returns
        -------
        enzmL_vessels: dict; Vessel object with the structure of the EnzymeML_json vessel model

    '''

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

    def extract_vessel(self): #TODO #19
        '''
            extracts the vessel object from the bch_dict dictionary
        '''

        vessels = self.bch_dict["vessel"]
        return vessels
    
    def build_vessels(self):

        try:
            v = self.extract_vessel()
            unit = UnitBuilder().convert_from_bch_to_enzymeml(v["unit"])
            print("die Einheit ist", unit)
            vessel_details = VesselDetail.from_orm(Vesselcls(v["type"], v["volume"], v["unit"], True, "v1", "asd", "sffdfd", "dsffd"))
            v_container = VesselContainer(__root__={"vessel1":vessel_details.dict()})
            return v_container.__root__
        
        except Exception as err:
            raise



