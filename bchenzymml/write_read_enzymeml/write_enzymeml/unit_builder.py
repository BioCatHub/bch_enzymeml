'''
    Creates and returns units commonly used in biocatalysis

    In EnzymeML, the Units need to be built based on the SI (International System of units). This module builds the units commonly used in biocatalysis and
    adds them to every enzymeML document. This module can be seen als boilerplate. It creates all units used in Biocatalysis and adds them o the EnzymeML documentation
    regardless if the unit is needed the describe an experiment or not.

    Important note!

    The unit definition in SBML follows the following laws:
    every self defined unit can consits of multiple "SI" Units:

    the concenentration mmol/L would have the following base units:

        mole: 
            - multiplier = 0 
            - scale = -3
            - exponent = 0
        litre
            - multiplier = 0
            - scale = 0
            - exponent = 0
        
    In the case of mmol/mL the situation would be as follows:

        mole:
            - multiplier = 0
            - scale = -3
            - exponent = 0
        litre
            - multiplier = 0
            - scale = -3
            - exponent = -1
        
        Taken together:
        --> The multiplier helps to adjust if units need to be multiplied by values like 50 or 4.234, anything else than a factor of 10
        --> the scale adjusts a unit if it needs to be multiplied or divided by a multitude of ten
            for example litre to millilitre : scale = -3
        --> the exponent shows the dimension of a unit. If it is cubic metre than the exponent is 3, if it is 1/metre the exponent is -1




'''


from bchenzymml.models.enzymeml_units import UnitsDetails, UnitContainer, Unit, CustomUnitSpecifier
from bchenzymml.models.enzymeml_classes import UnitDetailscls, CustomUnitcls 

class UnitBuilder:
    '''
        Builds the Units needed to describe experiments in Biocatalysis and returns an object which can be used to build the enzymeml model based object.
        
    '''

    def build_ml(self):

        unit_list = []
        unit_list.append(CustomUnitSpecifier.from_orm(CustomUnitcls("litre", -3, 0, 0)))
        ml_details = UnitsDetails.from_orm(UnitDetailscls("mL", "u0", "meta_u0", unit_list, ""))
        ml_container = UnitContainer(__root__={"mL":ml_details})

        return ml_details
    
    def build_ul(self):
        unit_list = []
        unit_list.append(CustomUnitSpecifier.from_orm(CustomUnitcls("litre", -6, 0, 0)))
        ul_details = UnitsDetails.from_orm(UnitDetailscls("uL", "u1", "meta_u1", unit_list, ""))
        ul_container = UnitContainer(__root__={"uL":ul_details})
        return ul_details
    '''
    def build_mol_L(self):
        name = "mol/L"
        unit_list = []
        unit_list.append(CustomUnitSpecifier.from_orm(CustomUnitcls("litre", -9, 0, 0)))
        #unit_list.append(CustomUnitSpecifier.from_orm(CustomUnitcls("mole", 0, 0, 0)))
        mol_L_details = UnitsDetails.from_orm(UnitDetailscls("mole_l", "u2", "meta_u2", unit_list, ""))
        mol_L_container = UnitContainer(__root__={name:mol_L_details})
        return mol_L_details
    '''

    def build_mol_L(self):
        unit_list = []
        unit_list.append(CustomUnitSpecifier.from_orm(CustomUnitcls("mole", -9, 0, 0)))
        ul_details = UnitsDetails.from_orm(UnitDetailscls("mole", "u2", "meta_u2", unit_list, "SBO_0000472"))
        ul_container = UnitContainer(__root__={"umol":ul_details})
        return ul_details


    def build_units(self):
        unit_container = UnitContainer(__root__={"mL":self.build_ml(), 
                                                "uL":self.build_ul(),
                                                "mole_l":self.build_mol_L()})
        
        units = Unit(units=unit_container)
        #print("Die Units in der Methode",units.dict())
        return unit_container.__root__

