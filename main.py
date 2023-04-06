"""Чуть исправленная версия"""


def game_board(NUMBERS_):
    print("-" * 13)
    for i in range(3):
        print("|", NUMBERS_[0 + i * 3], "|", NUMBERS_[1 + i * 3], "|", NUMBERS_[2 + i * 3], "|")
        print("-" * 13)


def win_condition(NUMBERS_):
    win = False
    for i in win_coord:
        if NUMBERS_[i[0]] == NUMBERS_[i[1]] == NUMBERS_[i[2]]:
            print(f"Поздравляю с победой, игрок {NUMBERS_[i[0]]}!!!!")
            win = True
            break
    return win


if __name__ == "__main__":
    NUMBERS_ = list(range(1, 10))
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    b = input("Приветствую Вас в игре крестики-нолики!\n"
              "Правила вам известны.\n"
              "Для того, чтобы начать играть введите сюда что-нибудь: ")

    game_board(NUMBERS_)

    while True:

        a = int(input("Ходит игрок X, введите номер клетки: "))
        if a in NUMBERS_:
            NUMBERS_[a - 1] = "X"
            game_board(NUMBERS_)

        if win_condition(NUMBERS_):
            break


        b = int(input("Ходит игрок O, введите номер клетки: "))

        if b in NUMBERS_:
            NUMBERS_[b - 1] = "O"
            game_board(NUMBERS_)

        if win_condition(NUMBERS_):
            break
