import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import BIRD, LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    
    def __init__(self):
        self.obstacles = []

    def update (self, game):
        x = random.randint(0,2)
        if len(self.obstacles) == 0:
            if x == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif x == 1:
                self.obstacles.append(Cactus(SMALL_CACTUS))
            elif x == 2:
                self.obstacles.append(Bird(BIRD))
        
        
        
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []