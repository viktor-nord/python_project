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
    def __init__(self, game, id, text, pos, width):
        super().__init__(game, id, text, pos)
        self.width = 280
        self.height = game.settings.tile_size
        self.rect = pygame.Rect(
            (pos[0] - self.width / 2, pos[1] - self.height / 2),
            (self.width, self.height)
        )
        baseUrl = "assets/ui_sprites/Sprites/Content/"
        img_array = (
            baseUrl + "4 Buttons/Sliced/5.png",
            baseUrl + "5 Holders/22.png",
            baseUrl + "5 Holders/12.png",
            baseUrl + "5 Holders/13.png",
            baseUrl + "5 Holders/14.png",
        )
        self.images = [pygame.image.load(url) for url in img_array]
        

        self.arrow = pygame.image.load("assets/ui_sprites/Sprites/Content/4 Buttons/Sliced/5.png")
        url = "assets/ui_sprites/Sprites/Content/5 Holders/"
        self.start = pygame.image.load(url + '9.png')
        self.middle = pygame.image.load(url + '10.png')
        self.end = pygame.image.load(url + '11.png')
        self.check_box_img = pygame.image.load(url + '22.png')
        x = self.rect.top + self.height/2
        y = left=self.rect.top
        self.check_box_rect = self.check_box_img.get_rect(
            top= self.rect.top + self.height/2, 
            left=self.rect.top + self.height/2
        )        
        self.start_rect = self.start.get_rect()
        self.middle_rect = self.middle.get_rect()
        self.end_rect = self.end.get_rect()
        self.end_rect.right = pos[1] + width/2
        self.margin = 10

    def draw_button(self):
        x = self.rect.left
        y = self.rect.top
        self.screen.blit(self.images[1], (x + 8, y + 8))
        self.screen.blit(self.images[2], (x + self.game.settings.tile_size, y))
        x += self.game.settings.tile_size + self.start_rect.width
        while x < self.rect.left + self.width - self.middle_rect.width:
            self.screen.blit(self.images[3], (x, y))
            x += self.middle_rect.width
        self.screen.blit(self.images[4], self.end.get_rect(right=self.rect.right, top=self.rect.top))
        self.screen.blit(self.text.text, self.text.rect)

    # update