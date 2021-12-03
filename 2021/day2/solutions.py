# Thu 02 Dec 2021 11:42:14 PM EST
# Author: Maverun

# Note that since you're on a submarine, down and up affect your depth,
# and so they have the opposite result of what you might expect.

# The submarine seems to already have a planned course (your puzzle input).
# You should probably figure out where it's going. For example:

# forward 5
# down 5
# forward 8
# up 3
# down 8
# forward 2

# Your horizontal position and depth both start at 0.
# The steps above would then modify them as follows:

#     forward 5 adds 5 to your horizontal position, a total of 5.
#     down 5 adds 5 to your depth, resulting in a value of 5.
#     forward 8 adds 8 to your horizontal position, a total of 13.
#     up 3 decreases your depth by 3, resulting in a value of 2.
#     down 8 adds 8 to your depth, resulting in a value of 10.
#     forward 2 adds 2 to your horizontal position, a total of 15.

# After following these instructions, you would have a horizontal position of 15 and a depth of 10.
# (Multiplying these together produces 150.)

# def clean_data(raw_input):
    
def clean_data(data):
    d = data.split()
    return d[0],int(d[1])

def firstPart(raw_data):
    horizontal = depth = 0
    for data in raw_data:
        movement, unit = data
        if movement == 'forward': horizontal += unit
        elif movement == 'up': depth -= unit
        elif movement == 'down': depth += unit
    result = horizontal * depth
    print("first part: total distance is ",result)

def secondPart(raw_data):
    horizontal = depth = aim = 0
    for data in raw_data:
        movement, unit = data
        if movement == 'forward':
            horizontal += unit
            depth += unit * aim
        elif movement == 'up': aim -= unit
        elif movement == 'down': aim += unit
    result = horizontal * depth
    print("second part: total distance is ",result)

def main(raw_data):
    firstPart(raw_data)
    secondPart(raw_data)
    pass


if __name__ == "__main__":
    with open('input.txt') as fp: raw_data = fp.readlines()
    test_input =[
"forward 5",
"down 5",
"forward 8",
"up 3",
"down 8",
"forward 2"]
    raw_data  = list(map(clean_data,raw_data))
    main(raw_data)
