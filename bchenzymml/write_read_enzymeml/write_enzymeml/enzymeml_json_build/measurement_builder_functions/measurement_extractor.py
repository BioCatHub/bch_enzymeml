from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.measurement_builder_functions.replicates_builder import ReplicatesBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.reaction_builder_functions.reactant_extractor_reaction import ReactionExtractor
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_reactants import ReactantsBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.reaction_builder_functions.reactant_extractor_reaction import ReactionExtractor

from bchenzymml.models.enzymeml_measurement import SpeciesMeasurementDetail
from bchenzymml.models.enzymeml_classes import SpeciesMeasurementDetailcls

from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder


class MeasurementExtractor(ReplicatesBuilder):

    def __init__(self, bch_dict):
        super().__init__(bch_dict)
        self.reactants = ReactantsBuilder(
            self.bch_dict).build_reactant_classes()

    def extract_initial_concentration(self, id):

        for i in self.reactants:
            base = self.reactants[i]

            if base["id"] == id:
                return base["init_conc"]

    def extract_reagent_id(self, reagent):

        reagent_dict = {"name": reagent}
        reagent_id = ReactionExtractor(
            self.bch_dict).query_reagent_identifier(reagent_dict)
        return reagent_id

    def extract_measured_unit(self, measurement):  # TODO #29

        unit = UnitBuilder().convert_from_bch_to_enzymeml(
            measurement["y_unit"])

        return unit

    def build_measurement(self):

        measurements_enzymeml = {}

        measurements = self.bch_dict["experimentalData"]

        for i in measurements["measurements"]:

            reagent_id = self.extract_reagent_id(i["reagent"])
            init_conc = self.extract_initial_concentration(reagent_id)
            unit = self.extract_measured_unit(i)
            replicates = self.build_replicates(i)
            print("die init conc ist", init_conc, unit)

            measurement = SpeciesMeasurementDetail.from_orm(SpeciesMeasurementDetailcls(
                init_conc,
                unit,
                reagent_id,
                replicates
            ))

            id = 0
            rest = measurement.dict()
            measurements_enzymeml[f"measur{id}"] = rest

            return measurements_enzymeml
