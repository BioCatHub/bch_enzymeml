class Configurations:

    def get_configuarations():
        config = {
            "CORS":{r'/*':{'origins':'*'}},
            "PORT":8000,
            "DEBUG":False,
            "enzymeml":
            {
                "path_incoming_pyenzyme":"assets/NewEnzymeML.omex",
                "path_updated_by_biocathub_model":"assets/NewEnzymeML!.omex",
                "path_without_enzml":"assets/withoutenzml.omex",
                "biocathub_paht_in_omex_archive":"biocathub.json",
                "biocathub_model_path_local":"assets/biocathub.json",
            },

            "zenodo":{
                "filename":"Experiment.omex"
            }
                }
        return config
        