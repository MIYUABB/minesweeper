import sys
import time
import pygame
import minesweeper_matrix

BLOCK_COLOR = (107, 107, 107)
GRID_COLOR = (200, 200, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
BLOCK_SIZE = 20


def main():
    board = create_board()
    global SCREEN
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Animation")
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLOCK_COLOR)
    while True:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos_x = round(pygame.mouse.get_pos()[0] / BLOCK_SIZE) * BLOCK_SIZE
                if pygame.mouse.get_pos()[0] < mouse_pos_x:
                    mouse_pos_x = mouse_pos_x - BLOCK_SIZE
                mouse_pos_y = round(pygame.mouse.get_pos()[1] / BLOCK_SIZE) * BLOCK_SIZE
                if pygame.mouse.get_pos()[1] < mouse_pos_y:
                    mouse_pos_y = mouse_pos_y - BLOCK_SIZE
                rect = pygame.Rect(mouse_pos_x, mouse_pos_y, BLOCK_SIZE, BLOCK_SIZE)
                pygame.draw.rect(SCREEN, GRID_COLOR, rect)

        pygame.display.update()


def draw_grid():
    for x in range(0, WINDOW_WIDTH, BLOCK_SIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCK_SIZE):
            rect = pygame.Rect(x, y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, GRID_COLOR, rect, 1)

def create_board():
    heigth = int(input("Give a heigth"))
    width = int(input("Give a width"))
    mines = int(input("Give num of mines"))
    board = minesweeper_matrix.create_minesweeper_board(heigth, width, mines)
    return board


if __name__ == "__main__":
    main()
