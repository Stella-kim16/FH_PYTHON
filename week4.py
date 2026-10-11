
"""
class Piece:
    def __init__(self, name, color, row, col):
        self.name = name
        self.color = color
        self.row = row
        self.col = col

    def describe(self):
        print(f"{self.color} {self.name} at ({self.row}, {self.col})")

    def can_move(self, new_row, new_col):
        return False

    def move_to(self, new_row, new_col):
        if self.can_move(new_row, new_col):
            self.row = new_row
            self.col = new_col
            print("Move successful!")
        else:
            print("Invalid move!")

        self.describe()


class Rook(Piece):
    def can_move(self, new_row, new_col):
        return self.row == new_row or self.col == new_col


class Queen(Piece):
    def can_move(self, new_row, new_col):
        row_diff = abs(new_row - self.row)
        col_diff = abs(new_col - self.col)

        return (
            self.row == new_row
            or self.col == new_col
            or row_diff == col_diff
        )


rook = Rook("Rook", "White", 0, 0)
queen = Queen("Queen", "Black", 3, 3)

rook.describe()
rook.move_to(0, 5)
rook.move_to(2, 7)

queen.describe()
queen.move_to(6, 6)
queen.move_to(5, 6)


"""




# 2 people player 
# listed in board every move -> discribe
# before the move, was asked move or finish game
# class player - name, colour, checkers, number of move, result of game, time of game
# class chenker follolw behavior of checker 
# class board - current status and array of checkes
# class game - info of player, time, number of moves 

# 게임 시작 - 플레이어의 이름과 말 색깔 결정
# 보드 출력 - 현재 체커 말 표시 
# 하얀색은 - 작은 행 번호 방향, 검은색은 큰행 번호 방향 
# 질문 출력 - 계속 또는 중지 
# 말 이동 처리 
# 게임 결과 및 요약 


import time


class Checker:
    def __init__(self, color, row, col):
        self.color = color
        self.row = row
        self.col = col

    def can_move(self, new_row, new_col):
        if self.color == "Red":
            return (
                new_row == self.row - 1
                and abs(new_col - self.col) == 1
            ) # 여기서 true 값이 나오면 바로 move 함수에서 
              # if 절로 들어가게 되고 아니면 else 로 들어가게 됨
              # row의 값도 true and col 의 값도 true 이니까! 
              # 숫자 값으로 보지말고 전 후의 좌표값으로 비교해야함 
        else:
            return (
                new_row == self.row + 1
                and abs(new_col - self.col) == 1
            )

    def move(self, new_row, new_col):
        if self.can_move(new_row, new_col):
            self.row = new_row
            # 원래 있던 값- > 새로운 값으로 움직이는것이므로 
            # self.new_row 가 아닌 self.row 가 되야함 
            self.col = new_col
            print("Move successful!")
            return True
        else:
            print("Invalid move!")
            return False


class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.move_count = 0
        self.result = "Playing"
        self.game_time = 0

    def add_move(self):
        self.move_count += 1

    def show_info(self):
        print(
            f"Player: {self.name} | "
            f"Color: {self.color} | "
            f"Moves: {self.move_count} | "
            f"Result: {self.result}"
        )


class Board:
    def __init__(self):
        self.checkers = []

    def add_checker(self, checker):
        self.checkers.append(checker)

    def get_checker(self, row, col):
        for checker in self.checkers:
            if checker.row == row and checker.col == col:
                return checker
        return None

    def show_board(self):
        print("\n  0 1 2 3 4 5 6 7")

        for row in range(8):
            print(row, end=" ")

            for col in range(8):
                checker = self.get_checker(row, col)

                if checker is None:
                    print(".", end=" ")
                elif checker.color == "Red":
                    print("R", end=" ")
                else:
                    print("B", end=" ")

            print()


class Game:
    def __init__(self):
        name1 = input("Red player name: ")
        name2 = input("Black player name: ")

        self.players = [
            Player(name1, "Red"),
            Player(name2, "Black")
        ]

        self.board = Board()

        # 간단한 예시용으로 말 두 개만 배치
        self.board.add_checker(Checker("Red", 5, 0))
        self.board.add_checker(Checker("Black", 2, 1))

        self.current_player_index = 0
        self.total_moves = 0
        self.start_time = 0
        self.finished = False

    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
        # 인덱스 값을 번갈아가면서 0,1 순서를 번갈아 줄 수 있게 해주는 코드 
        
    def finish_game(self):
        self.finished = True
        elapsed = time.time() - self.start_time

        print("\n=== GAME SUMMARY ===")
        print("Total moves:", self.total_moves)
        print(f"Game time: {elapsed:.1f} seconds")

        for player in self.players:
            player.game_time = elapsed
            player.show_info()

    def play_turn(self):
        player = self.players[self.current_player_index]

        print(f"\n{player.name}'s turn ({player.color})")
        self.board.show_board()

        choice = input("Enter m to move or q to finish: ").lower()

        if choice == "q":
            self.finish_game()
            return

        if choice != "m":
            print("Invalid choice!")
            return

        try:
            row = int(input("Current row: "))
            col = int(input("Current column: "))
            new_row = int(input("New row: "))
            new_col = int(input("New column: "))
        except ValueError:
            print("Please enter numbers.")
            return

        checker = self.board.get_checker(row, col)

        if checker is None:
            print("There is no checker at that position!")
            return

        if checker.color != player.color:
            print("That is not your checker!")
            return

        if not (0 <= new_row < 8 and 0 <= new_col < 8):
            print("Position is outside the board!")
            return

        if self.board.get_checker(new_row, new_col) is not None:
            print("That position is occupied!")
            return

        if checker.move(new_row, new_col):
            player.add_move()
            self.total_moves += 1
            self.board.show_board()
            self.switch_player()

    def start(self):
        self.start_time = time.time()

        while not self.finished:
            self.play_turn()


if __name__ == "__main__":
    game = Game()
    game.start()

