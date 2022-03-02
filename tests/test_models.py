import requests
import json

from bchenzymml.models.enzymeml_model_generals_creator import Generals, CreatorDetail, CreatorContainer, Creator
from bchenzymml.models.enzymeml_vessel import VesselDetail, VesselContainer, Vessel 
from bchenzymml.models.enzymeml_protein import ProteinDetail, ProteinContainer, Protein
from bchenzymml.models.enzymeml_reactants import ReactantsDetail, ReactantsContainer, Reactant
from bchenzymml.models.enzymeml_reactions import ReactionDetail, ReactionContainer, Reaction, ReagentDetail
from bchenzymml.models.enzymeml_units import UnitsDetails, UnitContainer, Unit, CustomUnitSpecifier


from bchenzymml.models.enzymeml_classes import Generalscls, Creatorcls, Vesselcls, Proteincls, Reactantcls, Reactioncls, ReagentDetailscls, Reactioncls, ReagentDetailscls,UnitDetailscls, CustomUnitcls 

from bchenzymml.write_read_enzymeml.write_enzymeml.unit_builder import UnitBuilder

def test_creator():
    creator_details = CreatorDetail.from_orm(Creatorcls("Jan", "jansen", "sdads", "asddsa"))
    creator_cont = CreatorContainer(__root__={"creator1":creator_details})
    creator1 = Creator(creator=creator_cont)
    # print(creator1.dict)

def test_vessel():
    vessel_details = VesselDetail.from_orm(Vesselcls("eppi", 1, "mL", True, "v1", "asd", "sffdfd", "dsffd"))
    vessel_container = VesselContainer(__root__={"vessel1":vessel_details})
    vessel = Vessel(vessel=vessel_container)
    #print(vessel.dict())
    return vessel_container


def test_protein():
    protein_details = ProteinDetail.from_orm(Proteincls("ahas", "21", "asd", "adsd", 0, True, False, "mmol/L", "fdsfdd", "fdsffsd", 
                                                        "dsfdfsd", "ASDF", "asdsdda", "e.coli", "awdwada", "dffdsdf"))
    protein_container = ProteinContainer(__root__={"protein_1":protein_details})
    protein = Protein(proteins=protein_container)
    #print(protein.dict())


def test_reactants():
    
    reactantdetails = ReactantsDetail.from_orm(Reactantcls("acetaldehyde", "sfdfds", "sfdg", "sdfsf", 0, False, False, "mmol/L", "dsfd", "fdfs", "sdfds", "fds", "sdfdsf", "sefsef"))
    reactant_container = ReactantsContainer(__root__={"reactant1":reactantdetails})
    reactant = Reactant(reactants = reactant_container )
    #print(reactant.dict())


def test_reactions():
    educts = test_reagents()
    reaction_details = ReactionDetail.from_orm(Reactioncls("decarboxaltion", True, 37, "°C", 5, "dfdsffds", "reac1", "meta_reac_1", "www.www.", "creator_1", {}, educts, [], []))
    #print(reaction_details.dict())
    reaction_container = ReactionContainer(__root__={"protein_1":reaction_details})
    reaction = Reaction(reactions=reaction_container)
    print("The reaction is:", reaction.dict())

def test_reagents():
    reagent_details= ReagentDetail.from_orm(ReagentDetailscls("name", 1, True, "fdsef"))
    reagent_list = []
    reagent_list.append(reagent_details)
    return reagent_list


'''
def test_unit():
    emtpy_list = []
    emtpy_list.append(CustomUnitSpecifier.from_orm(CustomUnitcls("litre", -3, 0, 0)))
    unit_details = UnitsDetails.from_orm(UnitDetailscls("mL", "u0", "meta_u0", emtpy_list, "SBO:0000"))
    unit_container = UnitContainer(__root__={"ml":unit_details})
    units = Unit(units=unit_container)
    print("Der unit container", unit_container.__root__)
    return unit_container.__root__
'''


def test_unit():
    emtpy_list = []
    emtpy_list.append(CustomUnitSpecifier.from_orm(CustomUnitcls("litre", -3, 0, 0)))
    unit_details = UnitsDetails.from_orm(UnitDetailscls("mL", "u0", "meta_u0", emtpy_list, "SBO:0000"))
    unit_container = UnitContainer(__root__={"mL":unit_details})
    units = Unit(units=unit_container)
    return unit_container.__root__

'''
def test_unit():
    #unit = UnitBuilder().build_ml()
    all_units = UnitBuilder().build_units()
    #print("Alle Units sind", all_units)
    #print("die unt ist", unit)
    return all_units
'''


def test_generals():

    vessels_general = test_vessel()
    units = test_unit()
    
    v = vessels_general.__root__
    generals = Generals.from_orm(Generalscls("decarboxylation", "23232", "www.example.com", "doi:10.101012323","10.01.2022", "11.01.2022", v))
        
    
    test_dict = generals.dict()
    print("Das gesamte Konstrukt ist", test_dict)

    assert type(test_dict) == dict
    return test_dict


def test_request():
    
    req = requests.post("https://enzymeml.sloppy.zone/create", json.dumps(test_generals()))
    print("return request is", req.status_code)
    print("der content ist", req.content)
    f = open("./tests/enzml.omex", 'wb')
    f.write(req.content)
    f.close()
