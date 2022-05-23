from bchenzymml.models.enzymeml_vessel import VesselDetail
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
            vessel_details = VesselDetail.from_orm(Vesselcls(v["type"], v["volume"], unit, True, "v1"))
            vessel_dict = {}
            vessel_dict["vessel1"] = vessel_details.dict()
            return vessel_dict
        
        except Exception as err:
            print("error in vessel_builder", err)
            raise



