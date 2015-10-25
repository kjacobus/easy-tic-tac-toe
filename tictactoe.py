class tictactoe:

    def __init__(self):
        self.items = [[0 for idx in range(3)] for idx in range(3)]
        
    def show_game(self):
        #create list of Xs and Os to print
        xs_and_os = []
        for row_i in range(len(self.items)):
            for col_i in range(len(self.items[row_i])):
                if self.items[row_i][col_i] == 1:
                    xs_and_os.append("X")
                elif self.items[row_i][col_i] == -1:
                    xs_and_os.append("O")
                else:
                    xs_and_os.append(" ")
        #print Xs and Os in grid
        for idx in range(9):
            if not idx % 3 == 2:
                print(str(xs_and_os[idx]) + " | ", end = "")
            elif idx != 8:
                print(str(xs_and_os[idx]))
                print(" -  -  - ")
            else:
                print(str(xs_and_os[idx]))
        
    def numb_plays(self):
        neg_size = 0
        for row_i in range(len(self.items)):
            for col_i in self.items[row_i]:
                if col_i == 0: neg_size += 1
        return 9 - neg_size
        
    def is_won(self):
        if self.numb_plays() < 3: return False
        for row_i in range(len(self.items)):
            #check rows
            if abs(sum(self.items[row_i])) == 3:
                return True
        #create transposed list
        board_t = []
        board_t = list(map(list, zip(*self.items)))
        for col_i in range(len(board_t)):
            #check columns
            if abs(sum(board_t[col_i])) == 3:
                return True
        #check diagonals        
        right_to_left_diag = []
        left_to_right_diag = []
        for idx in range(3):
            right_to_left_diag.append(self.items[idx][idx])
            left_to_right_diag.append(self.items[(idx + 2) % 3][(idx + 2) % 3])

        if abs(sum(right_to_left_diag)) == 3:
            return True
        if abs(sum(left_to_right_diag)) == 3:
            return True
                
        return False
    
    def who_won(self):
        if self.who_plays() == 1:
            return "O"
        else:
            return "X"
        
    def is_over(self):
        if self.is_won() or self.numb_plays() >=9: return True
        else: return False
            
    def who_plays(self):
        #if not self.is_won():
        return (-1) ** (self.numb_plays() % 2)
            
    def who_plays_x_o(self):
        if self.who_plays() == -1:
            return "O"
        else:
            return "X"
        
    def play(self, row_idx, col_idx):
        if not self.is_over():
            if self.items[row_idx][col_idx] == 0:
                self.items[row_idx][col_idx] = self.who_plays()
            else:
                print("Space already played; please play again")
        else:
                print("Game is_over; please play again")

        

    def game_play(self):
            allowable = range(0,3)
            row_desire = None
            column_desired = None
            while not game.is_over():
                game.show_game()
                print(game.who_plays_x_o() + " turn")
                
                while True:
                    row_desired = input("Which row would you like to play? ")
                    if int(row_desired) in allowable:
                        break
                while True:
                    column_desired = input("Which column would you like to play? ")
                    if int(column_desired) in allowable:
                        break
                          

                game.play(int(row_desired),int(column_desired))
        

        

playing = True

print("Welcome to a simple tic-tac-toe game")

while playing:

    game = tictactoe()
    game.game_play()
    game.show_game()
    
    if game.is_won():    
        print(game.who_won() + " wins!")
    else:
        print("Cat's game. Try again")
    
    playagain=input("Play again?" )
    if "N" in playagain.upper():
        playing = False
    
#    print(f.numb_plays())
#    print(f.is_won())
#game.play(1,1)

#game.play(0,1)
"""game.play(0,0)
game.play(1,0)
game.play(1,1)
game.play(2,1)
game.play(2,2)
game.play(0,2)
f.show_game()"""

