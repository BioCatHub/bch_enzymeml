from bchenzymml.models.enzymeml_measurement import ReplicatesDetails



class ReplicatesMapper:
    '''
        Maps the biocathub replicates to the enzymeml replicates dict.

        Attributes
        ----------

        Returns
        -------


    '''

    def __init__(self, bch_dict):
        self.bch_dict = bch_dict

    
    def extract_measurements(self): #TODO #28 This Method needs to be refactored

        try: 
            measurements = self.bch_dict["experimentalData"]["measurements"]
            return measurements
        
        except Exception as err:
            print("measurement Error")



    
    def extract_replicates(self, measurement):

        try: 

            measurement_enzymeml = {}            

            
            x_values = []

            y_values_length = len(measurement["replicates"][0]["y_values"])
            print(y_values_length)

            for j in measurement["replicates"]:
                x_values.append(j["x_value"])
            
            for y_len in range(y_values_length):
                y_values = []
                for repl in measurement["replicates"]:
                    y_values.append(repl["y_values"][y_len])
                measurement_enzymeml["y_values"+str(y_len)] = y_values

            measurement_enzymeml["x_values"] = x_values
            return measurement_enzymeml

        except Exception as e:
            print("extract Replicates")
            raise