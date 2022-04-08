from typing import List, Optional, Dict



class Generalscls:
    def __init__(self,
                 name: str,
                 pubmedid: str,
                 url: str,
                 doi: str,
                 created: str,
                 modified: str,
                 vessels: dict,
                 creators:dict,
                 proteins:dict,
                 reactants:dict,
                 reactions:dict,
                 measurements:dict,
                 files:dict
                  ):

        self.name = name
        self.pubmedid = pubmedid
        self.url = url
        self.doi = doi
        self.created = created
        self.modified = modified
        self.vessels = vessels
        self.creators=creators
        self.proteins = proteins
        self.reactants = reactants
        self.reactions = reactions
        self.measurements = measurements
        self.files = files


class Creatorcls:
    def __init__(self, given_name: str,
                 family_name: str,
                 mail: str,
                 id: str):

        self.given_name = given_name
        self.family_name = family_name
        self.mail = mail
        self.id = id


class Vesselcls:
    def __init__(self,
                 name: str,
                 volume: float,
                 unit: str,
                 constant: bool,
                 id: str,
                 #meta_id: str,
                 #uri: str,
                 #creator_id: str,
                 ):
        self.name = name
        self.volume = volume
        self.unit = unit
        self.constant = constant
        self.id = id
        #self.meta_id = meta_id
        #self.uri = uri
        #self.creator_id = creator_id
        


class Proteincls:
    def __init__(self,
                 name: str,
                 id: str,
                 vessel_id: str,
                 meta_id: str,
                 init_conc: float,
                 constant: bool,
                 #boundary: bool,
                 unit: str,
                 ontology: str,
                 #uri: str,
                 #creator_id: str,
                 sequence: str,
                 ecnumber: str,
                 #organism: str,
                 #organism_tax_id: str,
                 #uniprotid: str,
                 ):

        self.name = name
        self.id = id
        self.vessel_id = vessel_id
        self.meta_id = meta_id
        self.init_conc = init_conc
        self.constant = constant
        #self.boundary = boundary
        self.unit = unit
        self.ontology = ontology
        #self.uri = uri
        #self.creator_id = creator_id
        self.sequence = sequence
        self.ecnumber = ecnumber
        #self.organism = organism
        #self.organism_tax_id = organism_tax_id
        #self.uniprotid = uniprotid


class Reactantcls:
    def __init__(self,
                 name: str,
                 id: str,
                 vessel_id: str,
                 meta_id: str,
                 init_conc: float,
                 #constant: bool,
                 #boundary: bool,
                 unit: str,
                 #ontology: str,
                 #uri: str,
                 #creator_id: str,
                 smiles: str,
                 #inchi: str,
                 #chebi_id: str
                ):

        self.name = name
        self.id = id
        self.vessel_id = vessel_id
        self.meta_id = meta_id
        self.init_conc = init_conc
        #self.constant = constant
        #self.boundary = boundary
        self.unit = unit
        #self.ontology = ontology
        #self.uri = uri
        #self.creator_id = creator_id
        self.smiles = smiles
        #self.inchi = inchi
        #self.chebi_id = chebi_id


class Reactioncls:
    def __init__(self,
                name: str,
                reversible: bool,
                temperature: float,
                temperature_unit: str,
                ph: float,
                #ontology: str,
                id: str,
                meta_id: str,
                #uri: str,
                #creator_id: str,
                #model: dict,
                educts: list,
                products: list,
                #modifiers: list
                ):

        self.name = name
        self.reversible = reversible
        self.temperature = temperature
        self.temperature_unit = temperature_unit
        self.ph = ph
        #self.ontology = ontology
        self.id = id
        self.meta_id = meta_id
        #self.uri = uri
        #self.creator_id = creator_id
        #self.model = model
        self.educts = educts
        self.products = products
        #self.modifiers = modifiers


class ReagentDetailscls:
    def __init__(self,
                 species_id: str,
                 stoichiometry: float,
                 constant: bool,
                 ontology: str):

        self.species_id = species_id
        self.stoichiometry = stoichiometry
        self.constant = constant
        self.ontology = ontology


class ReplicatesDetailscls:
    def __init__(self, id:str,
                species_id:str,
                data_unit:str,
                time_unit:str,
                time:List,
                data:List,
                ):
        self.id = id
        self.species_id = species_id
        self.data_unit = data_unit
        self.time_unit = time_unit
        self.time = time
        self.data = data


class SpeciesMeasurementDetailcls:
    def __init__(self,
                init_conc: float,
                unit: str,
                reactant_id:str,
                replicates:List,
                        ):
        self.init_conc = init_conc
        self.unit=unit
        self.reactant_id = reactant_id
        self.replicates = replicates

class MeasurementDetailcls:
    def __init__(self, name, id, species_dict):
        self.name = name
        self.id = id
        self.species_dict = species_dict
