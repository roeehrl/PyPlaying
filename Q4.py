# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
# 1. At least 1 letter between [a-z]
# 2. At least 1 number between [0-9]
# 1. At least 1 letter between [A-Z]
# 3. At least 1 character from [$#@]
# 4. Minimum length of transaction password: 6
# 5. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.

from helpers import commaIn,commaSep
import re

RE_CRETERIA = r'^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#@$]).{6,13}$'

@commaIn
def prompt():
    print("This program checks the validity of password inputs\naccording to these criterias: ")
    print("""
    1. At least 1 letter between [a-z]
    2. At least 1 number between [0-9]
    1. At least 1 letter between [A-Z]
    3. At least 1 character from [$#@]
    4. Minimum length of transaction password: 6
    5. Maximum length of transaction password: 12
    """)

# returns list of strings adehering to regular expression criteria
def evaluate(passList:list[str]) -> list[str]:
    allowedPasses = [x for x in passList if re.fullmatch(RE_CRETERIA,x)] 
    return allowedPasses
    

def start():
    passList = prompt()
    print("\n" +commaSep(evaluate(passList)))


if __name__ == "__main__":
    start()

