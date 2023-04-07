import pygame
import pygame_menu

from typing import Tuple, Any

from gui.chess import Chess
from src.utils.color_converter import ColorConverter
from src.utils.color_getter import ColorGetter

FPS = 60
WIDTH = HEIGHT = 512


class Menu:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("BI-PYT Chess")

        self.single_player_menu = pygame_menu.Menu("Single-Player Menu", WIDTH, HEIGHT,
                                                   theme=pygame_menu.themes.THEME_SOLARIZED)

        self.single_player_menu.add.button('Start', self.play_single)

        self.single_player_menu.add.selector('Select your color ',
                                             [('White', 'WHITE'),
                                              ('Black', 'BLACK')],
                                             onchange=self.change_color)

        self.single_player_menu.add.selector('Select difficulty ',
                                             [('Easy', 'EASY'),
                                              ('Medium', 'MEDIUM'),
                                              ('Hard', 'HARD')],
                                             onchange=self.change_difficulty)

        self.single_player_menu.add.button('Return to main menu', pygame_menu.events.BACK)

        self.main_menu = pygame_menu.Menu("Chess - Main Menu", WIDTH, HEIGHT, theme=pygame_menu.themes.THEME_SOLARIZED)
        self.main_menu.add.button('Single-player', self.single_player_menu)
        self.main_menu.add.button('Multi-player', self.play_multi)
        self.main_menu.add.button('Quit', pygame_menu.events.EXIT)

        self.difficulty = 'EASY'
        self.color = 'WHITE'

    def show(self):
        while True:
            self.clock.tick(FPS)

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    exit()

            if self.main_menu.is_enabled():
                self.main_menu.mainloop(self.surface, fps_limit=FPS)

            pygame.display.flip()

    def play_single(self):
        self.play(True)

    def play_multi(self):
        self.play(False)

    def play(self, single: bool):
        self.main_menu.disable()
        self.main_menu.full_reset()
        chess = Chess(single, ColorConverter.convert(ColorGetter.get(self.color)), self.difficulty)
        chess.run()

    def change_color(self, value: Tuple[Any, int], color: str) -> None:
        selected, index = value
        print(f'Selected color: "{selected}" ({color}) at index {index}')
        self.color = color

    def change_difficulty(self, value: Tuple[Any, int], difficulty: str) -> None:
        selected, index = value
        print(f'Selected difficulty: "{selected}" ({difficulty}) at index {index}')
        self.difficulty = difficulty
