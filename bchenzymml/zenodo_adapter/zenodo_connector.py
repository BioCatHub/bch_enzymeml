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
        self.file = file #TODO #15
    
    
    def get_all_entries(self):
        ''' 
            This Method returns all depositions available in the respective Zenodo Account

            args
            ----
            None

            returns
            -------
            payload: List; List containing entries in the Zenodo account

        '''
        r = requests.get(self.url,
                        params=self.token)
        return r.json()

    def create_empty_deposit(self):
        r = requests.post(self.url,
                            params=self.token,
                            json={})
    
    def create_new_deposition(self,data, headers):

        '''
            This method creates an empty deposition in Zenodo and adds nessecary metadata via the data object

            args
            ----
                params:dict; dictionary containing the access token required to communicate with the Zenodo REST-API it based on the model, example {'access-token':<ZenodoAccessToken>}
                headers:dict; dictionary which contains general information about the HTTP request to Zenodo. In this case it only contains information about the content; example: headers = {"Content-Type": "application/json"}
                data: dict; dict containing the metadatata required to describe an experiment in Zenodo. Documentation see here: https://developers.zenodo.org/#representation

            returns
                response:dict; responst Object from Zenodo API Call
            -------

        '''
        r = requests.post(self.url,
                        params=self.token,
                        headers=headers,
                        data = json.dumps(data),
                        )
        response = r.json()     
        return response["id"] 

    def upload_enzymeml(self, data, headers):
        '''
            Uploads a new EnzymeML document to Zenodo. Therefore this method has two steps:
                1. It creates a new Deposition by calling the create_new_deposition method in Zenodo and adds metadata about the experiment in the EnzymeML document
                2. It uploads a given EnzymeML document as bytesting to the Zenodo Deposition

            args
            ----
                data: dict; dict containing the metadatata required to describe an experiment in Zenodo. Documentation see here: https://developers.zenodo.org/#representation
                headers: dict; dictionary which contains general information about the HTTP request to Zenodo. In this case it only contains information about the content; example: headers = {"Content-Type": "application/json"}
            
            returns
            -------
                response:dict; responst Object from Zenodo API Call
        '''


        id = self.create_new_deposition(data_test, headers)
        r = requests.post(self.url+"/{}/files?access_token={}".format(id, self.token["access_token"]),
                            files=self.file)
        return r.json()






    
    def get_individual_entry(self, id):
        r = requests.get("https://sandbox.zenodo.org/api/deposit/depositions/1023538/files", params=self.token)
        enzml = self.download_enzymeml_from_zenodo('https://sandbox.zenodo.org/api/files/e865a98e-6f82-445a-aaf2-14304547f033/2021-5-4ExperimentN.omex')
        new_file = open("NewEnzymeML.omex", "wb")
        new_file.write(enzml)
        new_file.close()
        #return enzml

    
    def download_enzymeml_from_zenodo(self, download_url):
        r = requests.get(download_url, params=self.token)
        print(r.content)        
        return r.content



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
    
test_file = "NewEnzymeML.omex"
upl_file = {"file":open(test_file, 'rb')}
headers = {"Content-Type": "application/json"}

data_obj={"metadata":{"upload_type":"dataset",
            "title":"Super_title"}}


connector = ZenodoConnector(url, token, upl_file)
connector.upload_enzymeml(data_test, headers)

#data_sets = connector.get_all_entries()
#for i in data_sets:
#    print(i)

data_set = connector.get_individual_entry("222")
print(data_set)



name ="Jürgen"
age = "22"
new = "my name is {}/{}".format(name, age) 
print(new)


    
