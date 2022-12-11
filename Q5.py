# Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

#
class Div7:
    DO_DIV = 7
    
    #objects need min, max range to initialize
    def __init__(self, min ,max):
        self.max = max
        self.min = min
        self.pos = self.defineStart()

    def defineStart(self):
        if self.min % self.DO_DIV == 0:
            return self.min
        i = self.min
        while(i < self.min + self.DO_DIV):
            if i % self.DO_DIV == 0:
                return i
            i += 1            
        
    #implementaion of iterable interface

    def __iter__(self):
        return self

    def __next__(self):
        if self.pos <= self.max:
            if self.pos % self.DO_DIV == 0:
                result = self.pos
                self.pos += self.DO_DIV
            return result
        else:
            raise StopIteration


    #another option for iterating is a generator 
    #this is redundant! because we already implented iterable interface
    #but just for practice 

    def generator(self):
        self.pos = self.defineStart()
        while self.pos <= self.max:
            yield self.pos
            self.pos += self.DO_DIV



def start():
    print ("This programm print numbers, which are divisible by 7 \n")
    print("using an intereable class acting as a generator \n")

    #creating div7 iterable object
    myIter = Div7(6, 80)
    
    #showing iteration capabilities
    for item in myIter:
        print(item)

    #showing use of generator 
    for item in myIter.generator():
        print(item)


if __name__ == "__main__":
    start()
