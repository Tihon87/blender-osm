from .container import Container
from .level_styles import LevelStyles


class Facade(Container):
    """
    Represents a building facade.
    It's typically composed of one or more faces (in the most cases rectangular ones)
    """
    
    def __init__(self):
        super().__init__()
        self.valid = True
    
    def init(self):
        self.valid = True
        self.faces = []
        self.normal = None
        self.levelStyles = LevelStyles()
        
        self.type = ("front", "back", "side")
        self.neighborL = None
        self.neighborR = None
        self.neighborT = None
        self.neighborB = None

    @classmethod
    def getItem(cls, itemFactory, parent, indices, width, heightLeft, heightRightOffset):
        item = itemFactory.getItem(cls)
        item.init()
        item.parent = parent
        item.indices = indices
        item.width = width
        # assign uv-coordinates
        item.uvs = ( (0., 0.), (width, heightRightOffset), (width, heightLeft), (0., heightLeft) )
        return item
    
    @property
    def front(self):
        return True
    
    @property
    def back(self):
        return True