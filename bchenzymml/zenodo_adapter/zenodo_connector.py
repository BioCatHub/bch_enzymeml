import requests
import json

from assets.configurations import Configurations

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
    def __init__(self, file):
        self.file = file #TODO #15
        self.config = Configurations.get_configuarations()
    
    
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
        r = requests.get(url,
                        params=token)
        #print(r.json())
        return r.json()
    
    def extract_deposits_for_dashboard_table(self):
        '''
            receives all entries from the Zenodo repository and extracts metadata needed for the display in the BioCatHub dashboard table

            Args:
                None
            
            Returns:
                depositions (dict): A dictionary containing the Zenodo entries together with the needed metadata for the BioCatHub dashboard
            
        '''

        deposits = self.get_all_entries()
        depositions = []
        for element in deposits:
            metadata = element['metadata']
            creator = metadata['creators'][0]
            deposition = {
                'id': element['id'],
                'title': metadata['title'],
                'date': metadata['publication_date'],
                'name': creator['name'],
                'affiliation': creator['affiliation'],
                'link': element['links']['html']
            }
            depositions.append(deposition)
        return depositions


    def create_empty_deposit(self):
        r = requests.post(url,
                            params=token,
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
        r = requests.post(url,
                        params=token,
                        headers=headers,
                        data = json.dumps(data),
                        )
        response = r.json()
        return response["id"] 

    def upload_enzymeml(self, data, headers, file):
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

        print("Neues EnzmL !*********************************************")
        print("request was there")
        id = self.create_new_deposition(data, headers)

        r = requests.post(url+"/{}/files?access_token={}".format(id, token["access_token"]),
                            files=file)
        print("WAS ALS ANTWORT KOMMT", r.content)

        
        return r.json()






    
    def get_individual_entry(self, id):
        r = requests.get("https://sandbox.zenodo.org/api/deposit/depositions/{}/files".format(id), params=token)
        print("die depositoon is",r.json())
        res = r.json()
        print("response ist", res[0]["links"]['download'])
        filename = self.config["zenodo"]["filename"]

        #enzml = self.download_enzymeml_from_zenodo('https://sandbox.zenodo.org/api/files/{}/{}'.format(id, filename))
        print("method used is:", 'https://sandbox.zenodo.org/api/files/{}/{}'.format(id, filename))
        enzml = self.download_enzymeml_from_zenodo(res[0]["links"]['download'])
        #new_file = open(self.config["enzymeml"]["path_updated_by_biocathub_model"], "wb")
        #new_file.write(enzml)
        #new_file.close()
        return enzml

    
    def download_enzymeml_from_zenodo(self, download_url):
        r = requests.get(download_url, params=token)
        print("Status ist",r.status_code)        
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


#connector = ZenodoConnector(upl_file)
#connector.upload_enzymeml(data_test, headers, upl_file)

#data_sets = connector.get_all_entries()
#for i in data_sets:
#    print(i)

#data_set = connector.get_individual_entry("222")
#print(data_set)



#name ="Jürgen"
#age = "22"
#new = "my name is {}/{}".format(name, age) 
#print(new)


    
