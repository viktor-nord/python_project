import pygame.font

class Button:
    def __init__(self, game, id, text, pos):
        self.game = game
        self.screen = game.screen
        self.id = id
        self.screen_rect = self.screen.get_rect()
        self.width = 200
        self.height = 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(pos[0], pos[1], self.width, self.height)
        self._prep_text(text, pos)

    def _prep_text(self, text, pos):
        self.text_image = self.font.render(
            text, True, self.text_color, self.button_color
        )
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = pos
        self.rect.center = pos
    
    def draw_button(self):
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)

    def check_click(self):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and self.game.game_pause:
            return self.id
        else:
            return False