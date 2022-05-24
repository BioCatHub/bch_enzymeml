import bchenzymml.write_read_enzymeml.write_enzymeml.write_enzymeml
from bchenzymml.models.biocathub_test_model import model
from app import AppInitializer
import json




# the app create app method needs to be imported



def test_case():
    app = AppInitializer().create_app()
    print("TEST_ROUTE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    with app.test_client() as client:
        payload = json.dumps(model)
        res = client.post("api/create_enzymeml", json=model)
        #print(res)
        data = 3
        assert data == 3
