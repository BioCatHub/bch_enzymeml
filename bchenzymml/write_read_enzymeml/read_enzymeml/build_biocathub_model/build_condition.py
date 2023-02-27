from bchenzymml.models.biocathub_model import Buffer, Condition


class BuildCondition:

    def __init__(self, enzml_model):
        self.enzml_model = enzml_model
    
    def build_buffer(self):
        buffer = Buffer(type="kpi buffer", concentration=1, unit="mmol/L")
        return buffer

    def build_condition(self):
        condition = Condition(ph=5, temp=33, unit="°C", buffer=self.build_buffer(), others=[])
        return condition.dict()