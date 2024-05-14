class Player:
    def __init__(self):  # we didn't include any parameters bec name and symbol methods will exist from the methods we will be creating
        self.name = ""
        self.symbol = ""
    
    #1st method for name in Player class
    def choose_name(self):
        while True:
            name = input("Enter your name (letters only): ")  #however we won't trust that they'll obey so: 
            if name.isalpha():    #we need the "isalpha method" that returns true if a string only contains letters
                self.name = name  # if yes then save that name
                break             #we need to break the while loop to not continue forever
            print("Invalid name. Please use letters only.")    #if they didn't insert letters only we'll continue our loop till they obey

    #2nd method for symbol in Player class
    def choose_symbol(self):
        while True:
            symbol = input(f"{self.name}, choose your symbol (single letter): ")
            if symbol.isalpha() and len(symbol) == 1:
                self.symbol = symbol.upper()
                break
            print("Invalid symbol. Please choose a single letter.")

class Menu:
    def display_main_menu(self):
        print("Welcome to my X-O game!")
        print("1. Start Game")
        print("2. Quit Game")
        choice = input("Enter your choice (1 or 2): ")
        return choice
        

    def display_endgame_menu(self):
        end_menu_text = '''
        Game Over!
        1. Restart Game
        2. Quit Game
        Enter you choice (1 or 2): ''' 
        choice = input(end_menu_text)
        return choice
        
class Board:
    def __init__(self):
        self.board = [str(i) for i in range(1,10)]
        #for i in range(1,10):
        #   self.board.append(str(i))   -->["1", "2", ..."9"]
        #instead of using a for loop with 2 lines, we used a list comprehension

    def display_board(self):
        for i in range(0,9,3):   #for indexing 
            print("|".join(self.board[i:i+3]))  #taking a slice from our list of self.board with just 3 numbers in each row
            if i < 6:
                print("_"*5)
    
    def update_board(self, choice, symbol):
        if self.is_valid_move(choice):
            self.board[choice - 1] = symbol
            return True
        return False



    #helper function
    def is_valid_move(self, choice):
        return self.board[choice-1].isdigit()   #in the self.board list we store numbers as strings but in this line we want to check if they are integers, subtract 1
        #if self.board[choice-1].isdigit() == True:
        #    return True
        #instead of using the if..return we could use return directly
    
    def reset_board(self):
        self.board = [str(i) for i in range(1,10)]

class Game:
    def __init__(self):
        self.players = [Player(), Player()]   #object from Player class
        self.board = Board()                  #object from Board class
        self.menu = Menu()                    #object from Menu class
        self.current_player_index = 0   #the 1st player take an index of 0

    def start_game(self):
        choice = self.menu.display_main_menu()   #this is a method in the Menu class that display the menu txt of "welcome blabla" and giving you a choice to play or quit
        if choice == "1":
            self.setup_players()
            self.play_game()
        else:
            self.quit_game()

    def setup_players(self):
        for number, player in enumerate(self.players, start=1):
            print(f"Player {number}, enter your details")
            player.choose_name()
            player.choose_symbol()
            print("_"*20)

    #game loop, keep playing until there is a winner or tie
    def play_game(self):
        while True:
            self.play_turn()
            if self.check_win() or self.check_draw():
                choice = self.menu.display_endgame_menu()
                if choice == "1":
                    self.restart_game()
                else:
                    self.quit_game()
                    break

    
    def restart_game(self):
        self.board.reset_board()   #give us the list of digits from 1~9
        self.current_player_index = 0   #ensure that player 1 is the 1st one to play
        self.play_game()

    def check_win(self):
        win_combination = [
            [0,1,2], [3,4,5], [6,7,8],  #-> for rows
            [0,3,6], [1,4,7], [2,5,8],  #-> for cols
            [0,4,8], [2,4,6]            #-> diagonals
        ]
        for combo in win_combination:   #[0,1,2]
            if self.board.board[combo[0]] == self.board.board[combo[1]] == self.board.board[combo[2]]:
                return True
        return False

    def check_draw(self):
        return all(not cell.isdigit() for cell in self.board.board)   #every cell in the board are symbols not digits, then there is a draw

    def play_turn(self):
        player = self.players[self.current_player_index]  #to access the list of [player(), player()] which is self.players use [] 
        self.board.display_board()
        print(f"{player.name}'s turn ({player.symbol})")   #--> return: salma's turn(X)
        while True:
            try:
                cell_choice = int(input("Choose a cel (1~9): "))
                if 1 <= cell_choice <=9 and self.board.update_board(cell_choice, player.symbol):
                    break
                else:
                    print("Invalid move, try again")
            except ValueError:
                print("Please enter a number between 1 and 9")  #in case they entered a letter 
        self.switch_player()

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
        #if current player = 0 ==> 1-0 = 1
        #if current player = 1 ==> 1-1 = 0

    def quit_game(self):
        print("Thank you for playing <3")

#we create an object game from our class Game
game = Game()
game.start_game()   #used the method start_game of the class Game