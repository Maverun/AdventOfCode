# Thu 02 Dec 2021 09:38:01 PM EST
# Author: Maverun


# This report indicates that, scanning outward from the submarine, the sonar sweep found depths of 199, 200, 208, 210, and so on.

# The first order of business is to figure out how quickly the depth increases,
# just so you know what you're dealing with - you never know if the keys will get carried into deeper water by an ocean current or a fish or something.

# To do this, count the number of times a depth measurement increases from the previous measurement.
# (There is no measurement before the first measurement.)

test_input = [199,200,208,210,200,207,240,269,260,263]

with open('input.txt') as f:
    raw_data = list(map(int,f.readlines()))
# raw_data = test_input

def firstpart():
    total = 0
    prev =  raw_data[0]
    for x in raw_data:
        total += x > prev
        prev = x

    print("the total is ", total)

# Start by comparing the first and second three-measurement windows.
#The measurements in the first window are marked A (199, 200, 208); their sum is 199 + 200 + 208 = 607. 
# The second window is marked B (200, 208, 210); its sum is 618. 
# The sum of measurements in the second window is larger than the sum of the first,
# so this first comparison increased.
def secondpart():
    #we do not need to use letter, we can just do this with 2D array
    total = 0
    #what we will do is that we will add element to counter, and if firstcounter is past 2,
    #then element will also add to second, once first counter is 3 we will then put it in data and pass second to 
    prev = sum(raw_data[0:3])
    for i in range(1,len(raw_data)):
        current = sum(raw_data[i:i+3])
        total += current > prev
        prev = current

    print(f"total is {total}")

def main():
    firstpart()
    secondpart()

if __name__ == "__main__":
    main()
