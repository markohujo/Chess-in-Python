import pygame
import pygame_menu

from gui.image_loader import ImageLoader
from src.board.board_factory import BoardFactory
from src.bots.random import RandomBot
from src.bots.minimax import MinimaxBot
from src.utils.color_converter import ColorConverter
from src.utils.enums.color import Color

WIDTH = HEIGHT = 512
CHESS_DIMENSION = 8
SQUARE_SIZE = WIDTH // CHESS_DIMENSION
WHITE = (255, 250, 240)
BLACK = (139, 69, 19)
HIGHLIGHT_PIECE_COLOR = (65, 105, 225)
HIGHLIGHT_PIECE_ALPHA = 120
HIGHLIGHT_MOVE_COLOR = (173, 255, 47)
HIGHLIGHT_MOVE_ALPHA = 150
FPS = 60
MEDIUM_DEPTH = 1
HARD_DEPTH = 3


class Chess:
    def __init__(self, single: bool, bot_color: Color, difficulty: str):
        pygame.init()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True
        self.end = False
        self.pieces = ['wp', 'wR', 'wN', 'wB', 'wQ', 'wK', 'bp', 'bR', 'bN', 'bB', 'bQ', 'bK']
        self.images = {}
        self.board = BoardFactory.create()
        self.single = single

        if single:
            if difficulty.lower() == 'easy':
                self.bot = RandomBot(bot_color)
            elif difficulty.lower() == 'medium':
                self.bot = MinimaxBot(bot_color, MEDIUM_DEPTH)
            elif difficulty.lower() == 'hard':
                self.bot = MinimaxBot(bot_color, HARD_DEPTH)

        self.color_on_turn = Color.WHITE
        self.selected_square = ()
        self.player_clicks = []

    def run(self):
        pygame.display.set_caption("BI-PYT Chess")
        clock = pygame.time.Clock()
        self.__load_images()

        while self.running:
            clock.tick(FPS)
            self.__check_events()
            self.__draw_game()

            pygame.display.flip()

            if self.single and self.color_on_turn == self.bot.color:
                self.bot.take_turn(self.board)
                self.color_on_turn = ColorConverter.convert(self.bot.color)

            if self.__checkmate():
                break

            if self.__stalemate():
                break

            pygame.display.flip()

        while self.end:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end = False
            pygame.display.flip()

        pygame.quit()

    def __checkmate(self):
        if self.board.checkmate(self.color_on_turn):
            self.__display_winner()
            self.running = False
            self.end = True
            return True
        return False

    def __stalemate(self):
        if self.board.stalemate(self.color_on_turn):
            self.__display_draw()
            self.running = False
            self.end = True
            return True
        return False

    def __load_images(self):
        for piece in self.pieces:
            self.images[piece] = ImageLoader(f'{piece}.png').load().scale(SQUARE_SIZE, SQUARE_SIZE).get

    def __check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not self.single or (self.single and self.color_on_turn != self.bot.color):
                    self.__on_mouse()

    def __on_mouse(self):
        mouse_location = pygame.mouse.get_pos()
        square = (mouse_location[0] // SQUARE_SIZE, mouse_location[1] // SQUARE_SIZE)

        if self.selected_square == square:
            self.selected_square = ()
            self.player_clicks = []
        else:
            self.selected_square = square
            self.player_clicks.append(self.selected_square)

        if len(self.player_clicks) == 2:
            if self.__take_turn():
                self.selected_square = ()
                self.player_clicks = []
                self.color_on_turn = ColorConverter.convert(self.color_on_turn)
            else:
                self.selected_square = square
                self.player_clicks = [self.selected_square]

    def __take_turn(self) -> bool:
        src = self.__get_src()
        dest = self.__get_dest()

        square = self.board.at(src[1], src[0])

        if square.empty() or square.piece.color != self.color_on_turn:
            return False

        move = square.piece.valid_move_to(self.board, square.x, square.y, dest[1], dest[0])

        if move is None or (move.castling() and self.board.check(self.color_on_turn)):
            return False

        move.execute()
        return True

    def __draw_game(self):
        self.__draw_board()
        self.__highlight_squares()
        self.__draw_pieces()

    def __draw_board(self):
        colors = [WHITE, BLACK]
        for row in range(CHESS_DIMENSION):
            for col in range(CHESS_DIMENSION):
                square_color = colors[(row + col) % 2]
                pygame.draw.rect(self.surface, square_color,
                                 pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def __draw_pieces(self):
        for row in range(CHESS_DIMENSION):
            for col in range(CHESS_DIMENSION):
                square = self.board.at(row, col)
                if not square.empty():
                    self.surface.blit(self.images[repr(square.piece)],
                                      pygame.Rect(col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

    def __highlight_squares(self):
        if self.selected_square == ():
            return

        col, row = self.selected_square
        square = self.board.at(self.selected_square[1], self.selected_square[0])

        if square.empty() or square.piece.color != self.color_on_turn:
            return

        highlight_surface = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))

        highlight_surface.set_alpha(HIGHLIGHT_PIECE_ALPHA)
        highlight_surface.fill(HIGHLIGHT_PIECE_COLOR)
        self.surface.blit(highlight_surface, (col * SQUARE_SIZE, row * SQUARE_SIZE))

        highlight_surface.set_alpha(HIGHLIGHT_MOVE_ALPHA)
        highlight_surface.fill(HIGHLIGHT_MOVE_COLOR)

        piece = square.piece
        moves = piece.valid_moves(self.board, square.x, square.y)

        for move in moves:
            if move.castling() and self.board.check(self.color_on_turn):
                continue

            self.surface.blit(highlight_surface, (SQUARE_SIZE * move.square_to.y, SQUARE_SIZE * move.square_to.x))

    def __display_winner(self):
        text = f'Checkmate! {self.__get_color_text(ColorConverter.convert(self.color_on_turn))} wins!'
        self.surface.fill((0, 0, 0))
        self.__display_text(text, 40, (255, 255, 255))

    def __display_draw(self):
        text = "Stalemate! It's a draw!"
        self.surface.fill((0, 0, 0))
        self.__display_text(text, 40, (255, 255, 255))

    def __display_text(self, text: str, size: int, color):
        t = pygame.font.Font(pygame_menu.font.FONT_FRANCHISE, size).render(text, True, color)
        self.surface.blit(t, (WIDTH / 2 - t.get_width() / 2, HEIGHT / 2 - t.get_height() / 2))
        pygame.display.flip()

    @staticmethod
    def __get_color_text(color: Color) -> str:
        return "White" if color == Color.WHITE else "Black"

    def __get_src(self):
        return self.player_clicks[0]

    def __get_dest(self):
        return self.player_clicks[1]
