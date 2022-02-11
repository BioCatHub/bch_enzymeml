from pydantic import BaseModel
from typing import List, Optional, Dict


class ProteinDetail(BaseModel):
    name: str
    id: str
    vessel_id:str
    meta_id:str
    init_conc:float
    constant:bool
    boundary:bool
    unit:str
    ontology:str
    uri:str
    creator_id:str
    sequence:str
    ecnumber: str
    organism: str
    organism_tax_id: str
    uniprotid: str

    class Config:
        orm_mode = True


class ProteinContainer(BaseModel):
    __root__:Dict[str, ProteinDetail]

class Protein(BaseModel):
    proteins:ProteinContainer

