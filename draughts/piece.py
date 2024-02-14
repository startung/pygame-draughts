import pygame
from .constants import RED, WHITE, GREY, SQUARE_SIZE, CROWN

class Piece:
    PADDING = 15
    OUTLINE = 2

    def __init__(self, row: int, col: int, colour: tuple[int, int, int]) -> None:
        self.row = row
        self.col = col
        self.colour = colour
        self.king = False
        self.direction = 1 if self.colour == WHITE else -1
        self.x = 0
        self.y = 0
        self.calc_pos()

    def __repr__(self) -> str:
        return str(self.colour)

    def calc_pos(self) -> None:
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def make_king(self) -> None:
        self.king = True

    def draw(self, win) -> None:
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(win, GREY, (self.x, self.y), radius+self.OUTLINE)
        pygame.draw.circle(win, self.colour, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() // 2, self.y - CROWN.get_height() // 2))

    def move(self, row, col) -> None:
        self.row = row
        self.col = col
        self.calc_pos()