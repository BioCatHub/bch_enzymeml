from pydantic import BaseModel
from typing import List, Optional, Dict


class ZenodoMetadata(BaseModel):
    '''
        Class defining the metadata required to define the upload of EnzymeML documents to Zenodo
    
    '''
    title: str
    upload_type: str
    description: str
    creators: Optional[List]
    keywords:Optional[List]
    #doi: Optional[str]
