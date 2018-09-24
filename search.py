class Node():
    children = []

    def __init__(self):
        self.visited = False
    
    def addChild(self, child, cost):
        self.children.append((child, cost))
    def getChildren(self):
        return self.children
    def openNode(self):
        self.visited = True
        return self.children


class chessBoard():
    boardState = [[True, False, False, False, False, False, False, False],
              [False, False, False, False, True, False, False, False],
              [False, True, False, False, False, False, False, False],
              [False, False, False, False, False, True, False, False],
              [False, False, True, False, False, False, False, False],
              [False, False, False, False, False, False, True, False],
              [False, False, False, True, False, False, False, True],
              [False, False, False, False, False, False, False, False]] 
    boardScore = 0

    def __init__(self):
        self.calcScore()

    #Calculate the amount of columns/rows with more than one queen
    def calcScore(self):

        #Loop through rows
        for y in range(8):
            queens = 0
            for x in range(8):
                if(self.boardState[y][x]):
                    queens += 1
            if(queens > 1): #if there are more than one queen, increase score by amount of excess queens
                self.boardScore += queens - 1 

        #Loop through columns
        for x in range(8):
            queens = 0
            for y in range(8):
                if(self.boardState[y][x]):
                    queens += 1
            if(queens > 1):
                self.boardScore += queens -1

        return self.boardScore

    def solveBoard(self):
        #Loop through columns
        for x in range(8):
            queens = 0
            for y in range(8):
                if(self.boardState[y][x]):
                    queens += 1
            if(queens > 1):
                
