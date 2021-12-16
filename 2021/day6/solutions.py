# Sat 11 Dec 2021 02:41:21 PM EST
# Author: Maverun
# File: solutions.py

import numpy as np
from collections import deque


def readData(file):
    with open(file,'r') as fp:
        return fp.read().split(',')

    # return np.loadtxt(file,delimiter=',')

def countFish(fish,day):

    for i in range(day):
        # print(f"After {i + 1} day(s): {fish}")
        #let check if there is any fish that is day 0, then we will add them to day 6, reset day 0,birth new... then iterate loops,
        #actually let just do branchless, if statement slow things down. we will do day 7, since day 7 will be come 6 in a second.
        fish[7] += fish[0]
        fish.append(fish[0]) # 9 that will become 8 before end of the day.. cuz i am confuse you right now lol
        fish[0] = 0
        fish.rotate(-1)
        fish.pop() #remove day 9 that become day 0, so we dont mix up.



    print(sum(fish))

def main(file):
    data = list(map(int,readData(file)))
    data = deque(sum(1 for x in data if x == day) for day in range(9))
    countFish(data.copy(),80)
    countFish(data.copy(),256)
    pass



if __name__ == "__main__":
    main('input.txt')
