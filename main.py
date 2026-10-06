from battleship import BattleShip
from mods import Bomb
from collections import deque

SPECIAL_MOVES = 2

def confirmInteger(incomingString):

    if incomingString.isnumeric():
        return int(incomingString)
    
    print(print("Select an integer please"))
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

        horizontal = input("Horizontal?: Ans with (y or n)\t")
        if horizontal == "y":
            horizontal = True
        elif horizontal == "n":
            horizontal = False
        else:
            print("Please select either y or n")
            continue

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

            if turnAmount % SPECIAL_MOVES == 0:
                print("Choose bomb or corrode hit")
                attackType = input("Select (b, c):\t")

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


                        if p2.isBoat(r,c) == True:
                            if p1.canAttack(r,c):
                                if regularAttack(p1, p2, r,c) == True:
                                    return True
                            
                            # expand poison
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

    print("-------------------------")
    print("Game has ended, Thank you for playing")





    


        
