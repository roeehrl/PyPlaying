# Write a program that computes the net amount of a bank account
# based a transaction log from console input. The transaction log format is shown as following:
# D 100
# W 200

from helpers import prompt, checkIntegrity

#prompt the user for input and returns transaction log required for construction of a bank account

@prompt
def prompt():
    print("""Please enter transaction log. 
    Enter action specifier letter (D/W) followed by a white space and a positive integer.
    Use one line for each action, hit enter to log action as shown in the following format: \n
    D 100 
    W 50 \n
    *expected result is 50* \n""")
   

#bank account object
class Account:

    def __init__(self, log):
        """Initializes a new account accoriding to provided log."""
        self._total = 0
        self._log = log
        self.logParser()

#defining withdrawl and depoist methods
    @checkIntegrity
    def withdraw(self, sum):
        self._total -= sum

    @checkIntegrity
    def deposit(self, sum):
        self._total += sum

#overwiting self description to show net amount
    def __str__(self):
        return str(self._total) + "\n"

#Account object helper method to parse account's log and manipulate account accoridingly
    def logParser(self) -> None:
        #log might be empty
        if self._log:
            for line in self._log:
                #stripping white spaces for execution integrity
                line = line.replace(" ", "")
                #Evaluate action needed. using switch statement for minimizing runtime
                match line[0]:
                    case 'D':
                        self.deposit(line[1:])
                    case 'W':
                        self.withdraw(line[1:])
                    case _:
                        raise Exception("A non-permitable action was entered.")
                        
        else:
            raise Exception("log is empty.")



#execution start point
def start():
    print("This program computes the net amount of a bank account based on a transaction log\n")
    try:
        #construct bank account object only after obtaining user input
        acc = Account(prompt())
        #show net amount of well constructed account
        print(acc)

    except Exception as e:
        print(str(e) + " exiting...")
    


if __name__ == "__main__":
    start()
