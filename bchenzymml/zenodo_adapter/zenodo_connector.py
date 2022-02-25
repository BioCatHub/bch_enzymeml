import requests
import json

token = {'access_token': 'h2VjvzgwrHAFLrQR3L0OhlsYPI8YE6H7VVHlTKWXfyCexOcIH0h8cMzZAtBq'}
url = "https://sandbox.zenodo.org/api/deposit/depositions"


class ZenodoConnector:
    '''
        This class builds the direct connection to Zenodo. It can send request to write or read entries in Zenodo database

        ----------
        args: 
            url:string = Url of the Zenodo endpoint
            token: string = Token used to authenticate in Zenodo
            file:bytestring EnzymeML file to be uploaded to Zenodo
    '''
    def __init__(self, url, token, file):
        self.url = url
        self.token = token
        self.file = file
    
    def get_all_entries(self):
        r = requests.get(self.url,
                        params=self.token)
        print(r.content)

    def create_empty_deposit(self):
        r = requests.post(self.url,
                            params=self.token,
                            json={})
        print(r.json())
    
    def publish_enzymeml(self,data, headers):
        r = requests.post(self.url,
                        params=self.token,
                        headers=headers,
                        data = json.dumps(data),
                        )
        resp = r.json()     
        return resp["id"] 

    def publish_file(self):
        id = self.publish_enzymeml(data_test, headers)
        r = requests.post(self.url+"/{}/files?access_token={}".format(id, self.token["access_token"]),
                            files=self.file)
        #r.json()



data_test = {
    "metadata": {
        "title": "New EnzymeML!",
        "upload_type": "dataset",
        "description": "EnzymeML document",
        "creators": [
            {"name": "Doe, John", "affiliation": "Zenodo"}
        ],
        "keywords":["enzymes", "biocatalysis"],
        "doi":""
    }
}
    
test_file = 'bchenzymml/zenodo_adapter/enzml.omex'
upl_file = {"file":open(test_file, 'rb')}
headers = {"Content-Type": "application/json"}

data_obj={"metadata":{"upload_type":"dataset",
            "title":"Super_title"}}


connector = ZenodoConnector(url, token, upl_file)
connector.publish_file()


name ="Jürgen"
age = "22"
new = "my name is {}/{}".format(name, age) 
print(new)


    
