import time
import os

class Clock:

    def __init__(self):
        #set up the list which holds the counter objects
        self.myTime = []
        self.myTime.append(Counter("Sec", 60))
        self.myTime.append(Counter("Min", 60))
        self.myTime.append(Counter("Hrs", 24))
        self.myTime.append(Counter("Days", 7))


    #select a counter in increment/reset
    def IncrementClockSec(self):
        for counterIndex in range(0, len(self.myTime)):

            if self.myTime[counterIndex].name == "Sec":
                self.myTime[counterIndex].Increment()

            if self.myTime[counterIndex].count == self.myTime[counterIndex].maxnum:

                self.myTime[counterIndex].Reset()

                #calling self.myTime[i+1] would be an index error if we were at the end of the array
                if self.myTime[counterIndex].name != "Days":

                    self.myTime[counterIndex+1].Increment()
                             
    def DrawClock(self):
        combined = ""
        #this counts backwards from the last index to 0
        for i in range (len(self.myTime)-1, -1, -1):
            if i == len(self.myTime)-1:
                combined += str.format("{:02d}", self.myTime[i].count)
            else:
                combined += str.format(":{:02d}", self.myTime[i].count)

        return combined

class Counter:
    #set intial values of the objects
    def __init__(self, name, maxnum):
        self.name = name
        self.count = 0
        self.maxnum = maxnum

    #increment the count by one
    def Increment(self):
        self.count += 1

    #reset count to 0 
    def Reset(self):
        self.count = 0

#clears console   
def cls():
    os.system('cls' if os.name=='nt' else 'clear')


#program entry point
def main():
    #Set the time per increment and the maximum length the clock will run for
    Sleeper = 0.1
    maxLength = 86410 * 7

    myClock = Clock()

    print(myClock.DrawClock())

    for i in range(0, maxLength):
        time.sleep(Sleeper)
        cls()
        print("Python Clock")
        myClock.IncrementClockSec()
        print(myClock.DrawClock())

if __name__ == "__main__":
    main()

        

    


