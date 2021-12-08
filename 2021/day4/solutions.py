# Mon 06 Dec 2021 11:06:57 PM EST
# Author: Maverun
# File: solutions.py
original_boards = []
locations = {} #we will find where is board for this number etc,
rng = []

def printA(a):
    for row in a:
        print(row)

def importData(data):
    data = data.split('\n')
    rng = list(map(int,data.pop(0).split(',')))
    data.pop(0) #remove new line new before the board.
    holder = []
    # print(data)
    counter_board = 0
    counter_row = -1 
    while(len(data)):
        counter_row += 1
        d = data.pop(0)
        print(d)
        if d != '':
            d = list(map(int,d.split()))
            for index,element in enumerate(d):
                #storing them as #Board, index(column)
                if locations.get(element): locations[element].append([counter_board,counter_row,index])
                else: locations[element] = [[counter_board,counter_row,index]]
            # d = [-1 if rng.count(x) else x for x in map(int,d.split())]
            # print(d)
            holder.append(list(map(int,d)))
        else:
            counter_board += 1
            counter_row = -1 
            original_boards.append(holder)
            holder = []
    return original_boards,rng


def checkWinner(board,row):
    if board[row].count(-1) == len(board[row]): return True
    columnboard = [x[row] for x in board]
    return columnboard.count(-1) == len(columnboard)

def getScore(board):
    total = 0
    for row in board:
        for column in row:
            if column != -1: total += column
    return total

def firstPart():
    boards = [row[:]for row in original_boards]
    # printA(boards)
    #so we will start from left to right for chosen number obviously, and we need to find which board is first to reached bingo
    # location contain chosen number with rowIndex and column Index
    # print(rng,boards)
    # print(locations)
    for chosenNumber in rng:
        listBoards = locations[chosenNumber]
        # print(chosenNumber,listBoards)
        for boardNumber,row,column in listBoards:
            # print(row,column,boardNumber)
            # print(boards[boardNumber],row,column)
            boards[boardNumber][row][column] = -1
            if checkWinner(boards[boardNumber],row): 
                print('found the boards',boardNumber + 1)
                score = getScore(boards[boardNumber])
                print(score)
                return boardNumber + 1, score * chosenNumber
    print("NONE FOUND!")
    return None,None




def main():
    result,score = firstPart()
    print(result,score)
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
