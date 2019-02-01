
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