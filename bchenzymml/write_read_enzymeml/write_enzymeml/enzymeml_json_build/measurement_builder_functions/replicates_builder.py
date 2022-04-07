from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.measurement_builder_functions.replicates_mapper import ReplicatesMapper
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.reaction_builder_functions.reactant_extractor_reaction import ReactionExtractor

from bchenzymml.models.enzymeml_measurement import ReplicatesDetails
from bchenzymml.models.enzymeml_classes import ReplicatesDetailscls

class ReplicatesBuilder(ReplicatesMapper):

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

    
    def extract_units(self, measurement): #TODO #29

        unit_y_values = measurement["y_unit"]
        unit_x_values = measurement["x_unit"]

        units = {
            "x_unit":unit_x_values,
            "y_unit":unit_y_values
        }


        return units
    
    def extract_reagent_id(self, measurement):
        
        reagent = {"name":measurement["reagent"]}
        print("der reagent ist:", reagent)
        reagent_id = ReactionExtractor(self.bch_dict).query_reagent_identifier(reagent)

        return reagent_id

    def build_replicates(self):

        measurement = self.extract_measurements()
        units = self.extract_units(measurement[0])
        reagent_id = self.extract_reagent_id(measurement[0])
        replicate_series = self.extract_replicates()

        replicate = ReplicatesDetails.from_orm(ReplicatesDetailscls("r1", 
                                                                    reagent_id, units["y_unit"],
                                                                    units["x_unit"],
                                                                    replicate_series["x_values"],
                                                                    replicate_series["y_values0"]
                                                                    ))
        return replicate.dict()

        #print(replicate_series)


        replicates_list = []

        



        print("Hallloooo!!!!!!!!!!!!!!")

        return measurement