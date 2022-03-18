from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_vessels import VesselBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_model import EnzymeMLModelBuilder

import json


class EnzymeMLJSONNuilder:
    '''
        Class which builds the EnzymeML JSON object based on the BioCatHub Moldel.
        
        Attributes
        ----------
        bch_json:JSON

        Methods
        -------
        convert_JSON_to_dict()
            converts the bch_json object to a python dictionary

    '''

    def __init__(self, bch_json):
        self.bch_json = bch_json

    
    def convert_JSON_to_dict(self):
        '''
            Converts the JSON object from the BioCatHub frontend to python dictionary

            Args
            ----
            bch_json: json 

            Returns
            -------
            bch_dict: dict

        '''
        bch_dict = json.loads(self.bch_json)
        return bch_dict

    def build_enzymeml_json(self):
        try:
            bch_dict = self.convert_JSON_to_dict()
            enzml_model = EnzymeMLModelBuilder(bch_dict).build_generals()
            print(enzml_model)
        except Exception as e:
            err = {"code":400, "err":"Error in Vessels"}
            return err

