from bchenzymml.models.enzymeml_model_generals_creator import Generals, CreatorDetail, CreatorContainer, Creator
from bchenzymml.models.enzymeml_vessel import VesselDetail, VesselContainer, Vessel 
from bchenzymml.models.enzymeml_protein import ProteinDetail, ProteinContainer, Protein
from bchenzymml.models.enzymeml_reactants import ReactantsDetail, ReactantsContainer, Reactant
from bchenzymml.models.enzymeml_reactions import ReactionDetail, ReactionContainer, Reaction, ReagentDetail


from bchenzymml.models.enzymeml_classes import Generalscls, Creatorcls, Vesselcls, Proteincls, Reactantcls, Reactioncls, ReagentDetailscls, Reactioncls, ReagentDetailscls





def test_creator():
    creator_details = CreatorDetail.from_orm(Creatorcls("Jan", "jansen", "sdads", "asddsa"))
    creator_cont = CreatorContainer(__root__={"creator1":creator_details})
    creator1 = Creator(creator=creator_cont)
    print(creator1.dict)

def test_vessel():
    vessel_details = VesselDetail.from_orm(Vesselcls("eppi", 1, "mL", True, "wee", "asd", "sffdfd", "dsffd"))
    vessel_container = VesselContainer(__root__={"vessel1":vessel_details})
    vessel = Vessel(vessel=vessel_container)
    print(vessel.dict())
    return vessel_container


def test_protein():
    protein_details = ProteinDetail.from_orm(Proteincls("ahas", "21", "asd", "adsd", 0, True, False, "mmol/L", "fdsfdd", "fdsffsd", 
                                                        "dsfdfsd", "ASDF", "asdsdda", "e.coli", "awdwada", "dffdsdf"))
    protein_container = ProteinContainer(__root__={"protein_1":protein_details})
    protein = Protein(proteins=protein_container)
    print(protein.dict())


def test_reactants():
    
    reactantdetails = ReactantsDetail.from_orm(Reactantcls("acetaldehyde", "sfdfds", "sfdg", "sdfsf", 0, False, False, "mmol/L", "dsfd", "fdfs", "sdfds", "fds", "sdfdsf", "sefsef"))
    reactant_container = ReactantsContainer(__root__={"reactant1":reactantdetails})
    reactant = Reactant(reactants = reactant_container )


def test_reactions():
    reaction_details = ReactionDetail.from_orm(Reactioncls("decarboxaltion", True, 37, "°C", 5, "dfdsffds", "reac1", "meta_reac_1", "www.www.", "creator_1", {},[],[],[]))
    reaction_container = ReactionContainer(__root__={"reaction_1":reaction_details})
    reaction = Reaction(reactions=reaction_container)
    print(reaction.dict())






def test_generals():

    vessels_general = test_vessel()
    v = vessels_general.__root__
    generals = Generals.from_orm(Generalscls("decarboxylation", "awdawd", "adsd", "sadasd", "dfdds", "fesfsf", v))
        
    
    test_dict = generals.dict()
    print(test_dict)

    assert type(test_dict) == dict