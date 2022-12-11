#module for redundant operations
import re

def commaSep(seqList:list[str]) -> str:
    filtered = list(filter(None,seqList))
    commaStr = ','.join(str(val) for val in filtered)
    return commaStr

def commaIn(func):
    def inner():
        func()
        rawSequence = input("Please enter a comma seperated sequence. Hit enter to submit: \n\n")
        if rawSequence:
            #strip whitespaces (if exist) and commas and resolve into list
            seqList = re.split(r'[ ,\s]\s*',rawSequence)
            return seqList
        else:
            raise Exception("No value was entered.")
    
    return inner

#decorator to for multiline prompt
def prompt(func):
    def inner():
        func()
        log = []
        print("To submit hit enter again. \n")
        while True:
                user_input = input()
                # if user pressed Enter without a value, break out of loop
                if user_input == '':
                    break
                else:
                    log.append(user_input)

        return log
    
    return inner


#decorator to check integrity of entered amount
def checkIntegrity(func):
    def inner(obj, sum):
        try:
            sum = int(sum)
            return func(obj, sum)
        except:
            raise Exception("Unable to read given input. Please make sure to enter a positive integer.") 
    return inner