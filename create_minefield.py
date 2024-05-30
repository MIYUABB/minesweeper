from random import randint


def create_minesweeper_matrix(width, height, mine_count):
    mine_field = []
    for i in range(width):
        mine_field.append([])
        for j in range(height):
            mine_field[i].append(0)
    if mine_count <= width * height:
        for mine in range(mine_count):
            while True:
                x_axis = randint(0, width - 1)
                y_axis = randint(0, height - 1)
                if mine_field[x_axis][y_axis] == 9:
                    continue
                else:
                    mine_field[x_axis][y_axis] = 9
                    break
        correct_fields(mine_field)
        opened = create_opened(mine_field)
        return mine_field, opened
    else:
        return "Invalid mines count"


def correct_fields(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 9:
                continue
            else:
                counter = 0
                try:
                    if field[i - 1][j - 1] == 9:
                        counter += 1
                except IndexError:
                    pass
                try:
                    if field[i - 1][j] == 9:
                        counter += 1
                except IndexError:
                    pass
                try:
                    if field[i - 1][j + 1] == 9:
                        counter += 1
                except IndexError:
                    pass
                try:
                    if field[i][j - 1] == 9:
                        counter += 1
                except IndexError:
                    pass
                try:
                    if field[i][j + 1] == 9:
                        counter += 1
                except IndexError:
                    pass
                try:
                    if field[i + 1][j - 1] == 9:
                        counter += 1
                except IndexError:
                    pass
                try:
                    if field[i + 1][j] == 9:
                        counter += 1
                except IndexError:
                    pass
                try:
                    if field[i + 1][j + 1] == 9:
                        counter += 1
                except IndexError:
                    pass
                if counter >= 8:
                    field[i][j] = 9
                else:
                    field[i][j] = counter
    return field


def create_opened(mine_field):
    opened = []
    for x in range(len(mine_field)):
        opened.append([])
        for y in range(len(mine_field[x])):
            if mine_field[x][y] == 0 or mine_field[x][y] == 1:
                opened[x].append(0)
            else:
                opened[x].append(1)
    return opened