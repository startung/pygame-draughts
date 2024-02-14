import pygame
from .board import Board
from .constants import RED, WHITE, BLUE, SQUARE_SIZE

class Game:
    def __init__(self, win) -> None:
        self._init()
        self.win = win

    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()

    def _init(self):
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}
        self.selected = None

    def reset(self):
        self._init()

    def change_turn(self):
        self.valid_moves = {}
        if self.turn == RED:
            self.turn = WHITE
        else:
            self.turn = RED

    def select(self, row, col):
        if self.selected:
            result = self._move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_piece(row, col)
        if piece != 0 and piece.colour == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def _move(self, row, col):
        piece = self.board.get_piece(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove(skipped)
            self.change_turn()
        else:
            return False
        return True

    def winner(self):
        return self.board.winner()

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.win, BLUE, (col*SQUARE_SIZE+SQUARE_SIZE//2, row*SQUARE_SIZE+SQUARE_SIZE//2), 15)