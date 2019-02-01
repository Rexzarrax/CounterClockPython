from counter import Counter
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