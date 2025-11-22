import pygame
from pygame.sprite import Sprite

class Button(Sprite):
    def __init__(self, game, id, text, pos):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.id = id
        self.text_color = (13, 141, 103)
        self.font = pygame.font.SysFont(None, 24)
        img = pygame.image.load('assets/button.png')
        self.wh = (img.get_rect().width * 2, img.get_rect().height * 2)
        self.image = pygame.transform.scale(img, self.wh)
        self.text = self.font.render(text, True, self.text_color)
        self.rect = self.image.get_rect(center = pos)
        self.text_rect = self.text.get_rect(center = pos)
        self.image.blit(self.text, pos)
    
    def draw_button(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text, self.text_rect)

    def update(self):
        pos = pygame.mouse.get_pos()
        basic = pygame.image.load('assets/button.png')
        active = pygame.image.load('assets/button_hover.png')
        if self.rect.collidepoint(pos):
            self.image = pygame.transform.scale(active, self.wh)
        else:
            self.image = pygame.transform.scale(basic, self.wh)

    def check_click(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and self.game.game_pause:
            return self.id
        else:
            return False