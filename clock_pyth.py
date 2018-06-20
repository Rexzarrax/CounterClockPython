import time
import os


class Clock:
    @staticmethod
    def clocksetup(self):
        mytime = []
        mytime[0].append("Sec", 60)
        mytime[1].append("Min", 60)
        mytime[2].append("Hrs", 24)
        mytime[3].append("Days", 7)

    @staticmethod
    def incrementclocksec(self, mytime):
        for i in Counter:
            if mytime[i].Name == "Sec":
                mytime[i].Increment()

            if mytime[i].Count >= mytime[i].Maxnum:
                mytime[i].Reset()
                if i + 1 != mytime.Length:
                    mytime[i + 1].Increment()

    def drawclock(self, mytime):
        combined = ""
        for i in range(0, mytime.Length):
            if i == mytime.Length - 1:
                combined += str.format("{0:D2}", mytime[i].Count)
            else:
                combined += str.format(":{0:D2}", mytime[i].Count)

        return self.combined


class Counter:
    _name = ""
    _count, _maxnum = 0

    def append(self, name, maxnum):
        self._name = name
        self._count = 0
        self._maxnum = maxnum

    def Increment(self):
        _count += 1

    def Reset(self):
        _count = 00


class Program:
    @staticmethod
    def main(self):
        sleeper = 1000
        maxlength = 86410 * 7

        myclock = Clock().ClockSetup()

        print(myclock.DrawClock())

        for i in range(0, maxlength):
            time.sleep(sleeper)
            cls()
            myclock.IncrementClockSec()
            print(myclock.DrawClock())
        s = input()
        print(s)


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
