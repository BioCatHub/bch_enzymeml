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
    units:dict
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


class CreatorContainer(BaseModel):
    __root__: Dict[str, CreatorDetail]

class Creator(BaseModel):
    creator: CreatorContainer


creatordetail1 = CreatorDetail.from_orm(Creatorcls("Jan", "jansen", "sdads", "asddsa"))
creator1container = CreatorContainer(__root__={"creator_1": creatordetail1})
creator1 = Creator(creator=creator1container)



