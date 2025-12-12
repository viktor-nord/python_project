from turtle import left
import pygame
import pygame.font

class Text:
    def __init__(self, text, parent, size=20, has_underline=False, centered=True):
        pygame.font.init()
        self.text = text
        self.has_underline = has_underline
        self.text_color = (13, 141, 103)
        self.font = pygame.font.Font('assets/font/ThaleahFat.ttf', size)
        self.under_line_img = pygame.image.load('assets/ui_sprites/Sprites/Content/5 Holders/20_2.png')
        self.text = self.font.render(text, True, self.text_color)
        self.margin = 8
        if centered:
            self.rect = self.text.get_rect(center = parent.center)
        else: 
            self.rect = self.text.get_rect(left = parent.left, centery = parent.centery)

    def blitme(self, screen):
        screen.blit(self.text, self.rect)
        if self.has_underline:
            r = self.rect
            y = self.rect.bottom + self.margin
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
    def __init__(self, text, parent, size=42, has_underline=False):
        super().__init__(text, parent, size, has_underline, centered=True)
        self.font = pygame.font.Font('assets/font/Blackwood Castle.ttf', size)
        self.text = self.font.render(text, True, self.text_color)