import random
from dino_runner.components.obstacles.cactus import Cactus
from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update (self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus(random.choice([SMALL_CACTUS, LARGE_CACTUS])))
        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):
                game.playing = False
                break

    def draw (self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)