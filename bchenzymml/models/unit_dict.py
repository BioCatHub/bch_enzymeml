
class UnitBase:
    '''
        class which stores the enzymeml and biocathub units
    '''

    def unit_selector(self):

                
        unit_dict = {}
        unit_dict["mL"] = "ml"
        unit_dict["mol"] = "mole"
        unit_dict["mmol"] = "mmole"
        unit_dict["mmoL/L"] = "mmole/l"
        unit_dict["L"] = "litre"
        unit_dict["mL"] = "mlitre"
        unit_dict["mg/mL"] = "mgram/mlitre"
        unit_dict["°C"] = "C"
        return unit_dict
    
    def check_unit(self, unit):
        unit_dict = self.unit_selector()

        try:
            
            if unit in unit_dict:
                return unit_dict[unit]
            
            else:
                return "dimensionless"
        
        except Exception as e:
            return "no Unit Error"

        