import pygame

from button import CheckBoxList
from font import Text, Title
from book import Book

class CharacterCreation:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.bg = pygame.image.load('assets/ui_sprites/Sprites/Book Desk/3.png')
        self.bg_rect = self.bg.get_rect(center = game.screen_rect.center)
        self.book = Book(game)
        self.right_page = pygame.Rect((534, 90),(270, 358))
        self.check_box_list = CheckBoxList(
            self.game, self.right_page,
            [
                {"id":"munk", "text":"Munk"},
                {"id":"cleric", "text":"Cleric"},
                {"id":"priest", "text":"Priest"},
            ] 
        )

    def blitme(self):
        self.screen.blit(self.bg, self.bg_rect)
        self.book.blitme(self.screen)
        self.check_box_list.draw_list()