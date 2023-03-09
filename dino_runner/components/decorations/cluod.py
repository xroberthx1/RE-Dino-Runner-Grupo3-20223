import random
from dino_runner.utils.constants import CLOUD, SCREEN_WIDTH


class Cluod:
    def __init__(self):
        self.image = CLOUD
        self.dino_rect = self.image.get_rect()
        self.type = 0
        self.rect.x = 900
        self.rect.y = random.randint(140, 240)
        self.fly_index = 0

    def draw(self,screen):
        if self.fly_index >=10:
            self.fly_index = 0
        elif self.fly_index <= 5:
            self.image = CLOUD
        else:
            self.image = CLOUD

        screen.blit(self.image, (self.rect.x, self.rect.y))
        self.fly_index +=1