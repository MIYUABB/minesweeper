

class MinesweeperMatrix:

    def __init__(self, block_x, block_y, difficulty):
        self._block_x = block_x
        self._block_y = block_y
        self._difficulty = difficulty
        self.mine_count = (self._block_x * self._block_y) * self._difficulty
        self._matrix  = list()


    def create_matrix(self):
        for i in range(self._block_y):
            for j in range(self._block_x):
                pass
        matrix = None
        return matrix

    def add_list(self):
        self._matrix.append(list())
