# You are required to write a program to sort the (name, age, height) tuples by ascending order 
# where name is string, age and height are numbers. 
# The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.
# The priority is that name > age > score.
# If the following tuples are given as input to the program:
# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85
# Then, the output of the program should be:
# [('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

from dataclasses import astuple, dataclass
from helpers import prompt
import re

#dataclass decorator helps creating iterable data store objects sortable ascending prioratized by property order 
@dataclass(order=True)
class Person:
    name: str
    age :int
    height: int

@dataclass
class People:
    people: list[Person]

    #override existing dataclass init method.
    def __init__(self,log):
        self.people = []
        if(log):
            for line in log:
                seqList = re.split(r'[ ,\s]\s*',line)
                filtered = list(filter(None,seqList))
                if len(filtered)>2:
                    if filtered[1].isnumeric() and filtered[2].isnumeric():
                        self.people.append(Person(filtered[0],filtered[1],filtered[2]))
                    else:
                        raise Exception("non numeric inputs were given.")
                else:
                        raise Exception("non numeric inputs were given.")
        else:
            raise Exception("Bad input.")
        
        #sorting the people list by creteria stated above
        self.people.sort()
    #return a resolved list of sorted Person tuples
    def getPeopleTuples(self):
        return [astuple(item) for item in self.people]


@prompt
def prompt():
    print("This programm sorts tuples of people represnted by name, age & height.")
    print("Please enter a comma seperated sequence to represent a person. One sequence at a line. \n")


def start():
    try:
        people = People(prompt())
        print(people.getPeopleTuples())
    except Exception as e:
        print(str(e) + " exiting...")


if __name__ == "__main__":
    start()

    
   
        


