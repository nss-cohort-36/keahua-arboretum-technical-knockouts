from ..animal import IAquatic

class ISaltFresh(IAquatic):

    def __init__(self):
        super().__init__()
        self.cell_type = "isotonic"