class House:
    def __init__ (self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self,new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range ( 1, new_floor + 1 ):
                print(floor)
        else:
            print('Такого этажа не существуе')

    def __len__(self):
                return self.number_of_floors

    def __str__(self):
                return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __eq__(self, other):
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == otherb

    def __lt__(self, other):
        if isinstance(other.number_of_floors, int) and isinstance(other, House):
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if isinstance(value, int):
            self.number_of_floors = self.number_of_floors + value
        return self
        
    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        if isinstance(value, int):
            self.number_of_floors += value
        return self

# Пример выполняемого кода:

h1 = House('ЖК Эльбрус', 10)

h2 = House('ЖК Акация', 20)



print(h1)

print(h2)



print(h1 == h2) # __eq__



h1 = h1 + 10 # __add__

print(h1)

print(h1 == h2)



h1 += 10 # __iadd__

print(h1)



h2 = 10 + h2 # __radd__

print(h2)



print(h1 > h2) # __gt__

print(h1 >= h2) # __ge__

print(h1 < h2) # __lt__

print(h1 <= h2) # __le__

print(h1 != h2) # __ne__



# Вывод на консоль:
#
# Название: ЖК Эльбрус, кол-во этажей: 10
#
# Название: ЖК Акация, кол-во этажей: 20
#
# False
#
# Название: ЖК Эльбрус, кол-во этажей: 20
#
# True
#
# Название: ЖК Эльбрус, кол-во этажей: 30
#
# Название: ЖК Акация, кол-во этажей: 30
#
# False
#
# True
#
# False
#
# True
#
# False
#
