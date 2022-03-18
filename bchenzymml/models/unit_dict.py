
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
        return unit_dict
    
    def check_unit(self, unit):
        unit_dict = self.unit_selector()

        try:
            
            if unit in unit_dict:
                return unit_dict[unit]
            
            else:
                return "no Unit"
        
        except Exception as e:
            return "no Unit Error"

        