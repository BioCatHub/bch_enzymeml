from pydantic import BaseModel
from typing import List, Optional, Dict




class VesselDetail(BaseModel):
    name:str
    volume:float
    unit:str
    constant: bool
    id: str
    #meta_id: str
    #uri: str
    #creator_id:str

    class Config:
            orm_mode = True


