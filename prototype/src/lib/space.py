from cell import Cell


class Space:

    def __init__(self, xlen: 'int', ylen: 'int'):
        self.__xlen = xlen
        self.__ylen = ylen
        self.__space = None

        self.__build_space()

    @property
    def xlen(self):
        return self.__xlen

    @property
    def ylen(self):
        return self.__ylen

    @property
    def space(self):
        return self.__space

    def __build_space(self):
        space = []
        for row in range(self.ylen):
            space.append([Cell(col, row) for col in range(self.xlen)])

        self.__space = space
