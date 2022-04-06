
import requests
import json
import os


from bchenzymml.models.biocathub_test_model import model
from bchenzymml.models.biocathub_test_model_vessel_err import model as vessel_err_test
from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.reaction_builder_functions.reactant_extractor_reaction import ReactionExtractor
from bchenzymml.Exceptions.enzymeml_write_exceptions import VesselError, ProteinError, CreatorError, ReactantsError, ReactionsError



from bchenzymml.write_read_enzymeml.write_enzymeml.enzymeml_json_build.enzymeml_json_builder import EnzymeMLJSONNuilder

def test_enzymeML_builder():

    new_model = EnzymeMLJSONNuilder(model).build_enzymeml_json()
    #vessel_err_test_model = EnzymeMLJSONNuilder(vessel_err_test).build_enzymeml_json()
    #print(vessel_err_test_model)
    #print(new_model)
    return new_model

def test_enzymeml_exception():
    
    try:
        new_model = EnzymeMLJSONNuilder(vessel_err_test).build_enzymeml_json()
        print("Error Model Test")
        print(new_model)
    except VesselError as e:
        print("Error Model Test, excepotion called")
        print("error in vessels")



def testReaction_builder():
    model_template = json.loads(model)
    new_reaction = ReactionExtractor(model_template).extract_reaction_participants()
    print(new_reaction)

def test_request():
    
    req = requests.post("http://127.0.0.1:5000/create", json.dumps(test_enzymeML_builder()))
    
    #print("return request is", req.status_code)
    print("der content ist", req.content)
    if os.path.exists("./tests/enzml.omex"):
        os.remove("./tests/enzml.omex")
    f = open("./tests/enzml.omex", 'wb')
    f.write(req.content)
    f.close()