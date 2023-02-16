from bchenzymml.models.enzymeml_classes import MeasurementDetailcls
from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.measurement_builder_functions.measurement_extractor import MeasurementExtractor
from bchenzymml.models.enzymeml_measurement import MeasurementDetail
from bchenzymml.Exceptions.enzymeml_write_exceptions import MeasurementError


class MeasurementBuilder:
    '''
        Builds the EnzymeML_Json reaction dictionary.

        Args
        ----
        bch_dict: dict; Dictionary with the structure of the BioCatHub model

        Returns
        -------
        enzmL_measurements: dict; Reaction object with the structure of the EnzymeML_json measurement model

    '''

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict


    def build_species(self):
        

        try:
            species_dict = {}
            reagent_measurements = MeasurementExtractor(self.bch_dict).build_measurement()
            species_dict["reactants"] = reagent_measurements
            species_dict["proteins"] = {}
            return species_dict
        
        except Exception as err:
            print("Error in species building", err)
            raise
    
    
    def build_measurements(self):

        try:

            species = self.build_species()

            measurements_model = MeasurementDetail.from_orm(MeasurementDetailcls("BioCatHub_measurement", "m0", species))
            measurements_dict = {"measurement0":measurements_model.dict()}
            #print(measurements_dict)
            return measurements_dict
        except Exception as Error:
            print("something wrong with the measurements", Error)
            raise MeasurementError 

    