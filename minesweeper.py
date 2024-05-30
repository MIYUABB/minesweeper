import pygame
import create_minefield

# CONSTANTS
CELL_COLOR = "#15910f"
LINE_COLOR = "#22911d"
OPEN_COLOR = "#e6e6e6"
BLACK = "#000000"
BLOCK_SIZE = 20


def play_minesweeper(height, width, mine_count):
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((width * BLOCK_SIZE, height * BLOCK_SIZE))
    CLOCK = pygame.time.Clock()
    mine_field, opened = create_minefield.create_minesweeper_matrix(width, height, mine_count)
    running = True
    dt = 0
    print(mine_field)
    print("\n\n")
    for row in mine_field:
        print(row)
    print("\n\n")
    print(opened)
    print("\n\n")
    for row in opened:
        print(row)

    while running:
        SCREEN.fill(CELL_COLOR)
        draw_minesweeper(height, width, opened, mine_field)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()

        dt = CLOCK.tick(60) / 1000

    pygame.quit()


def draw_minesweeper(height, width, opened, minefield):
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(y * BLOCK_SIZE, x * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            if opened[x][y] == 1:
                pygame.draw.rect(SCREEN, OPEN_COLOR, rect, 1)
            elif opened[x][y] == 0:
                pygame.draw.rect(SCREEN, OPEN_COLOR, rect, 0)
                number_font = pygame.font.SysFont(None, round(BLOCK_SIZE * 1.3))
                number = str(minefield[x][y])
                number_image = number_font.render(number, True, BLACK, OPEN_COLOR)
                sizes = number_image.get_size()
                SCREEN.blit(number_image, (y * BLOCK_SIZE + (BLOCK_SIZE - sizes[0]) / 2, x * BLOCK_SIZE + (BLOCK_SIZE - sizes[1]) / 2))


if __name__ == "__main__":
    play_minesweeper(5, 5, 5)
