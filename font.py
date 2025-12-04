import pygame
import pygame.font

class Text:
    def __init__(self, text, center_pos, size=20, has_underline=False):
        pygame.font.init()
        self.text = text
        self.has_underline = has_underline
        self.text_color = (13, 141, 103)
        self.font = pygame.font.Font('assets/font/ThaleahFat.ttf', size)
        self.under_line_img = pygame.image.load('assets/ui_sprites/Sprites/Content/5 Holders/20_2.png')
        self.text = self.font.render(text, True, self.text_color)
        self.rect = self.text.get_rect(center = center_pos)
        self.bottom_margin = 8

    def blitme(self, screen):
        screen.blit(self.text, self.rect)
        if self.has_underline:
            r = self.rect
            y = self.rect.bottom + self.bottom_margin
            if self.rect.width > self.under_line_img.get_width():
                x = r.left + 4
                gg = x + self.rect.width - self.under_line_img.get_width()
                while x < gg:
                    pos = self.under_line_img.get_rect(left = x, bottom = y)
                    screen.blit(self.under_line_img, pos)
                    x += self.under_line_img.get_width()
                # screen.blit(self.under_line_img, self.under_line_img.get_rect(right = r.right, bottom = y))
            else:
                ul_pos = self.under_line_img.get_rect(center=r.center, bottom = y)
                screen.blit(self.under_line_img, ul_pos)

class Title(Text):
    def __init__(self, text, center_pos, size=32, has_underline=False):
        super().__init__(text, center_pos, size, has_underline)
        self.font = pygame.font.Font('assets/font/Blackwood Castle.ttf', size)
        self.text = self.font.render(text, True, self.text_color)