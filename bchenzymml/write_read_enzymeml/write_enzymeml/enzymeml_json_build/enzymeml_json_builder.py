from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_vessels import VesselBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_model import EnzymeMLModelBuilder
from bchenzymml.Exceptions.enzymeml_write_exceptions import VesselError, ProteinError, ProteinKeyError, CreatorError, ReactantsError, ReactionsError, MeasurementError

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

        try:
    
            bch_dict = json.loads(self.bch_json)
            return self.bch_json
        except Exception as err:
            return self.bch_json

    def build_enzymeml_json(self):
        #bch_dict = self.convert_JSON_to_dict()        
        
        try:
            enzml_model = EnzymeMLModelBuilder(self.bch_json).build_generals()
            return enzml_model

        except VesselError as err:
            print("Error in EnzymeMLJson Builder Vessel")
            raise
            
        except ProteinKeyError as err:
            print("There is a missing value in the proteins", err.missing_key)
            raise
        
        except CreatorError as err:
            print("Error in EnzymeMLJson Creator")
            raise

        except ReactantsError as err:
            print("Error in EnzymeMLJson Reactants")
            raise

        except ReactionsError as err:
            print("Error in EnzymeMLJson Builder, Reactions")
            raise ReactionsError(err)

        except Exception as err:
            print("unkown err",err)
            raise


