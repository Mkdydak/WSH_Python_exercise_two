### LIST COMPREHENSION ###
# ZADANIE 1
names = ['Ada', 'Bill', 'Yen', 'Geralt', 'Ksawery', 'Candice', 'Esmeralda']

name_lenghts = [len(x) for x in names]
print(name_lenghts)

names_upper = [x.upper() for x in names]
print(names_upper)

# ZADANIE 2
radii = [12.1, 33, 9.3, 0.2, 190, 22.5]
pi = 3.14
circle_areas = []

circle_areas = [(pi * x ** 2) for x in radii]

print(circle_areas)

# ZADANIE 3
discounts = [19, 21, -5.5, 7.8, 13.1, -10.2, -21, 10.1]
discounts_checked = []

discounts_checked =[0 if x < 0 else x for x in discounts]

print(discounts_checked)

### METODY ###
# ZADANIE 1
import random
doggos = ['Bubba', 'Joey', 'Thor', 'Milo', 'Chester', 'Simba', 'Buddy']

def random_doggo(input_list):
    random_name = random.choice(input_list)
    return random_name

print(random_doggo(doggos))

# ZADANIE 2
def greater_of_pair(a,b):
    if a > b:
        return a
    else:
        return b

print(greater_of_pair(3,2))

def average_of_3(a, b, c):
    return (a + b + c) / 3

print(average_of_3(2,5,5))

# ZADANIE 3
list_1 = ['Bubba', 'Joey', 'Thor', 'Milo', 'Chester', 'Simba', 'Buddy']
list_2 = [12.1, 33, 9.3, 0.2, 190, 22.5]
list_3 = [3, 5]
list_4 = ['Piłka']
list_5 = [2]
list_6 = []

def margins(input_list):
    if len(input_list) > 1:
        input_list_value_first = input_list[0]
        input_list_value_last = input_list[-1]
        return print(input_list_value_first, input_list_value_last)
    elif len(input_list) == 1:
        return print(input_list[0], None)
    else:
        return print(None, None, str('List is empty!'))

margins(list_6)

### KLASY ###
#ZADANIE 1
class Player:
    def __init__(self, name, age, goals):
        self.name = name
        self.age = age
        self.goals = goals

    @property
    def get_name(self):
        return self.name

    @property
    def set_name(self, name):
        self.name = name

    @property
    def get_age(self):
        return self.age

    @property
    def set_age(self, age):
        self.age = age

    @property
    def get_goals(self):
        return self.goals

my_player = Player('David Beckham', 23, 6)

print(my_player.name, my_player.age, my_player.goals)

def score():
    my_player.goals += 1
    return print(my_player.name, str('strzelił gola!, ma na koncie:'), my_player.goals)
score()