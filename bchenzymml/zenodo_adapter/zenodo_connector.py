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
    '''
    def __init__(self, url, token):
        self.url = url
        self.token = token
    
    def get_all_entries(self):
        r = requests.get(self.url,
                        params=self.token)
        print(r.content)

    def create_empty_deposit(self):
        r = requests.post(self.url,
                            params=self.token,
                            json={})
        print(r.json())
    
    def publish_enzymeml(self, file, data, headers):
        r = requests.post(self.url,
                        params=self.token,
                        headers=headers,
                        data = json.dumps(data),
                        #files=file,
                        )
        print(r.json())

    def publish_file(self, file):
        r = requests.post(self.url+"/1022337/files?access_token=h2VjvzgwrHAFLrQR3L0OhlsYPI8YE6H7VVHlTKWXfyCexOcIH0h8cMzZAtBq",
                            files=file)
        #r.json()



data_test = {
    "metadata": {
        "title": "New_upload!",
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


connector = ZenodoConnector(url, token)
#connector.get_all_entries()
#connector.create_empty_deposit()
connector.publish_enzymeml(upl_file, data_test, headers)
#connector.publish_file(upl_file)


    
