from bchenzymml.models.unit_dict import UnitBase


'''
    Converts the Units used in BioCatHub to the Units used in EnzymeML

'''

class UnitBuilder:
    '''
        Converts the units from BioCatHub to Units used in EnzymeML
        
        Attributes
        ----------
        Methods
        -------
            convert_from_bch_to_enzymeml()

    '''

    def convert_from_bch_to_enzymeml(self, unit):
        try:
            unit = UnitBase().check_unit(unit)
            return unit
        except Exception as Err:
            print("unit error")
            raise


