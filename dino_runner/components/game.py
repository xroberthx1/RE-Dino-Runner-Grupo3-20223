import pygame
from dino_runner.components.Dino import Dino
from dino_runner.components.obstacles.obstaclemanager import ObstacleManager
from dino_runner.components import text_utils
from dino_runner.utils.constants import BG, DINO_START, ICON, RUNNING, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380
        self.player = Dino()
        self.obstacle_manager = ObstacleManager()
        self.points = 0
        self.running = True
        self.death_count = 0


    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.obstacle_manager.reset_obstacles()
        while self.playing:
            self.events()
            self.update()
            self.draw()
        
        

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self)
        


    def draw(self):
        
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def execute(self):
        while self.running:
            if not self.playing:
                self.show_menu()
                self.points = 0
                self.game_speed = 20
                
                

            
    def show_menu(self):
        if self.running == True:
            white_color = (255,255,255)
            self.screen.fill(white_color)
            self.print_menu_elements()
            pygame.display.update()
            self.handle_key_events_on_menu()
        
        elif self.running == False:
            white_color = (255,255,255)
            self.screen.fill(white_color)
            self.print_menu_elements_end()
            pygame.display.update()
            self.handle_key_events_on_menu()
        

    def print_menu_elements(self):
        if self.death_count == 0:
            text, text_rect = text_utils.get_centered_message('Press any Key to Start')
            self.screen.blit(text, text_rect)
        
    
        #Tarea posible
        else:
            pass

        self.screen.blit(DINO_START, (80, 310))

    def print_menu_elements_end(self):
        if self.death_count > 1:
            text, text_rect = text_utils.get_centered_message_end('GAME OVER')
            self.screen.blit(text, text_rect)
        
    
        #Tarea posible
        else:
            pass

        self.screen.blit(DINO_START, (80, 310))

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.playing = False
                pygame.display.quit()
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                self.run()
                

    def score(self):
        self.points += 1
        if self.points % 100 == 0:
            self.game_speed += 100
        text, text_rect = text_utils.get_score_element(self.points)
        self.screen.blit(text, text_rect)
        
