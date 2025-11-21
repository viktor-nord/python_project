import pygame

from button import Button

class StartScreen:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.image = pygame.image.load('assets/start_img.bmp')
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.generate_buttons()
        self.buttons = [self.new_btn, self.load_btn, self.option_btn]
    
    def generate_buttons(self):
        base_btn = Button(self.game, 0, 'test', (0,0))
        base_rect = base_btn.rect
        base_rect.center = self.screen_rect.center
        pos_1 = (base_rect.center[0], base_rect.center[1] -70)
        pos_2 = base_rect.center
        pos_3 = (base_rect.center[0], base_rect.center[1] +70)
        self.new_btn = Button(self.game, 1, 'New Game', pos_1)
        self.load_btn = Button(self.game, 2, 'Load Game', pos_2)
        self.option_btn = Button(self.game, 3, 'Options', pos_3)

    def blitme(self):
        fade = pygame.Surface((self.width, self.height))
        fade.fill((0, 0, 0))
        fade.set_alpha(200)
        self.screen.blit(fade, (0, 0))
        self.screen.blit(self.image, self.rect)
        self.new_btn.draw_button()
        self.load_btn.draw_button()
        self.option_btn.draw_button()