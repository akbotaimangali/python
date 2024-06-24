cars = ["Ford", "Volvo", "BMW"]

print(cars)


cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

print(x)


cars = ["Ford", "Volvo", "BMW"]

cars[0] = "Toyota"

print(cars)


cars = ["Ford", "Volvo", "BMW"]

x = len(cars)

print(x)
#Note: Длина массива всегда на единицу больше максимального индекса массива.

cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)


cars = ["Ford", "Volvo", "BMW"]

cars.append("Honda")

print(cars)


cars = ["Ford", "Volvo", "BMW"]

cars.pop(1)

print(cars)


cars = ["Ford", "Volvo", "BMW"]

cars.remove("Volvo")

print(cars)


fruits = ["apple", "banana", "cherry"]

fruits.append("orange")

print(fruits)


a = ["apple", "banana", "cherry"]

b = ["Ford", "BMW", "Volvo"]

a.append(b)

print(a) #[[]]


fruits = ["apple", "banana", "cherry"]

fruits.clear()

print(fruits) #[]



fruits = ["apple", "banana", "cherry"]

x = fruits.count("cherry")

print(x)


points = [1, 4, 2, 9, 7, 8, 9, 3, 1]

x = points.count(9)

print(x)


fruits = ['apple', 'banana', 'cherry']

cars = ['Ford', 'BMW', 'Volvo']

fruits.extend(cars)

print(fruits) #add


fruits = ['apple', 'banana', 'cherry']

points = (1, 4, 5, 9)

fruits.extend(points)

print(fruits) #add


fruits = ['apple', 'banana', 'cherry']

x = fruits.index("cherry")

print(x)  #находим индекс

fruits = [4, 55, 64, 32, 16, 32]

x = fruits.index(32)

print(x) #находим индекс


fruits = ['apple', 'banana', 'cherry']

fruits.insert(1, "orange")

print(fruits) 


fruits = ['apple', 'banana', 'cherry']

fruits.pop(1)

print(fruits)


fruits = ['apple', 'banana', 'cherry']

x = fruits.pop(1)

print(x)


fruits = ['apple', 'banana', 'cherry']

fruits.reverse()

print(fruits)


cars = ['Ford', 'BMW', 'Volvo']

cars.sort()

print(cars)



cars = ['Ford', 'BMW', 'Volvo']

cars.sort(reverse=True)

print(cars)


# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(key=myFunc)

print(cars)



def myFunc(e):
  return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]

cars.sort(key=myFunc)

print(cars)



# A function that returns the length of the value:
def myFunc(e):
  return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort(reverse=True, key=myFunc)

print(cars)





