import questionary
from battleship import BattleShip
from mods import Bomb
from collections import deque
import random
import subprocess

SPECIAL_MOVES = 3
SPECIAL_MOVES_STRICT = 7

def confirmInteger(incomingString):

    if incomingString.isnumeric():
        return int(incomingString)
    
    print("Select an integer please")
    return None


def playerSetup():

    name = input("Select a name:\t")
    figure = input("Select a figure to represent your ship:\t")

    p1 = BattleShip(name, figure)
    p1.printBoard()

    print("Set up your ships")

    while len(p1.getAvailableBoats()) > 0:

        print(f"Available Boat Selection: {p1.getAvailableBoats()}\n")
        
        row = input("Select starting row:\t")
        row = confirmInteger(row)
        if row is None:
            continue

        col = input("Select starting col:\t")
        col = confirmInteger(col)
        if col is None:
            continue

        boatSize = input("Select your boat size:\t")
        boatSize = confirmInteger(boatSize)
        if boatSize is None:
            continue

        orientation = questionary.select(
            "Select orientation:",
            choices=["Horizontal", "Vertical"]
        ).ask()
        horizontal = orientation == "Horizontal"

        p1.placeShip((row,col), boatSize, horizontal=horizontal)

    return p1


def regularAttack(p1, p2, row, col):
        hit = p2.isBoat(row, col)
        if hit == True:

            if p1.attack(row,col,miss=False) == True:
                print(f"{p1.getName()} Wins The Game!")
                return True
        else:
            p1.attack(row,col)
        
        return False

def play(p1, p2):
    while True:

        p1.printAttacks()
        row = input("Select attacking row:\t")
        row = confirmInteger(row)
        if row is None:
            continue

        col = input("Select attacking col:\t")
        col = confirmInteger(col)
        if col is None:
            continue


        if p1.canAttack(row, col):
            turnAmount = p1.getTurn()

            # if turnAmount % SPECIAL_MOVES == 0:
            if random.randint(1, SPECIAL_MOVES) == SPECIAL_MOVES or turnAmount % SPECIAL_MOVES_STRICT == 0:
                attackChoice = questionary.select(
                    "Choose special attack:",
                    choices=["Bomb", "Corrode"]
                ).ask()
                attackType = "b" if attackChoice == "Bomb" else "c"

                if attackType == "b":
                    print("BOOM")
                    b = Bomb((row,col))
                    placesToAttack = b.getPosToAttack()

                    for r,c in placesToAttack:
                        if p1.canAttack(r,c):
                            if regularAttack(p1, p2, r, c) == True:
                                return True
                    
                    p1.addTurn()
                    return False
                elif attackType == "c":
                    print("Audible Fart")

                    moves = [(0,1), (1,0), (0,-1), (-1,0)]
                    queue = deque()

                    queue.append((row,col))
                    visited = set()

                    while queue:
                        r, c = queue.popleft()

                        if (r,c) in visited:
                            continue

                        visited.add((r,c))

                        if not (1 <= r < p2.boardSize and 1 <= c < p2.boardSize):
                            continue

                        # if p2.isBoat(r,c) == True:
                        if p1.canAttack(r,c):
                            if regularAttack(p1, p2, r,c) == True:
                                return True
                        
                        # expand poison
                        if p2.isBoat(r,c) == True:
                            for m in moves:
                                newRow = m[0] + r
                                newCol = m[1] + c

                                queue.append((newRow, newCol))

                    p1.addTurn()
                    return False

                else:
                    continue
            else:
                p1.addTurn()
                return regularAttack(p1, p2, row, col)
        else:
            continue



while True:

    print("Starting up Game\n\n")
    print("-------------------------")

    p1 = playerSetup()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    p2 = playerSetup()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    move = 0
    while True:

        if move % 2 == 0:

            print("Player 1 Turn")

            if play(p1, p2) == True:
                break

        else:
            print("Player 2 Turn")
            if play(p2, p1) == True:
                break

        move += 1
        print("\n\n\n\n\n\n")


    subprocess.run(["xdg-open", "/home/bruno/Desktop/battleship/Battleship/skepta.gif"])
    print("-------------------------")
    print("Game has ended, Thank you for playing")





    


        
