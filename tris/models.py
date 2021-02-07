CROSS = "x"
CIRCLE = "o"
DRAW = "="


class Player:
    def __init__(self, name, symbol):
        self.score = 0
        self.name = name
        self.symbol = symbol
    
    def __str__(self):
        return f"Player {self.name} has {self.symbol}"


class Grid:
    def __init__(self):
        self.grid = None
        self.tot_inserts = 9
        self.curr_inserts = 0
        self.grid_size = 3
        self.clear()

    def __str__(self):
        return "|" + "|\n|".join(["|".join(row) for row in self.grid]) + "|"

    def clear(self):
        self.curr_inserts = 0
        self.grid = [[" "]*self.grid_size, [" "]*self.grid_size, [" "]*self.grid_size]

    def check_tris(self):
        for i in range(self.grid_size):
            row_els = self.grid[i]
            col_els = (self.grid[j][i] for j in range(self.grid_size))
            for els in (row_els, col_els):
                els = list([el for el in els if el.strip()])
                if len(els) < 3:
                    continue
                if len(set(els)) == 1:
                    return els[0]

    def insert_at(self, nrow, ncol, symbol):
        if (
            nrow < 0 or nrow >= self.grid_size or 
            ncol < 0 or ncol >= self.grid_size or
            self.grid[nrow][ncol] != " "
        ):
            return 0
        self.grid[nrow][ncol] = symbol
        self.curr_inserts += 1
        tris = self.check_tris()
        if tris is not None:
            return 1
        if self.curr_inserts == self.tot_inserts:
            return 2


class Tris:
    def __init__(self, p1_name, p2_name):
        p1 = Player(p1_name, CROSS)
        p2 = Player(p2_name, CIRCLE)
        self.player1 = p1
        self.player2 = p2
        self.playing_player = p1
        self.grid = Grid()

    def new_game(self, p1_name=None, p2_name=None):
        if p1_name is not None and p1_name != self.player1.name:
            self.player1 = Player(p1_name, CROSS)
        if p1_name is not None and p2_name != self.player2.name:
            self.player2 = Player(p2_name, CIRCLE)
        self.grid.clear()

    def play_turn(self, nrow, ncol):
        res = self.grid.insert_at(nrow, ncol, self.playing_player.symbol)
        if res is None:
            if self.playing_player == self.player1:
                self.playing_player = self.player2
            else:
                self.playing_player = self.player1
        elif res == 0:
            return False
        elif res == 1:
            self.playing_player.score += 1
            return self.playing_player
        elif res == 2:
            return DRAW
        