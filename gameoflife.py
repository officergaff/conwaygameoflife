import random
import time 
import os

R = 50
C = 110
game = [[random.randint(0, 1) for _ in range(C)] for _ in range(R)]

def print_game(game):
    for r in range(R):
        for c in range(C):
            if game[r][c] == 0: print(".", end=" ")
            else: print("\033[91m@\033[0m", end=" ")
        print("")
    # print("-"*(C*2-1))

def next(game: list[list[int]]) -> list[list[int]]:
    next_game = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        for c in range(C):
            count = check_neighbors(game, r, c)
            if game[r][c] == 1:
                if count < 2:
                    next_game[r][c] = 0
                elif count < 4:
                    next_game[r][c] = game[r][c]
                else: next_game[r][c] = 0
            else:
                if count == 3: next_game[r][c] = 1
    return next_game

def check_neighbors(game, r, c):
    count = 0
    for y in range(r-1, r+2):
        if 0 <= y < R:  
            for x in range(c-1, c+2):
                if 0 <= x < C:
                    count += game[y][x]
    if game[r][c] == 1: count -= 1
    return count

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print_game(game)
    game = next(game)
    input()
