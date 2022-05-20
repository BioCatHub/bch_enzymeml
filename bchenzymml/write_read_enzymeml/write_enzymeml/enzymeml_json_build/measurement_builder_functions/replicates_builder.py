from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.measurement_builder_functions.replicates_mapper import ReplicatesMapper
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.reaction_builder_functions.reactant_extractor_reaction import ReactionExtractor
from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder

from bchenzymml.models.enzymeml_measurement import ReplicatesDetails
from bchenzymml.models.enzymeml_classes import ReplicatesDetailscls

class ReplicatesBuilder(ReplicatesMapper):

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

    
    def extract_units(self, measurement): #TODO #29

        unit_y_values = measurement["y_unit"]
        unit_x_values = measurement["x_unit"]

        units = {
            "x_unit":UnitBuilder().convert_from_bch_to_enzymeml(unit_x_values),
            "y_unit":UnitBuilder().convert_from_bch_to_enzymeml(unit_y_values)
        }


        return units
    
    def extract_reagent_id_(self, measurement):
        
        reagent = {"name":measurement["reagent"]}
        reagent_id = ReactionExtractor(self.bch_dict).query_reagent_identifier(reagent)

        return reagent_id

    def build_replicates(self, measurement):

        replicate_list = []
        #self.extract_reagent_id_()

        units = self.extract_units(measurement)
        reagent_id = self.extract_reagent_id_(measurement)
        print("reagent id", reagent_id)
        replicate_series = self.extract_replicates(measurement)

        for k in range(len(replicate_series)-1):
            #print(k)
            #print("replicates series", replicate_series[f"y_values{k}"])
            replicate = ReplicatesDetails.from_orm(ReplicatesDetailscls(f"r{k}", 
                                                                        reagent_id, 
                                                                        units["y_unit"],
                                                                        units["x_unit"],
                                                                        replicate_series["x_values"],
                                                                        replicate_series[f"y_values{k}"]
                                                                        ))
            replicate_list.append(replicate.dict())
        
        return replicate_list
