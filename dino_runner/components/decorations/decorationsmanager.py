from dino_runner.components.decorations.cluod import Cluod
from dino_runner.utils.constants import CLOUD


class DecorationsManager:
    def __init__(self):
        
        self.decoration = (CLOUD)
            
    def draw(self, screen):
        self.decoration.draw(screen)

    