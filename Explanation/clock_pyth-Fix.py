import time
import os

class Clock:

    #this is the python constructor
    #if you need to initialize class or instance variables
    #an __init__ method should be created
    #python runs this method automatically on the objects creation
    def __init__(self):
        #self is the current object reference
        #adding self in front of variables in a class turns them into instance variables
        self.myTime = []
        #array append takes one arguement, you had two
        #now, there is one arguement which is a Counter object
        #you were also calling append on an element of the array rather than the whole array
        #by doing myTime[index].append(x)
        #here we just want to "push" an element onto the array, so it should be called directly onto myTime
        self.myTime.append(Counter("Sec", 60))
        self.myTime.append(Counter("Min", 60))
        self.myTime.append(Counter("Hrs", 24))
        self.myTime.append(Counter("Days", 7))


    #myTime is an instance variable so no need to pass it to the method
    def IncrementClockSec(self):
        #in python, advanced for loops get the element itself, not the index
        #if you want to loop for every element in a list, with the index being the control variable,
        #use the code below
        #use len(x) instead of x.length() in python
        #none of this really made sense so here is a working implementation
        for counterIndex in range(0, len(self.myTime)):

            if self.myTime[counterIndex].name == "Sec":
                self.myTime[counterIndex].Increment()

            if self.myTime[counterIndex].count == self.myTime[counterIndex].maxnum:

                self.myTime[counterIndex].Reset()

                #calling self.myTime[i+1] would be an index error if we were at the end of the array
                if self.myTime[counterIndex].name != "Days":

                    self.myTime[counterIndex+1].Increment()

    #see line 25                              
    def DrawClock(self):
        combined = ""
        #this counts backwards from the last index to 0
        #look at the range documentation at https://www.pythoncentral.io/pythons-range-function-explained/
        for i in range (len(self.myTime)-1, -1, -1):
            if i == len(self.myTime)-1:
                #idk what the :D2 was for so i took it out
                #https://docs.python.org/3.4/library/string.html
                combined += str.format("{:01d}", self.myTime[i].count)
            else:
                combined += str.format(":{:01d}", self.myTime[i].count)

        #no semi-colons in python
        return combined

class Counter:

    #see line 6
    def __init__(self, name, maxnum):
        self.name = name
        self.count = 0
        self.maxnum = maxnum

    def Increment(self):
        self.count += 1

    def Reset(self):
        #integer so 00 === 0
        self.count = 0

#clears console   
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


#no reason for main to be a class as it has no instance methods/variables
#Defined as a function instead
def main():
    #python time.sleep takes seconds, not milliseconds like most other languages' time modules
    # https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/
    Sleeper = 0.1
    maxLength = 86410 * 7
    
    myClock = Clock()

    print(myClock.DrawClock())

    for i in range(0, maxLength):
        time.sleep(Sleeper)
        cls()
        myClock.IncrementClockSec()
        print(myClock.DrawClock())


#__name__ is an inate property in any python program
#if __name__ is equal to __main__, we know this python file was run directly
#rather than imported as a module
#if this file is imported as a module, we don't want the clock to start automatically
#we just want its classes and functions available to the other file calling the module

if __name__ == "__main__":
    main()

        

    


