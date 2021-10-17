import time
import os
from colorama import init, Fore, Style
from game.custom_exceptions import InputError

init()


class TicTacGame:
    """Класс, реализующий игру крестики-нолики.
    """

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


    def show_board(self):
        """Метод вывода игровой доски.
        """
        print ("----------")
        for i in range(3):
            print(
                1+i*3 if not self.board[1+i*3]
                else Fore.YELLOW + self.board[1+i*3] + Style.RESET_ALL, '|', \
                2+i*3 if not self.board[2+i*3]
                else Fore.YELLOW + self.board[2+i*3] + Style.RESET_ALL, '|',\
                3+i*3 if not self.board[3+i*3]
                else Fore.YELLOW + self.board[3+i*3] + Style.RESET_ALL
                )
            print ("----------")


    def validate_input(self, answer):
        """Метод проверки корректности ввода.

        :param answer: введенное значение
        :type answer: str
        :raises InputError: ошибка, возникающая при вводе нечислового значения
        :raises InputError: ошибка, возникающая при вводе номера несуществующей или занятой ячейки
        :return: корректное числовое значение
        :rtype: int
        """
        try:
            key = int(answer)
            if key not in self.board or self.board[key] is not None:
                raise InputError("Введенное число не входит в указанный диапазон или уже занято.")
        except ValueError:
            raise InputError("Введеное значение не является числом.")
        else:
            return key


    def start_game(self):
        """Сценарий игры.
        """
        self.welcome_players()
        time.sleep(2)
        os.system('cls||clear')
        counter = 0
        while not self.win:
            self.show_board()
            if counter % 2 == 0:
                self.make_move('X', self.player_1)
            else:
                self.make_move('O', self.player_2)
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
        """Метод, реализующий ход одного игрока.

        :param value: игровое значение, которое ставит игрок (X или O)
        :type value: str
        :param player: имя игрока
        :type player: str
        """
        while True:
            try:
                cell_number = self.validate_input(
                    input(f"{player}, ваш ход. Выберите число, куда хотите поставить {value}: ")
                )
                break
            except InputError:
                print("Вы ввели некорректное значение. Попробуйте еще раз.")
        self.board[cell_number] = value


    def welcome_players(self):
        """Метод, реализующий приветствие и знакомство с игроками.
        """
        print("Добро пожаловать в игру крестики-нолики.")
        self.player_1 = input("Введите имя первого игрока: ")
        print(f"Привет, {self.player_1}!")
        self.player_2 = input("Введите имя второго игрока: ")
        print(f"Привет, {self.player_2}!")
        print("Ну что ж, начнем игру!")


    def check_winner(self):
        """Метод, определяющий победителя.

        :return: True, если получена выигрышная комбинация и False, еслине получена
        :rtype: bool
        """
        win_combinations = ((1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7))
        for each in win_combinations:
            if self.board[each[0]] == self.board[each[1]] == self.board[each[2]] != None:
                return True
        return False
