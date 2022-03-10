import requests
import json

from io import BytesIO
import os

from bchenzymml.models.enzymeml_model_generals_creator import Generals, CreatorDetail, CreatorContainer, Creator
from bchenzymml.models.enzymeml_vessel import VesselDetail, VesselContainer, Vessel 
from bchenzymml.models.enzymeml_protein import ProteinDetail, ProteinContainer, Protein
from bchenzymml.models.enzymeml_reactants import ReactantsDetail, ReactantsContainer, Reactant
from bchenzymml.models.enzymeml_reactions import ReactionDetail, ReactionContainer, Reaction, ReagentDetail
from bchenzymml.models.enzymeml_units import UnitsDetails, UnitContainer, Unit, CustomUnitSpecifier
from bchenzymml.models.enzymeml_measurement import MeasurementDetail, MeasurementDetailContainer, SpeciesMeasurementDetail, SpeciesMeasurementContainer,  ReplicatesDetails, SpeciesDictContainer

from bchenzymml.models.enzymeml_classes import Generalscls, Creatorcls, Vesselcls, Proteincls, Reactantcls, Reactioncls, ReagentDetailscls, Reactioncls, ReagentDetailscls,UnitDetailscls, CustomUnitcls, ReplicatesDetailscls, SpeciesMeasurementDetailcls, MeasurementDetailcls

from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder

def test_creator():
    creator_details = CreatorDetail.from_orm(Creatorcls("Jan", "jansen", "sdads", "a1"))
    creator_cont = CreatorContainer(__root__={"creator1":creator_details})
    creator1 = Creator(creator=creator_cont)
    return creator_cont.__root__
    # print(creator1.dict)

def test_vessel():
    vessel_details = VesselDetail.from_orm(Vesselcls("eppi", 1, "ml", True, "v1", "asd", "sffdfd", "dsffd")) #TODO #17
    vessel_details_falcon = VesselDetail.from_orm(Vesselcls("falcon", 1, "ul", True, "v2", "asd", "sffdfd", "a1"))
    vessel_container = VesselContainer(__root__={"vessel1":vessel_details, "vessel2":vessel_details_falcon })
    vessel = Vessel(vessel=vessel_container)
    #print(vessel.dict())
    return vessel_container


def test_protein():
    protein_details = ProteinDetail.from_orm(Proteincls("ahas", "p0", "v1", "adsd", 0, True, False, "mmole/l", "SBO:0000176", "fdsffsd", 
                                                        "dsfdfsd", "ASDF", "1.1.1.1", "e.coli", "awdwada", "dffdsdf"))
    protein_container = ProteinContainer(__root__={"protein_1":protein_details})
    protein = Protein(proteins=protein_container)
    return protein_container.__root__
    #print(protein.dict())


def test_reactants():
    
    reactantdetails = ReactantsDetail.from_orm(Reactantcls("acetaldehyde", "s1", "sfdg", "sdfsf", 0, False, False, "mgram/ml", "SBO:0000377", "fdfs", "sdfds", "fds", "sdfdsf", "sefsef"))
    reactant_container = ReactantsContainer(__root__={"reactant1":reactantdetails})
    reactant = Reactant(reactants = reactant_container )
    return reactant_container.__root__
    
    #print(reactant.dict())


def test_reactions():
    educts = test_reagents()
    reaction_details = ReactionDetail.from_orm(Reactioncls("decarboxaltion", True, 37, "Celsius", 5, "SBO:0000176", "r1", "meta_r1", "www.www.", "creator_1", educts, [], []))
    #print(reaction_details.dict())
    reaction_container = ReactionContainer(__root__={"protein_1":reaction_details})
    reaction = Reaction(reactions=reaction_container)
    return reaction_container.__root__

def test_reagents():
    reagent_details= ReagentDetail.from_orm(ReagentDetailscls("name", 1, True, "SBO:0000176"))
    reagent_list = []
    reagent_list.append(reagent_details)
    return reagent_list


def test_unit():
    all_units = UnitBuilder().build_units()
    return all_units


def test_measurements():
    measurements = {
    "name":"pyruvate",
    "species":{
        "init_conc":0,
        "unit":"mmole/l",
        "replicates":{
            "id":"m0",
            "species_id":"s1",
            "data_unit":"mmole/l",
            "time_unit":"s",
            "time":[0,1,2,3,4],
            "data":[0,2,3,9,16]
            }
        }
    }

    dr = measurements["species"]["replicates"]
    sp = measurements["species"]


    replicates_list = []
    replicates = ReplicatesDetails.from_orm(ReplicatesDetailscls(dr["id"], dr["species_id"], dr["data_unit"], dr["time_unit"], dr["time"], dr["data"]))
    replicates_list.append(replicates.dict())

    species_specs = SpeciesMeasurementDetail.from_orm(SpeciesMeasurementDetailcls(sp["init_conc"], sp["unit"], "s1", replicates_list))
    species_conteiner = SpeciesMeasurementContainer(__root__={"species1":species_specs.dict()})
    spec_conteiner_return = species_conteiner.__root__
    spec_dict_container = SpeciesDictContainer(__root__={"reactants":spec_conteiner_return, "proteins":{}})

    measurement_object = MeasurementDetail.from_orm(MeasurementDetailcls(measurements["name"],spec_dict_container.__root__))
    measurement_container = MeasurementDetailContainer(__root__={"measurement1":measurement_object.dict()})
    print("meauremnt container", measurement_container.__root__)
    return measurement_container.__root__


def test_generals():

    vessels_general = test_vessel()
    units = test_unit()
    creator = test_creator()
    proteins = test_protein()
    reactants = test_reactants()
    reactions = test_reactions()
    measurments = test_measurements()
    print("die measurment sind:", measurments)
    filename = "./assets/biocathub.json"

    file = open("./assets/biocathub.json", "rb")
    print("Die atei ist:", file.read1())


    files = {"file":{"hallo":"ddd"}}
    file.close()

    #print("Die Reaktion ist:", reactions)
    
    v = vessels_general.__root__
    generals = Generals.from_orm(Generalscls("decarboxylation", "23232", "www.example.com", "doi:10.101012323","10.01.2022", 
                                            "11.01.2022", v, units,creator, proteins, reactants, reactions, measurments, files))
        
    
    test_dict = generals.dict()
    #print("Das gesamte Konstrukt ist", test_dict)

    assert type(test_dict) == dict
    return test_dict


def test_request():
    
    req = requests.post("http://127.0.0.1:5000/create", json.dumps(test_generals()))
    
    print("gesendet wird:", test_generals())
    print("return request is", req.status_code)
    print("der content ist", req.content)
    if os.path.exists("./tests/enzml.omex"):
        os.remove("./tests/enzml.omex")
    f = open("./tests/enzml.omex", 'wb')
    f.write(req.content)
    f.close()
