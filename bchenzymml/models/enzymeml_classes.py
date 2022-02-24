
class Generalscls:
    def __init__(self,
                 name: str,
                 pubmedid: str,
                 url: str,
                 doi: str,
                 created: str,
                 modified: str,
                 vessels: dict,
                 units: dict):

        self.name = name
        self.pubmedid = pubmedid
        self.url = url
        self.doi = doi
        self.created = created
        self.modified = modified
        self.vessels = vessels
        self.units = units


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
                 meta_id: str,
                 uri: str,
                 creator_id: str,
                 ):
        self.name = name
        self.volume = volume
        self.unit = unit
        self.constant = constant
        self.id = id
        self.meta_id = meta_id
        self.uri = uri
        self.creator_id = creator_id


class Proteincls:
    def __init__(self,
                 name: str,
                 id: str,
                 vessel_id: str,
                 meta_id: str,
                 init_conc: float,
                 constant: bool,
                 boundary: bool,
                 unit: str,
                 ontology: str,
                 uri: str,
                 creator_id: str,
                 sequence: str,
                 ecnumber: str,
                 organism: str,
                 organism_tax_id: str,
                 uniprotid: str,
                 ):

        self.name = name
        self.id = id
        self.vessel_id = vessel_id
        self.meta_id = meta_id
        self.init_conc = init_conc
        self.constant = constant
        self.boundary = boundary
        self.unit = unit
        self.ontology = ontology
        self.uri = uri
        self.creator_id = creator_id
        self.sequence = sequence
        self.ecnumber = ecnumber
        self.organism = organism
        self.organism_tax_id = organism_tax_id
        self.uniprotid = uniprotid


class Reactantcls:
    def __init__(self,
                 name: str,
                 id: str,
                 vessel_id: str,
                 meta_id: str,
                 init_conc: float,
                 constant: bool,
                 boundary: bool,
                 unit: str,
                 ontology: str,
                 uri: str,
                 creator_id: str,
                 smiles: str,
                 inchi: str,
                 chebi_id: str):

        self.name = name
        self.id = id
        self.vessel_id = vessel_id
        self.meta_id = meta_id
        self.init_conc = init_conc
        self.constant = constant
        self.boundary = boundary
        self.unit = unit
        self.ontology = ontology
        self.uri = uri
        self.creator_id = creator_id
        self.smiles = smiles
        self.inchi = inchi
        self.chebi_id = chebi_id


class Reactioncls:
    def __init__(self,
                 name: str,
                 reversible: bool,
                 temperature: float,
                 temperature_unit: str,
                 ph: float,
                 ontology: str,
                 id: str,
                 meta_id: str,
                 uri: str,
                 creator_id: str,
                 model: dict,
                 educts: list,
                 products: list,
                 modifiers: list
                 ):

        self.name = name
        self.reversible = reversible
        self.temperature = temperature
        self.temperature_unit = temperature_unit
        self.ph = ph
        self.ontology = ontology
        self.id = id
        self.meta_id = meta_id
        self.uri = uri
        self.creator_id = creator_id
        self.model = model
        self.educts = educts
        self.products = products
        self.modifiers = modifiers


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


class UnitDetailscls:
    def __init__(self,
				name,
				id,
				meta_id,
				units,
				ontology,
				):
        self.name = name
        self.id = id
        self.meta_id = meta_id
        self.units = units
        self.ontology = ontology


class CustomUnitcls:
    def __init__(self,
                 kind,
                 exponent,
                 scale,
                 multiplier):
        self.kind = kind
        self.exponent = exponent
        self.scale = scale
        self.multiplier = multiplier
