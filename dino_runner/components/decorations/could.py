import random
from dino_runner.utils.constants import COULD


class Could:
    def __init__(self):
        self.image = COULD
        self.rect = 500
        self.rect.x = 500
        self.rect.y = 500

    def draw(self,screen):
        
        self.image = COULD
        screen.blit(self.image, (self.rect.x, self.rect.y))
        