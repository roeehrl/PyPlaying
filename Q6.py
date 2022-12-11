#A robot moves in a plane starting from the original point (0,0).
#The robot can move  UP, DOWN, LEFT and RIGHT with given steps
#Please write a program to compute the distance from current position after a sequence of movement and original point. 
#If the distance is a float, then just print the nearest integer.
#as the following example: 
# UP 5
# DOWN 3 
# LEFT 3 
# RIGHT 2
# The output of the program should be: 2

from helpers import prompt
from enum import Enum
import math

#define enum of valid actions
class Actions(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

#define point in plate object
class Point:

        def __init__(self, x=0, y=0):
            self._x = x
            self._y = y

        def distance(self,other) -> float:
            x,y = other.raw()
            return math.sqrt(math.pow((x - self._x),2)  +  math.pow((y - self._y),2))
        
        def raw(self):
            return (self._x,self._y)

# define robot object 
class Robot:

    ACTIONS = [m.name for m in Actions]

    #instruction list is required to construct a robot object
    def __init__(self,instructions:list[str]):
        self.startPos = Point()
        self.allowedActions = self.ACTIONS
        self.instructions = instructions
        try:
            self.checkIntegrity()
        except Exception as e:
            raise e
            
    #object helper method called from main to retrieve distance from start point and latest point
    def getDistance(self):
        return round(self.move().distance(self.startPos))

    #move robot to latest point (shorcuting the sequence)
    def move(self):
        x,y = self.startPos.raw()

        for item in self.log:
            match item[0]:
                case "UP":
                    y += item[1]
                case "DOWN":
                    y -= item[1]
                case "RIGHT":
                    x += item[1]
                case "LEFT":
                    x -= item[1]
        return Point(x,y)
        
    #called from constructor to create move log from instructions list to be used by the move action
    def checkIntegrity(self):
        self.log = []
        for line in self.instructions:
            splitLine = line.strip().split()
            if(splitLine[0] in self.allowedActions):
                if splitLine[1].replace(" ","").isnumeric():
                    self.log.append( (splitLine[0],int(splitLine[1])))
                else:
                    raise Exception("input is not a number.")
            else:
                raise Exception("unallowed action specified")

@prompt
def prompt():
    print("This program computes the distance from current position after a sequence of movements and original point (0,0)")
    print("""Please enter the trace of robot movement as shown in the following: \n
            UP 5
            DOWN 3
            LEFT 3 
            RIGHT 2 \n""")
    
                
def start():
    instructions = prompt()
    try:
        r = Robot(instructions)
        print(r.getDistance())
    except Exception as e:
        print(str(e) + " Exiting...")
   

if __name__ == "__main__":
    start()

    
   

   