import requests
import json

def test_request():
    files = {"omex_archieve":open("tests/enzml.omex", "rb")}

    req = requests.post("http://127.0.0.1:5000/read", files=files)
    
    print(req.text)