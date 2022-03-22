from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_vessels import VesselBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_proteins import ProteinBuilder
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.build_creator import CreatorBuilder



class EnzymeMLModelBuilder:

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

    def build_generals(self):
        try:
            vessels = VesselBuilder(self.bch_dict).build_vessels()
        except Exception as e:
            raise 
        
        try:
            proteins = ProteinBuilder(self.bch_dict).build_proteins()
            #print("die proteins sind im build model", proteins)
        except:
            #print("die proteins sind im build model, Fehler!", proteins)
            raise
        
        try:
            creators = CreatorBuilder(self.bch_dict).build_creator()
            print("die creators sind sind im build model", creators)
        except:
            print("die proteins sind im build model, Fehler!", proteins)
            raise


        generals = {}
        generals["vessels"] = vessels # TODO #20 
        generals["proteins"] = proteins
        generals["creators"] = creators

        return generals