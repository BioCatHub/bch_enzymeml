from bchenzymml.models.biocathub_model import Buffer, Condition


class BuildCondition:

    def __init__(self, enzml_model):
        self.enzml_model = enzml_model
    
    def build_buffer(self):
        buffer = Buffer(type="kpi buffer", concentration=1, unit="mmol/L")
        return buffer

    def build_condition(self):
        try:

            reactions = self.enzml_model["reactions"]["r0"] # is the condition in the reaction enzymeml model?
            print(reactions)
            ph = reactions["ph"]
            temperature = reactions["temperature"]
            temperature_unit = reactions["temperature_unit"]


            condition = Condition(ph=ph, temp=temperature, unit=temperature_unit, buffer=self.build_buffer(), others=[])
            return condition.dict()
    
        except Exception as err:
            print("conditions error")
            raise