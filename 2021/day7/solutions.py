# Sun 12 Dec 2021 03:51:03 PM EST
# Author: Maverun
# File: solutions.py
    
def main(raw_data):
    firstdata = {}
    seconddata = {}

    for f in raw_data:
        total = 0
        secondtotal = 0
        for x in raw_data:
            diff = abs(f-x)
            total += diff
            secondtotal += sum(range(diff+1))

        firstdata[f] = total
        seconddata[f] = secondtotal
    lowest = min(firstdata.items(),key=lambda x:x[1])
    print(lowest)
    lowest2nd = min(seconddata.items(),key=lambda x:x[1])
    print(lowest2nd)


if __name__ == "__main__":
    with open("input.txt",'r') as fp:
        data = list(map(int,fp.read().split(',')))
    main(data)
