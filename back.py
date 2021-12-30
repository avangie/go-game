from assets.constans import BLACK, WHITE

class Board:
    def __init__(self):
        """
        Create and initialize a board.
        """
        self._next_player = BLACK
        self._stones = []
        self.sets = []

    def player(self):
        return self._next_player
    
    def set_next_player(self, player):
        self._next_player = player

    def get_set(self):
        return self.sets
    
    def whose_turn(self):
        """
        Update turns of the players by flipping colors of the stones.
        """
        if self.player() == BLACK:
            self.set_next_player(WHITE)
            return BLACK
        else:
            self.set_next_player(BLACK)
            return WHITE

    def stones(self):
        """
        List, contains all stones on board.
        """
        return self._stones
    
    def add_stone(self, point):
        """
        Add stone to a list.
        """
        if point not in self.stones():
            self.stones().append(point)

    def find(self, coords = None, coord = None):
        """
        Find stones on the board by given coordinates.
        """
        if not coords:
            coords = []
        stones = []
        for aset in self.get_set():
            for stone in aset.get_set():
                if stone.coordy() in coords:
                    stones.append(stone)
                elif stone.coordy() == coord and not coords:
                    return stone 
        return stones      


class Stone:
    def __init__(self, color, coordinates, board):
        """
        Create and initialize a stone.
        Coordinates argument is a tuple, ie. (2,2) represents 
        upper left corner of the board.
        Color argument is a color of the stone - white or black.
        
        """
        self._color = color
        self._coordinates = coordinates
        self.board = board
        self.set = self.fset()

    def get_board(self):
        return self.board

    def get_color(self):
        return self._color

    def get_set(self):
        return self.set

    def set_set(self, set):
        self.set = set

    def fset(self):
        """
        Find a set (family) for a stone.
        If none, creates a family.
        """
        sets = []
        stones = self.get_board().find(coords = self.neighbours())
        for stone in stones:
            if stone.get_set() not in sets and stone.get_color() == self.get_color():
                sets.append(stone.get_set())
        if sets:
            if len(sets) > 1:
                for fam in sets[1:]:
                    sets[0].merge(fam)
            sets[0].get_set().append(self)
            return sets[0]     
        else:
            set = Family(self.get_board(), self)
            return set

    def find_all_neigh(self):
        """
        Create a list of all possible neighbors of the stone.
        """
        left = (self.coordy()[0] - 1, self.coordy()[1])
        right = (self.coordy()[0] + 1, self.coordy()[1])
        upper = (self.coordy()[0], self.coordy()[1] - 1)
        lower = (self.coordy()[0], self.coordy()[1] + 1)
        points = [left, right, lower, upper]
        return points

    def coordy(self):
        return self._coordinates

    def neighbours(self):
        """
        In edge cases, removes a non-existent neighbor from 
        the list of all possible neighbors.
        """
        points = self.find_all_neigh()
        copy_points = points
        for neighbor in points:
            if self.coordy()[0] == 20 and self.coordy()[1] == 2:
                points = [copy_points[0], copy_points[2]]
            elif self.coordy()[0] == 20 and self.coordy()[1] == 20:
                points = [copy_points[0], copy_points[3]]
            elif not 1 < neighbor[0] < 21 or not 1 < neighbor[1] < 21:
                points.remove(neighbor)
        return points

    def properties(self):
        a = self.neighbours()
        stones = self.get_board().find(coords=a)
        for stone in stones:
            a.remove(stone.coordy())
        return a

    def remove_stone(self):
        """
        Remove a stone.
        """
        self.get_set().get_set().remove(self)
        del self


class Family:
    def __init__(self, board, set):
        self.property = None
        self._board = board
        self.set = [set]
        self._board.get_set().append(self)

    def get_set(self):
        return self.set

    def get_board(self):
        return self._board

    def get_property(self):
        return self.property

    def set_property(self, property):
        self.property = set(property)

    def remove(self):
        """
        Delete a family in case it got enclosed.
        """
        while self.get_set():
            self.get_set()[0].remove()
        self.get_board().get_set().remove(self)
        del self

    def properties_w(self):
        property = []
        for stone in self.get_set():
            for properties in stone.properties():
                property.append(properties)
        self.set_property(property)
        if len(self.get_property()) == 0:
            self.remove()

    def merge(self, set):
        """
        Merge two families.
        Used when putting down a stone creates one family,
        connecting dwo separate ones.
        """
        for stone in set.get_set():
            stone.set_set(self)
            self.get_set().append(stone)
        self.get_board().get_set().remove(set)
        del set