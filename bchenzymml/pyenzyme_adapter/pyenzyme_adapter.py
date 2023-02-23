import requests
import json
import os
import zipfile
from io import BytesIO


from assets.configurations import Configurations

class PyenzmeAdapter:
    '''
        Adapter which connects to the Pyenzyme REST-API
    '''

    def __init__(self, enzymeml_model):
        self.enzymeml_model = enzymeml_model
        self.config = Configurations.get_configuarations()


    def send_to_pyenzyme_create(self):
        
        try:
            try: 
                req = requests.post("https://enzymeml.sloppy.zone/create", json.dumps(self.enzymeml_model))
            except Exception as err:
                print("REST API call did not work", err)
                raise
            print("Läuft")
            try:
                enzml_buffer = BytesIO(req.content)
                with open("assets/container.zip", "wb") as zip:
                    zip.write(enzml_buffer.getbuffer())   
                os.mkdir("assets/enzymemlContainer")
            
                with zipfile.ZipFile("assets/container.zip", "r") as zip:
                    zip.extractall("assets/enzymemlContainer") 
                
                #if os.path.exists(self.config["enzymeml"]["path_incoming_pyenzyme"]):
                    #os.remove(self.config["enzymeml"]["path_incoming_pyenzyme"])
            except Exception as err:
                print("deleting folder failed")
                err
                raise
            '''
            try:
                f = open(self.config["enzymeml"]["path_incoming_pyenzyme"], 'wb')
                f.write(req.content)
                f.close()
            except Exception as err:
                print("file cannot be written!")
                print(err)
                raise
            '''
        except Exception as e:
            print("Error in Adapter", e)
            raise

    def send_to_pyenzyme_read(self, file):
            try: 
                files = {"omex_archive":open("assets/Model_4.omex", "rb")}
                req = requests.post("https://enzymeml.sloppy.zone/read", files=files)
                return req
            except Exception as err:
                print("REST API call EnzymeML read did not work", err)
                raise



            