
class VesselError(Exception):
    pass

class ProteinError(Exception):
    def __init__(self, error):
        self.message = "there was an error during the protein dictionary build process"
        self.error = error
        super().__init__(self.message)
    
    

class ProteinKeyError(Exception):
    def __init__(self, missing_key):
        self.message = "there was an error during the protein dictionary build process"
        self.missing_key = missing_key
        super().__init__(self.message)

class CreatorError(Exception):
    pass

class ReactantsError(Exception):
    pass

class ReactionsError(Exception):
    pass


class MeasurementError(Exception):
    pass