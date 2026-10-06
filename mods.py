class Bomb:
    def __init__(self, center):

        moves = [(-1,-1), (1,1), (-1,1), (1,-1), (0,1), (1,0), (0,-1),(-1,0)]
        self.posToAttack = [(center[0], center[1])]

        for m in moves:
            row, col = center
            newPos = (row+m[0], col+m[1])
            self.posToAttack.append(newPos)


    def getPosToAttack(self):
        return self.posToAttack


    