# Mon 06 Dec 2021 11:06:57 PM EST
# Author: Maverun
# File: solutions.py
original_boards = []
locations = {} #we will find where is board for this number etc,
rng = []

class LocationBoard:
    def __init__(self,boardNumer,row,column) -> None:
        self.done = False
        self.boardNumber = boardNumer
        self.row = row
        self.column = column

class Board:
    def __init__(self,board,number) -> None:
        self.board = board
        self.number = number
        self.score = 0
        self.done = False


def printA(a):
    for row in a:
        print(row)

def importData(data):
    data = data.split('\n')
    rng = list(map(int,data.pop(0).split(',')))
    data.pop(0) #remove new line new before the board.
    holder = []
    counter_board = 0
    counter_row = -1 
    while(len(data)):
        counter_row += 1
        d = data.pop(0)
        if d != '':
            d = list(map(int,d.split()))
            for index,element in enumerate(d):
                l = LocationBoard(counter_board,counter_row,index)
                if locations.get(element): locations[element].append(l)
                else: locations[element] = [l]
            holder.append(list(map(int,d)))
        else:
            counter_board += 1
            counter_row = -1 
            b = Board(holder,counter_board)
            original_boards.append(b)
            holder = []
    return original_boards,rng


def checkWinner(board,row,column):
    if board[row].count(-1) == len(board[row]): return True
    columnboard = [x[column] for x in board]
    return columnboard.count(-1) == len(columnboard)

def getScore(board):
    total = 0
    for row in board:
        for column in row:
            if column != -1: total += column
    return total

def firstPart():
    boards = original_boards[:]
    #so we will start from left to right for chosen number obviously, and we need to find which board is first to reached bingo
    # location contain chosen number with rowIndex and column Index
    for chosenNumber in rng:
        listBoards = locations[chosenNumber]
        for board in listBoards:
            boards[board.boardNumber].board[board.row][board.column] = -1
            if checkWinner(boards[board.boardNumber].board,board.row,board.column): 
                # board.done =True
                score = getScore(boards[board.boardNumber].board)
                return board.boardNumber + 1, score * chosenNumber
    return None,None


def secondPart():
    # boards = [row[:]for row in original_boards]
    boards = original_boards[:]
    done_board = []
    current_board = 0
    #so we will start from left to right for chosen number obviously, and we need to find which board is first to reached bingo
    # location contain chosen number with rowIndex and column Index
    for chosenNumber in rng:
        listBoards = locations[chosenNumber]
        for board in listBoards:
            if board.done or board.boardNumber in done_board: 
                continue
            boards[board.boardNumber].board[board.row][board.column] = -1
            if checkWinner(boards[board.boardNumber].board,board.row,board.column): 
                board.done =True
                done_board.append(board.boardNumber)
                current_board += 1
                if len(boards) == current_board:
                    score = getScore(boards[board.boardNumber].board)
                    return board.boardNumber + 1, score * chosenNumber
    print("NONE FOUND!")
    return None,None



def main():
    result,score = firstPart()
    print(result,score)
    print("now checking second part")
    result1,score1 = secondPart()
    print(result1,score1)

    pass


if __name__ == "__main__":
    with open('input.txt') as fp: raw_data = fp.read()
    test_input ="""\
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""
    original_boards,rng = importData(raw_data)
    main()
