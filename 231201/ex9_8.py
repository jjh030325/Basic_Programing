class Counter:
    def __init__(self, number = 0):
        self.__number = number
        if self.__number >= 100 or self.__number<=-1:
            self.__number = 0
    def reset(self):
        self.__number = 0
    def inc(self):
        self.__number += 1
        if self.__number >= 100:
            self.__number = 0
    def dec(self):
        self.__number -= 1
        if self.__number <= -1:
            self.__number = 0
    def __str__(self):
        return "C({})".format(self.__number)
    
c1 = Counter(10)
c1.inc()
print('c1 =', c1)

c2 = Counter()
c2.inc()
c2.inc()
c2.dec()
print("c2 =", c2)
c2.reset()
print("c2 =", c2)