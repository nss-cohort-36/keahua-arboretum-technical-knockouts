from ..animal import IAquatic

class IAquaticPrey(IAquatic):

    def __init__(self):
        super().__init__()
        self.aquatic_prey = True