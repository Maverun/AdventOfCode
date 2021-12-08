# Sat 04 Dec 2021 07:24:25 PM EST
# Author: Maverun
"""
The submarine has been making some odd creaking noises, so you ask it to produce a diagnostic report just in case.

The diagnostic report (your puzzle input) consists of a list of binary numbers which, when decoded properly, can tell you many useful things about the conditions of the submarine.
The first parameter to check is the power consumption.

You need to use the binary numbers in the diagnostic report to generate two new binary numbers (called the gamma rate and the epsilon rate).
The power consumption can then be found by multiplying the gamma rate by the epsilon rate.

Each bit in the gamma rate can be determined by finding the most common bit in the corresponding position of all numbers in the diagnostic report.
For example, given the following diagnostic report:

00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010

Considering only the first bit of each number, there are five 0 bits and seven 1 bits.
Since the most common bit is 1, the first bit of the gamma rate is 1.

The most common second bit of the numbers in the diagnostic report is 0, so the second bit of the gamma rate is 0.

The most common value of the third, fourth, and fifth bits are 1, 1, and 0, respectively, and so the final three bits of the gamma rate are 110.

So, the gamma rate is the binary number 10110, or 22 in decimal.

The epsilon rate is calculated in a similar way; rather than use the most common bit, the least common bit from each position is used. So, the epsilon rate is 01001, or 9 in decimal.
Multiplying the gamma rate (22) by the epsilon rate (9) produces the power consumption, 198.

Use the binary numbers in your diagnostic report to calculate the gamma rate and epsilon rate, then multiply them together.
What is the power consumption of the submarine? (Be sure to represent your answer in decimal, not binary.)
"""

"""
Based on what I understood, count of all 0 and 1 in first column, highest count is 1, so add one for gamma and so on..
"""

def firstpart(raw_input):
    #since we are dealing with binary, so better to do them in the strings then convert to decimal later.
    gamma = epsilon = ''
    #we will iterate each of them and then we will count bit each, sadly this might be end up o(n^2)
    for i in range(len(raw_input[0])):
        one = sum(1 for x in raw_input if x[i] == '1')
        zero = sum(1 for x in raw_input if x[i] == '0')
        if one == zero and one == 0: break
        gamma += f"{int(one > zero)}"
        epsilon += f"{int(zero > one)}"

    gamma = int(gamma,2)
    epsilon = int(epsilon,2)
    print(gamma,epsilon,gamma * epsilon)
    pass


#there is better way to merge them into one but I am so lazy... meh.
def recOxy(oldData,pos):
    if len(oldData) == 1: return int(oldData[0],2)
    one = sum(1 for x in oldData if x[pos] == '1')
    zero = sum(1 for x in oldData if x[pos] == '0')
    result = '1' if one > zero else '0'
    if one == zero: result = '1'
    newData = [x for x in oldData if x[pos] == result]
    return recOxy(newData,pos+1)

def recCo2(oldData,pos):
    if len(oldData) == 1: return int(oldData[0],2)
    one = sum(1 for x in oldData if x[pos] == '1')
    zero = sum(1 for x in oldData if x[pos] == '0')
    result = '0' if one > zero else '1'
    if one == zero: result = '0'
    newData = [x for x in oldData if x[pos] == result]
    return recCo2(newData,pos+1)

def secondPart(raw_input):
    oxy = recOxy(raw_input,0)
    co2 = recCo2(raw_input,0)
    print(oxy,co2,oxy * co2)


def main(raw_input):
    firstpart(raw_input)
    secondPart(raw_input)


if __name__ == "__main__":
    with open('input.txt') as fp: raw_data = fp.readlines()
    test_input =[
"00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010",
]
    main(raw_data)

