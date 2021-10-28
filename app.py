from flask import Flask
from flask_restx import Api, Resource
from flask_cors import CORS

# Hier werden Python eigenen Libraries importiert
from assets.configurations import Configurations
# Selbst definierten Packages importiert

class AppInitializer():
    '''
    Intatiates the app and api classes required to run the REST-API

    Params:
        none

    This class is essential, because: 
    - it instatiates the app required for the webserver to work
    - it instatiates the api required for REST-API functionalities and the Swagger documentation
    - it sets the CORS 
    - it adds the namespaces to the api object
    '''

    def create_app(self):
        '''
        initiates the app, api and CORS object for the REST-Api
        Params:
            none
        Returns:
            app(Object): Central object and entrypoint for the REST-API
        '''
        app = Flask(__name__)
        api = Api(app)
        config = Configurations.get_configuarations()
        CORS(app, resources=config["CORS"])
        return app
    

if __name__ == '__main__':
    Newapp = AppInitializer
    app = Newapp.create_app()
    app.run()
    

