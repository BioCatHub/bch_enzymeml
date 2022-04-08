from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_vessels import VesselBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_proteins import ProteinBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_creator import CreatorBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_reactants import ReactantsBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_reactions import ReactionBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_measurements import MeasurementBuilder

from bchenzymml.Exceptions.enzymeml_write_exceptions import VesselError, ProteinError, CreatorError, ReactantsError, ReactionsError


class EnzymeMLModelBuilder:

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

    def build_generals(self):
        try:
            vessels = VesselBuilder(self.bch_dict).build_vessels()
        except Exception as e:
            raise VesselError

        try:
            proteins = ProteinBuilder(self.bch_dict).build_proteins()
            #print("die proteins sind im build model", proteins)
        except:
            #print("die proteins sind im build model, Fehler!", proteins)
            raise ProteinError

        try:
            creators = CreatorBuilder(self.bch_dict).build_creator()
        except:
            print("die proteins sind im build model, Fehler!", proteins)
            raise CreatorError

        try:
            reactants = ReactantsBuilder(self.bch_dict).build_reactants()
        except:
            print("die proteins sind im build model, Fehler!", proteins)
            raise ReactantsError

        try:
            reactions = ReactionBuilder(self.bch_dict).build_reactions()
        except:
            print("die proteins sind im build model, Fehler!", proteins)
            raise ReactionsError
        
        try:
            measurements = MeasurementBuilder(self.bch_dict).build_measurements()
        except:
            print("die proteins sind im build model, Fehler!", proteins)
            raise

        generals = {}
        generals["name"] = "experiment"
        generals["vessels"] = vessels  # TODO #20
        generals["proteins"] = proteins
        generals["creators"] = creators
        generals["reactants"] = reactants
        generals["reactions"] = reactions
        generals["measurements"] = measurements
        return generals
