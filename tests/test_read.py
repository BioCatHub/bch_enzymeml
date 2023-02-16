import requests
import json



def test_request():
    files = {"omex_archive":open("tests/Model_4.omex", "rb")}

    #req = requests.post("http://127.0.0.1:5000/read", files=files) https://enzymeml.sloppy.zone/create
    req = requests.post("https://enzymeml.sloppy.zone/read", files=files) 
    
    print("RESULT",req)
    print("RESULT",req.text)

