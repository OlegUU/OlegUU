import random
# Цель: закрепить знания множественного наследования в Python.
# Задача "Ошибка эволюции":
# Замечали, что некоторые животные в нашем мире обладают странными и, порой, несовместимыми друг с другом свойствами? Например, утконос... Вроде есть клюв, но не птица. Вроде милый, а есть шипы на задних лапах. А ещё он откладывает яйца... Опустим факт о том, что они потеют молоком и попробуем не эволюционным способом создать нашего утконоса.
# Необходимо написать 5 классов:
class Animal: #- класс описывающий животных.
    live = True
    sound = None # звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0 #- степень опасности существа
    # Объект этого класса обладает следующими атрибутами:
    def __init__(self,speed):
        self._cords = [0, 0, 0] # координаты в пространстве.
        self.speed = speed #- скорость передвижения существа (определяется при создании объекта)
# И методами:
    def move(self, dx, dy, dz): # который должен менять соответствующие кооординаты в _cords на dx, dy и dz в том же порядке, где множетелем будет являтся speed.
        # Если при попытке изменения координаты z в _cords значение будет меньше 0, то выводить сообщение "It's too deep, i can't dive :(" , при этом изменения не вносяться.
        if self._cords[2] + dz < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords[0] += dx * self.speed
            self._cords[1] += dy * self.speed
            self._cords[2] += dz * self.speed

    def get_cords(self):#, который выводит координаты в формате: "X: <координаты по x>, Y: <координаты по y>, Z: <координаты по z>"
        print(f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}")

    def attack(self):#, который выводит "Sorry, i'm peaceful :)", если степень опасности меньше 5 и "Be careful, i'm attacking you 0_0" , если равно или больше.
        if self._DEGREE_OF_DANGER > 5:
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")

    def speak(self):#, который выводит строку со звуком sound.
        print(self.sound)
class Bird(Animal):  #- класс описывающий птиц. Наследуется от Animal.
# Должен обладать атрибутом:
    beak = True # - наличие клюва
# И методом:
    def lay_eggs(self):#, который выводит строку
        print(f"Here are(is) {random.randint(1,4)} eggs for you")
class AquaticAnimal(Animal): #- класс описывающий плавающего животного. Наследуется от Animal.
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 3

# Должен обладать методом:

    def dive_in(self, dz): #- где dz изменение координаты z в _cords. Этот метод должен всегда уменьшать координату z в _coords. Чтобы сделать dz положительным,
        # берите его значение по модулю (функция abs). Скорость движения при нырянии должна уменьшаться в 2 раза, в отличии от обычного движения. (speed / 2)
        self._cords[2] -= int(abs(dz) * (self.speed / 2))

class PoisonousAnimal(Animal): #- класс описывающий ядовитых животных. Наследуется от Animal.
    def __init__(self, speed):
        super().__init__(speed)
        self._DEGREE_OF_DANGER = 8
#
class Duckbill (Bird,AquaticAnimal,PoisonousAnimal):#- класс описывающий утконоса. Наследуется от классов Bird, AquaticAnimal, PoisonousAnimal.
    # Порядок наследования определите сами, опираясь на ниже приведённые примеры выполнения кода.
# Объект этого класса должен обладать одним дополнительным атрибутом:
    sound = "Click-click-click" #- звук, который издаёт утконос
    def __init__(self, speed):
        super().__init__(speed)


# Пример результата выполнения программы:
# Пример работы программы:

db = Duckbill(10)

print(db.live)
print(db.beak)


db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

# Вывод на консоль:
# True
# True
# Click-click-click
# Be careful, i'm attacking you 0_0
# X: 10 Y: 20 Z: 30
# X: 10 Y: 20 Z: 0
# Here are(is) 3 eggs for you # Число может быть другим (1-4)

# По итогу мы должны получить живого утконоса с клювом, атакующего и издающего странные звуки.
# После чего утконос совершает манёвры и ныряет.
# Теперь утконос в безопасности, он откладывает яйца для будущего потомства.
#
# Примечания:
#
# Будьте внимательней, когда вызываете методы классов родителей в классе наследнике при множественном наследовании: при обращении через super() методы будут искаться сначала в первом, потом во втором и т.д. классах по mro().
# При определении порядка наследования обратите внимание на то, что утконос атакует "Be careful, i'm attacking you 0_0"