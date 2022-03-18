from bchenzymml.models.biocathub_test_model import model
from bchenzymml.models.biocathub_test_model_vessel_err import model as vessel_err


from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.enzymeml_json_builder import EnzymeMLJSONNuilder

def test_enzymeML_builder():

    new_model = EnzymeMLJSONNuilder(model).build_enzymeml_json()
    vessel_err_test = EnzymeMLJSONNuilder(vessel_err).build_enzymeml_json()
    print(vessel_err_test)