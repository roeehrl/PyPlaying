# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be: bag,hello,without,world

from helpers import commaSep, commaIn
import re

#prompt user for input & parse input
@commaIn
def prompt():
    print(f"This program prints words in a comma-separated sequence after sorting them alphabetically.")

def start():
    try:
        seq = sorted(prompt())
        print(f"\n {commaSep(seq)}")
    except Exception as e:
        print(str(e) + " exiting...")
    
if __name__ == "__main__":
    start()
  