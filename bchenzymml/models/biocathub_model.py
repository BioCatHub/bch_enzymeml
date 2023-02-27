# TODO #3

from pydantic import BaseModel
from typing import List, Optional, Dict


# This definition is highly unfinished!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class BioCatHubModel(BaseModel):
    title: Optional[str]
    descrioption:Optional[str]
    enzymes:Optional[List]
    vessel:Optional[dict]
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
    others:Optional[List]


class Buffer(BaseModel):
    type:Optional[str]
    concentration:Optional[float]
    unit:Optional[str]


class Condition(BaseModel):
    ph:Optional[str]
    temp:Optional[float]
    unit:Optional[str]
    buffer:Optional[Buffer]
    others:Optional[List]









