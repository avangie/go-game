
from assets.constans import BLACK, WHITE





class Board(object):
    def __init__(self):
        """
        Create and initialize a board.
        """
        self._next_player = BLACK
        self._stones = []

    def player(self):
        return self._next_player
    
    def set_next_player(self, player):
        self._next_player = player
    
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
        if point not in self.stones():
            self._stones.append(point)
            
        
        


class Stone:
    def __init__(self, color, coordinates, board):
        """
        Create and initialize a stone.
        Coordinates argument is a tuple, ie. (0,0) represents 
        upper left corner of the board.
        Color argument is a color of the stone - white or black.
        
        """
        self._color = color
        self._coordinates = coordinates
        self._board = board

    def remove_stone(self):
        pass


    
