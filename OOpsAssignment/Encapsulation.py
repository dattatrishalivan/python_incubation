class Encap:
    def __init__(self, name, age, add):
        self.name=name
        self._age=age
        self.__add=add
e=Encap("datta", 34, "hyderabad")
print(e.name)
print(e._age)
print(e._Encap__add)


