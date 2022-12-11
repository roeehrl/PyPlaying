# Write a program to compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.
# Suppose the following input is supplied to the program:
# New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
# Then, the output should be: 2:2
# 3.:1
# 3?:1
# New:1
# Python:5 
# Read:1 
# and:1 
# between:1 
# choosing:1 
# or:2
# to:1

import re
from collections import Counter

def prompt():
    print("This programm computes the frequency of words from the input. the output is diaplayed alphanumerically \n")
    rawSequence = input("Please enter a sequence\n\n")
    if rawSequence:
        #strip whitespaces and resolve into list
        seqList = re.split(r'[ \s]\s*',rawSequence)
        return seqList
    else:
        raise Exception("No value was entered.")

def start():
    #ask for input and parse into list of strings delimited by whitespaces
    seqList = prompt()
    #use Counter object to retrieve tuples keyed by string an valued occurence in list
    counted = Counter(seqList)
    for key, value in (sorted(counted.items())):
        print(f"{key}:{value}")
    

if __name__ == "__main__":
    start()
