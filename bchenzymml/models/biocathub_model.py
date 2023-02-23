# TODO #3

from pydantic import BaseModel
from typing import List, Optional, Dict


# This definition is highly unfinished!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class BioCatHubModel(BaseModel):
    title: Optional[str]
    descrioption:Optional[str]
    enzymes:Optional[List]
    vessels:Optional[dict]
    condition:Optional[dict]
    experimentalData:Optional[dict]
    user:Optional[dict]


class User(BaseModel):
    email: Optional[str]
    firstName:Optional[str]
    institution:Optional[str]
    lastName:Optional[str]


class Vessel(BaseModel):
    type: Optional[str]
    unit: Optional[str]
    volume:Optional[float]




