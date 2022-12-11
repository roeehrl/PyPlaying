# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of
# 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line

from helpers import commaSep

LOW_RANGE, HIGH_RANGE = 2000, 3200
DO_DIV = 7
DONT_DIV = 5

#find first divisible by 7
def defineStart():
    i = LOW_RANGE
    while (i < LOW_RANGE + DO_DIV):
        if i % DO_DIV == 0:
            return i
        i += 1


def start():
    print(
        f"This program displays all number divisble by {DO_DIV} but are not a multiple of {DONT_DIV} between {LOW_RANGE} & {HIGH_RANGE}. \n")
    # find first number divisible by 7
    start = LOW_RANGE if LOW_RANGE % DO_DIV == 0 else defineStart()
    # creating list of numbers adehering to the conditions stated. No need to check divisbilty by 7 because step is always 7 from first 7-divisble integer.
    numberStack = [i for i in range(start, HIGH_RANGE+1, DO_DIV) if (i % DONT_DIV != 0)] 
    # conversion to user friendly string
    stackStr = commaSep(numberStack)

    print(stackStr)


if __name__ == "__main__":
    start()
