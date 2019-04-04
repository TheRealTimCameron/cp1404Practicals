import random

NUMBERS_PER_LINE = 6
MINIMUM_NUM = 1
MAXIMUM_NUM = 45


def main():
    quick_pick_amount = int(input("How many quick picks? "))
    while quick_pick_amount <= 0:
        print("Number must be > 0")
        quick_pick_amount = int(input("How many quick picks? "))

    for i in range(quick_pick_amount):
        quick_pick_board = []
        for j in range(NUMBERS_PER_LINE):
            number = random.randint(MINIMUM_NUM, MAXIMUM_NUM)
            while number in quick_pick_board:
                number = random.randint(MINIMUM_NUM, MAXIMUM_NUM)
            quick_pick_board.append(number)
        quick_pick_board.sort()
        print(" ".join("{}".format(number) for number in quick_pick_board))


main()
