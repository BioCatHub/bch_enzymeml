# TODO #4

from pydantic import BaseModel
from typing import List, Optional, Dict

class Generals(BaseModel):

    name:str
    level = 3
    version = "2"
    pubmedid: Optional[str]
    url: Optional[str]
    doi: str
    created: str
    modified: str
    vessels:dict
    creators:Optional[dict]
    proteins:Optional[dict]
    reactants:Optional[dict]
    reactions:Optional[dict]
    measurements:Optional[dict]
    files:Optional[dict]

    class Config:
            orm_mode = True


class CreatorDetail(BaseModel):
    given_name: str
    family_name: str
    mail: str
    id:str
    class Config:
            orm_mode = True

class Creatorcls:
    def __init__(self, given_name: str,
                        family_name: str,
                        mail: str,
                        id:str):
                        
        self.given_name = given_name
        self.family_name = family_name
        self.mail = mail
        self.id = id




