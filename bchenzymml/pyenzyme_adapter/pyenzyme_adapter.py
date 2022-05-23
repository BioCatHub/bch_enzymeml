import requests
import json
import os


class PyenzmeAdapter:
    '''
        Adapter which connects to the Pyenzyme REST-API
    '''

    def __init__(self, enzymeml_model):
        self.enzymeml_model = enzymeml_model


    def send_to_pyenzyme_create(self):
        
        try:
            req = requests.post("http://127.0.0.1:8000/create", json.dumps(self.enzymeml_model))
            if os.path.exists("assets/BioCatHub_enzml.omex"):
                os.remove("assets\BioCatHub_enzml.omex")
            f = open("assets\BioCatHub_enzml.omex", 'wb')
            f.write(req.content)
            f.close()
        except Exception as e:
            print("Error in Adapter", e)
            raise

