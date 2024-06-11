from random import randint


def create_minesweeper_matrix(width, height, mine_count, x, y):
    mine_field = []
    for horizontal in range(width):
        mine_field.append([])
        for vertical in range(height):
            mine_field[horizontal].append(0)
    mine_field[x][y] = 10
    if x != width - 1:
        mine_field[x + 1][y] += 10
    if y != height - 1:
        mine_field[x][y + 1] += 10
    if x != width - 1 and y != height - 1:
        mine_field[x + 1][y + 1] += 10
    if x != 0:
        mine_field[x-1][y] = 10
        if y != height-1:
            mine_field[x-1][y+1] = 10
    if y != 0:
        mine_field[x][y-1] = 10
        if x != width-1:
            mine_field[x+1][y-1] = 10
    if x != 0 and y != 0:
        mine_field[x-1][y-1] = 10

    while mine_count > 0:
        random_x = randint(0, width-1)
        random_y = randint(0, height-1)
        if mine_field[random_x][random_y] != 10:
            mine_field[random_x][random_y] = 9
            mine_count -= 1
    for row in mine_field:
        print(row)

    for x in range(len(mine_field)):
        for y in range(x):
            if mine_field[x][y] == 10:
                mine_field[x][y] -= 10
            elif mine_field[x][y] == 9:
                if x != width-1:
                    mine_field[x + 1][y] += 1
                if y != height-1:
                    mine_field[x][y + 1] += 1
                if x != width-1 and y != height-1:
                    mine_field[x + 1][y + 1] += 1
                if x != 0:
                    mine_field[x - 1][y] += 1
                    if y != height-1:
                        mine_field[x - 1][y + 1] += 1
                if y != 0:
                    mine_field[x][y - 1] += 1
                    if x != width-1:
                        mine_field[x + 1][y - 1] += 1
                if x != 0 and y != 0:
                    mine_field[x - 1][y - 1] += 1
            else:
                continue
