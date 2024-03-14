import sys
import time
import pygame

BLOCK_COLOR = (107, 107, 107)
GRID_COLOR = (150, 150, 150)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
BLOCKSIZE = 20


def main():
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
                mouse_pos_x = round(pygame.mouse.get_pos()[0] / BLOCKSIZE) * BLOCKSIZE
                if pygame.mouse.get_pos()[0] < mouse_pos_x:
                    mouse_pos_x = mouse_pos_x - BLOCKSIZE
                mouse_pos_y = round(pygame.mouse.get_pos()[1] / BLOCKSIZE) * BLOCKSIZE
                if pygame.mouse.get_pos()[1] < mouse_pos_y:
                    mouse_pos_y = mouse_pos_y - BLOCKSIZE
                rect = pygame.Rect(mouse_pos_x, mouse_pos_y, BLOCKSIZE, BLOCKSIZE)
                pygame.draw.rect(SCREEN, GRID_COLOR, rect)

        pygame.display.update()


def draw_grid():
    for x in range(0, WINDOW_WIDTH, BLOCKSIZE):
        for y in range(0, WINDOW_HEIGHT, BLOCKSIZE):
            rect = pygame.Rect(x, y, BLOCKSIZE, BLOCKSIZE)
            pygame.draw.rect(SCREEN, GRID_COLOR, rect, 1)


if __name__ == "__main__":
    main()
