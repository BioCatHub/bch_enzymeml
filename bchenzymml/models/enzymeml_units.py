# TODO #11:

from pydantic import BaseModel
from typing import List, Optional, Dict


class UnitsDetails(BaseModel):
    name: str
    id: str
    meta_id: str
    units: Optional[List]
    ontology: str

    class Config:
        orm_mode = True


class UnitContainer(BaseModel):
    __root__: Dict[str, UnitsDetails]


class Unit(BaseModel):
    units: UnitContainer


class CustomUnitSpecifier(BaseModel):
    kind: str
    exponent: float
    scale: int
    multiplier: float

    class Config:
        orm_mode = True
