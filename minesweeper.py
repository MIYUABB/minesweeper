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
    first_click = True
    game_over = False
    running = True
    pygame.init()
    opened = create_opened(height, width)
    mine_field = []
    SCREEN = pygame.display.set_mode((width * BLOCK_SIZE, height * BLOCK_SIZE))
    CLOCK = pygame.time.Clock()

    while running:
        SCREEN.fill(CELL_COLOR)
        if first_click:
            draw_startscreen(height, width)
        elif not game_over:
            draw_minesweeper(height, width, opened, mine_field)
        else:
            draw_endscreen(height, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                x = int((mouse_pos[0] - (mouse_pos[0] % BLOCK_SIZE)) / BLOCK_SIZE)
                y = int((mouse_pos[1] - (mouse_pos[1] % BLOCK_SIZE)) / BLOCK_SIZE)
                if first_click:
                    mine_field = create_minefield.create_minesweeper_matrix(height, width, mine_count, x, y)
                    first_click = False
                else:
                    opened[x][y] = 0

                print(x, y)

        pygame.display.flip()

        CLOCK.tick(60) / 1000

    pygame.quit()


def draw_minesweeper(height, width, opened, mine_field):
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            if opened[x][y] == 1:
                try:
                    if mine_field[x][y] == 0 or mine_field[x][y] == 1:
                        opened[x][y] = 0
                except IndexError:
                    pygame.draw.rect(SCREEN, OPEN_COLOR, rect, 1)
            elif opened[x][y] == 0:
                pygame.draw.rect(SCREEN, OPEN_COLOR, rect, 0)
                number_font = pygame.font.SysFont(None, round(BLOCK_SIZE * 1.3))
                number = str(mine_field[x][y])
                number_image = number_font.render(number, True, BLACK, OPEN_COLOR)
                sizes = number_image.get_size()
                SCREEN.blit(number_image, (
                    x * BLOCK_SIZE + (BLOCK_SIZE - sizes[0]) / 2, y * BLOCK_SIZE + (BLOCK_SIZE - sizes[1]) / 2))


def draw_startscreen(height, width):
    for x in range(width):
        for y in range(height):
            rect = pygame.Rect(x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(SCREEN, OPEN_COLOR, rect, 1)


def draw_endscreen(height, width):
    pass


def create_opened(height, width):
    opened = []
    for x in range(width):
        opened.append([])
        for y in range(height):
            opened[x].append(1)
    return opened


if __name__ == "__main__":
    play_minesweeper(20, 20, 80)
