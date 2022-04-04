from pydantic import BaseModel
from typing import List, Optional, Dict




class ReactantsDetail(BaseModel): 
    name: str
    id: str
    vessel_id: str
    meta_id: str
    init_conc: float
    #constant: bool
    #boundary: bool
    unit: str
    #ontology:str
    #uri: str
    #creator_id: str
    smiles: str
    #inchi: str
    #chebi_id:str

    class Config:
        orm_mode = True

