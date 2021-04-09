import re

class formatting:
    def __init__(self, string):
        self.string = string
        self.list = []

    def lower(self):
        for i in self.string:
            if i.islower():
                print(i)

    def upper(self):
        for i in self.string:
            if i.isupper():
                print(i)

    def lowerall(self):
        for i in self.string:
            if i.isupper():
                self.list.append(i.lower())
            else:
                self.list.append(i)
        return self.list
    
a = formatting("HellO")
print(a.lowerall())

