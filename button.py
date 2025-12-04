import pygame
from pygame.sprite import Sprite
from font import Text

class Button(Sprite):
    def __init__(self, game, id, text, pos):
        super().__init__()
        self.game = game
        self.screen = game.screen
        self.id = id
        img = pygame.image.load('assets/button.png')
        self.wh = (img.get_rect().width * 2, img.get_rect().height * 2)
        self.image = pygame.transform.scale(img, self.wh)
        self.rect = self.image.get_rect(center = pos)
        self.text = Text(text, pos)
    
    def draw_button(self):
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text.text, self.text.rect)

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

class CheckBox(Button):
    def __init__(self, game, id, text, pos):
        super().__init__(game, id, text, pos)
        start = pygame.image.load('assets/ui_sprites/Sprites/Content/5 Holders/9.png')
        middle = pygame.image.load('assets/ui_sprites/Sprites/Content/5 Holders/10.png')
        end = pygame.image.load('assets/ui_sprites/Sprites/Content/5 Holders/11.png')
        check_box_img = pygame.image.load('assets/ui_sprites/Sprites/Content/5 Holders/22.png')
        start_rect = start.get_rect()
        middle_rect = middle.get_rect()
        end_rect = end.get_rect()