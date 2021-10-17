import time
import os
from game.custom_exceptions import InputError
from colorama import init
init()
from colorama import Fore, Style

class TicTacGame:

    def __init__(self):
        self.board = {
            1: None,
            2: None,
            3: None,
            4: None,
            5: None,
            6: None,
            7: None,
            8: None,
            9: None,
        }
        self.player_1 = None
        self.player_2 = None
        self.win = False
        self.win_combination = None
    
    def show_board(self):
         print ("----------")
         for i in range(3):
             print(1+i*3 if not self.board[1+i*3] else Fore.YELLOW + self.board[1+i*3] + Style.RESET_ALL, '|', \
                 2+i*3 if not self.board[2+i*3] else Fore.YELLOW + self.board[2+i*3] + Style.RESET_ALL, '|',\
                 3+i*3 if not self.board[3+i*3] else Fore.YELLOW + self.board[3+i*3] + Style.RESET_ALL)
             print ("----------")
        
    
    def validate_input(self, answer):
        try:
            x = int(answer)
            if x not in self.board or self.board[x] is not None:
                raise InputError("Введенное число не входит в указанный диапазон или уже занято.")
        except ValueError:
            raise InputError("Введеное значение не является числом.")
        else:
            return x
     

    def start_game(self):
        self.welcome_players()
        time.sleep(2)
        os.system('cls||clear')
        counter = 0
        while not self.win:
            self.show_board()
            if counter % 2 == 0:
                cell_number = self.make_move('X', self.player_1)
                self.board[cell_number] = 'X'
            else: 
                cell_number = self.make_move('O', self.player_2)
                self.board[cell_number] = 'O'
            self.win = self.check_winner()
            counter += 1
            if counter == 9:
                self.show_board()
                print(Fore.RED + "Ничья!")
                break
        else:
            self.show_board()
            print(Fore.GREEN + "Вы выиграли!")
            
        
    def make_move(self, value, player):
        while True:
                try:
                    cell_number = self.validate_input(input("{}, ваш ход. Выберите число, куда хотите поставить {}: ".format(player, value)))
                    break
                except InputError:
                    print("Вы ввели некорректное значение. Попробуйте еще раз.")
        return cell_number


    def welcome_players(self):
        print("Добро пожаловать в игру крестики-нолики.")
        self.player_1 = input("Введите имя первого игрока: ")
        print("Привет, {}!".format(self.player_1))
        self.player_2 = input("Введите имя второго игрока: ")
        print("Привет, {}!".format(self.player_2))
        print("Ну что ж, начнем игру!")

    def check_winner(self):
        win_combinations = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
        for each in win_combinations:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]] != None:
                return True
        return False