from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_vessels import VesselBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_proteins import ProteinBuilder



class EnzymeMLModelBuilder:

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

    def build_generals(self):
        try:
            vessels = VesselBuilder(self.bch_dict).build_vessels()
        except Exception as e:
            raise Exception("Error in Vessels")

        proteins = ProteinBuilder(self.bch_dict).build_proteins()

        generals = {}
        generals["vessels"] = vessels # TODO #20 

        return generals