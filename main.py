import pygame
from draughts.constants import WIDTH, HEIGHT, SQUARE_SIZE, RED
from draughts.game import Game

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Draughts')

def get_row_col_from_mouse(pos) -> tuple[int, int]:
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    # piece = board.get_piece(0, 1)
    # board.move(piece, 4, 3)

    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                # if game.turn == RED:
                game.select(row, col)

        game.update()

    pygame.quit()

if __name__ == "__main__":
    main()