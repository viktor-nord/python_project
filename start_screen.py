import pygame

from button import Button
from animation import Animation, AnimationIndex

class StartScreen:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width = self.screen_rect.width
        self.height = self.screen_rect.height
        self.image = pygame.image.load('assets/ui_sprites/Sprites/Book Desk/3.png')
        self.papper = ''
        self.rect = self.image.get_rect()
        self.rect.center = self.screen_rect.center
        self.generate_buttons()
        self.animation = Animation(
            game, AnimationIndex.header.value, (None, 50)
        )
        self.font = pygame.font.SysFont(None, 32)
        self.title = self.font.render('Akavir: God of None', True, (13, 141, 103))
        self.title_rect = self.title.get_rect(center = self.animation.rect.center)
    
    def generate_buttons(self):
        buttons = ['New Game', 'Load Game', 'Options']
        x, y = self.screen_rect.center
        y -= 70
        for i, button in enumerate(buttons):
            self.game.buttons.add(Button(self.game, i + 1, button, (x,y)))
            y += 70

    def blitme(self):
        fade = pygame.Surface((self.width, self.height))
        fade.fill((0, 0, 0))
        fade.set_alpha(160)
        self.screen.blit(fade, (0, 0))
        self.screen.blit(self.image, self.rect)
        self.game.buttons.draw(self.game.screen)
        for btn in self.game.buttons:
            btn.draw_button()
        self.animation.blitme(self.game.screen)
        if self.animation.counter > ((self.animation.lenght - 1) * 2) - 1:
            self.screen.blit(self.title, self.title_rect)