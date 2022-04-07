from pydantic import BaseModel
from typing import List, Optional, Dict


# This definition is highly unfinished!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

class MeasurementDetail(BaseModel):
    name: str
    species_dict:dict

    class Config:
            orm_mode = True


class SpeciesMeasurementDetail(BaseModel):
    init_conc: float
    unit: str
    reactant_id:str
    replicates:List

    class Config:
        orm_mode = True


class ReplicatesDetails(BaseModel):
    id:str
    species_id:str
    data_unit:str
    time_unit:str
    time:List
    data:List

    class Config:
        orm_mode = True







class ReplicatesDetailscls:
    def __init__(self, id:str,
                species_id:str,
                data_unit:str,
                time_unit:str,
                time:List,
                data:List,
                ):
        self.id = id
        self.species_id = species_id
        self.data_unit = data_unit
        self.time_unit = time_unit
        self.time = time
        self.data = data


class SpeciesMeasurementDetailcls:
    def __init__(self,
                init_conc: float,
                unit: str,
                replicates:List,
                        ):
        self.init_conc = init_conc
        self.unit=unit
        self.replicates = replicates

class MeasurementDetailcls:
    def __init__(self, name, species_dict):
        self.name = name
        self.species_dict = species_dict


measurements = {
    "name":"pyruvate",
    "species":{
        "init_conc":0,
        "unit":"mmole/l",
        "replicates":{
            "id":"m0",
            "species_id":"s0",
            "data_unit":"mmole/l",
            "time_unit":"s",
            "time":[0,1,2,3,4],
            "data":[0,2,3,9,16]
        }
    }
}

'''

dr = measurements["species"]["replicates"]
sp = measurements["species"]


replicates_list = []
replicates = ReplicatesDetails.from_orm(ReplicatesDetailscls(dr["id"], dr["species_id"], dr["data_unit"], dr["time_unit"], dr["time"], dr["data"]))
replicates_list.append(replicates.dict())

species_specs = SpeciesMeasurementDetail.from_orm(SpeciesMeasurementDetailcls(sp["init_conc"], sp["unit"], replicates_list))

#print(species_specs)
species_conteiner = SpeciesMeasurementContainer(__root__={"species1":species_specs})
spec_conteiner_return = species_conteiner.__root__

#print("Der container ist", spec_conteiner_return)

measurement_object = MeasurementDetail.from_orm(MeasurementDetailcls(measurements["name"],spec_conteiner_return))
#print("Das gesamt Objekt ist",measurement_object)
#print("Das gesamt Dict ist",measurement_object.dict())

#print("Das Objekt ist: ", measurement_object)

#print("Das Dict ist: ", measurement_object.dict())


'''