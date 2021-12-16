# Mon 13 Dec 2021 05:18:58 PM EST
# Author: Maverun
# File: solutions.py
    
"""
--- Day 8: Seven Segment Search ---

You barely reach the safety of the cave when the whale smashes into the cave mouth, collapsing it. Sensors indicate another exit to this cave at a much greater depth, so you have no choice but to press on.

As your submarine slowly makes its way through the cave system, you notice that the four-digit seven-segment displays in your submarine are malfunctioning; they must have been damaged during the escape. You'll be in a lot of trouble without them, so you'd better figure out what's wrong.

Each digit of a seven-segment display is rendered by turning on or off any of seven segments named a through g:

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

So, to render a 1, only segments c and f would be turned on; the rest would be off. To render a 7, only segments a, c, and f would be turned on.

The problem is that the signals which control the segments have been mixed up on each display. 
The submarine is still trying to display numbers by producing output on signal wires a through g, but those wires are connected to segments randomly.
Worse, the wire/segment connections are mixed up separately for each four-digit display! (All of the digits within a display use the same connections, though.)

So, you might know that only signal wires b and g are turned on, but that doesn't mean segments b and g are turned on: the only digit that uses two segments is 1,
so it must mean segments c and f are meant to be on. With just that information, you still can't tell which wire (b/g) goes to which segment (c/f).
For that, you'll need to collect more information.

For each display, you watch the changing signals for a while, make a note of all ten unique signal patterns you see, and then write down a single four digit output value (your puzzle input).
Using the signal patterns, you should be able to work out which pattern corresponds to which digit.

For example, here is what you might see in a single entry in your notes:

acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf

(The entry is wrapped here to two lines so it fits; in your notes, it will all be on a single line.)

Each entry consists of ten unique signal patterns, a | delimiter, and finally the four digit output value. Within an entry, the same wire/segment connections are used (but you don't know what the connections actually are).
The unique signal patterns correspond to the ten different ways the submarine tries to render a digit using the current wire/segment connections.
Because 7 is the only digit that uses three segments, dab in the above example means that to render a 7, signal lines d, a, and b are on.
Because 4 is the only digit that uses four segments, eafb means that to render a 4, signal lines e, a, f, and b are on.

Using this information, you should be able to work out which combination of signal wires corresponds to each of the ten digits.
Then, you can decode the four digit output value. Unfortunately, in the above example, all of the digits in the output value (cdfeb fcadb cdfeb cdbaf) use five segments and are more difficult to deduce.

For now, focus on the easy digits. Consider this larger example:

be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce

Because the digits 1, 4, 7, and 8 each use a unique number of segments, you should be able to tell which combinations of signals correspond to those digits.
Counting only digits in the output values (the part after | on each line), in the above example, there are 26 instances of digits that use a unique number of segments (highlighted above).

In the output values, how many times do digits 1, 4, 7, or 8 appear?
"""

def convertSeg(segIN,segOUT):
    segDigit = [set()]*10 #creating 10 element which is 0 - 9, i use set() instead of 0 to ignore freaking diagnostics about iterate[1] and slice thingy
    seg_5 = [] #any segment that have 5 segment only, those are gonna be filter out soon later
    seg_6 = [] # ^
    #first let find easy digit, while we do that, we will also put multi of same digit segments into ^^ list
    for s in segIN:
        length = len(s)
        #getting easy digit
        if length == 2: segDigit[1]   = set(s)
        elif length == 3: segDigit[7] = set(s)
        elif length == 4: segDigit[4] = set(s)
        elif length == 7: segDigit[8] = set(s)
        #now else check if it 5 or 6 segment
        elif length == 5: seg_5.append(set(s))
        elif length == 6: seg_6.append(set(s))
    #we are done filtering them out... now let find which one is 0,0 is in segment 6 that contains 0,6,9, while we are at it , let find 6 and 9
    #to do that, we need to do 8 - 0 and it should return 1 element, as for 6,9
    #we can find 6,9 remain by doing subtract 1, if there is 4 segment remain, then it is 9, else if it 5 segment remain, then it is 6.
    for s in seg_6:
        if len(s - segDigit[7]) == 3 and len(s - segDigit[4]) == 3: segDigit[0] = s #we found 0
        elif len(s - segDigit[7]) == 3 and len(s - segDigit[4]) == 2: segDigit[9] = s #we found 9
        elif len(s - segDigit[7]) == 4 and len(s - segDigit[4]) == 3: segDigit[6] = s #we found 6
    #now we can go ahead and find remain 2,3,5
    #if we substract 9 with others, and get one segment, that mean it is 3, put that away, and then with 4 substract remain 2,5, 2 will return 3 segment and 5 will give 2 segment...
    for s in seg_5:
        if len(s - segDigit[7]) == 3 and len(s - segDigit[4]) == 3: segDigit[2] = s #we found 2
        elif len(s - segDigit[7]) == 2 and len(s - segDigit[4]) == 2: segDigit[3] = s #we found 3
        elif len(s - segDigit[7]) == 3 and len(s - segDigit[4]) == 2: segDigit[5] = s #we found 5
    return [segDigit.index(set(x)) for x in segOUT]#we are returning segment output with index we can find


if __name__ == "__main__":
    with open('input.txt', 'r') as fp:
        data = []
        while True:
            line = fp.readline()
            if not line: break
            seg_input, seg_output = [x.strip().split(" ") for x in line.split("|")]
            data.append(convertSeg(seg_input,seg_output))

    #now for part 1, we need to find easy digit in output values, which are 1,4,7,8
    counter = 0
    total = 0
    for d in data:
        counter += d.count(1) + d.count(4) + d.count(7) + d.count(8)
        temp = ''.join(map(str,d))
        total += int(temp)


    print(f"total easy digit are {counter}")
    print(f"total output value are {total}")
