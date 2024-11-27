from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        direction = 1 if self.color == 'white' else -1
        # Pěšák se může posunout pouze vpřed, nebere žádné figury
        move_forward = (row + direction, col)
        if self.is_position_on_board(move_forward):
            return [move_forward]
        return []

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy střelce.
        Střelec se může pohybovat diagonálně.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        
        # Čtyři diagonály: čtyři směry
        for i in range(1, 8):
            moves.extend([
                (row + i, col + i), (row + i, col - i),
                (row - i, col + i), (row - i, col - i)
            ])
        
        # Filtrujeme tahy mimo šachovnici
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy věže.
        Věž se může pohybovat horizontálně a vertikálně.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        
        # Horizontální a vertikální pohyby
        for i in range(1, 8):
            moves.extend([
                (row + i, col), (row - i, col),
                (row, col + i), (row, col - i)
            ])
        
        # Filtrujeme tahy mimo šachovnici
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy dámy.
        Dáma se může pohybovat horizontálně, vertikálně a diagonálně.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = []
        
        # Všechny pohyby jako věž a střelec
        for i in range(1, 8):
            moves.extend([
                (row + i, col), (row - i, col),
                (row, col + i), (row, col - i),
                (row + i, col + i), (row + i, col - i),
                (row - i, col + i), (row - i, col - i)
            ])
        
        # Filtrujeme tahy mimo šachovnici
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy krále.
        Král se může pohybovat o jedno pole ve všech směrech.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 1, col), (row - 1, col),
            (row, col + 1), (row, col - 1),
            (row + 1, col + 1), (row + 1, col - 1),
            (row - 1, col + 1), (row - 1, col - 1)
        ]
        
        # Filtrujeme tahy mimo šachovnici
        return [move for move in moves if self.is_position_on_board(move)]

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())
    
    # Příklad pro další figury
    pawn = Pawn("white", (2, 2))
    print(pawn)
    print(pawn.possible_moves())
    
    bishop = Bishop("black", (4, 4))
    print(bishop)
    print(bishop.possible_moves())
    
    rook = Rook("white", (1, 1))
    print(rook)
    print(rook.possible_moves())
    
    queen = Queen("black", (5, 5))
    print(queen)
    print(queen.possible_moves())
    
    king = King("white", (7, 7))
    print(king)
    print(king.possible_moves())
