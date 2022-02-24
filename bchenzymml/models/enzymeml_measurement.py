from pydantic import BaseModel
from typing import List, Optional, Dict


# This definition is highly unfinished!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class MeasurementDetail(BaseModel):
    name: str
    temperature: float
    temperature_unit: str
    ph: str
    species_dict:dict

    class Config:
            orm_mode = True