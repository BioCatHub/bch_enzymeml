from pydantic import BaseModel
from typing import List, Optional, Dict


class ReactionDetail(BaseModel):
    name: str
    reversible: bool
    temperature: float
    temperature_unit: str
    ph: float
    ontology:str
    id:str
    meta_id:str
    uri:str
    creator_id:str
    model:Optional[dict]
    educts:Optional[List]
    products:Optional[List]
    modifiers:Optional[List]

    class Config:
            orm_mode = True

class ReactionContainer(BaseModel):
    class CreatorContainer(BaseModel):
        __root__: Dict[str, ReactionDetail]

class Reaction(BaseModel):
    reactions:ReactionContainer


class ReagentDetail(BaseModel):
    species_id: str
    stoichiometry: float
    constant: bool
    ontology: str


