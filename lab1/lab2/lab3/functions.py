def my_function():
  print("Hello from a function")

my_function()


def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")


def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")  #This function expects 2 arguments, but gets only 1:so it is error

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")


def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")



def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")



def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



def my_function(x):
  return 5 * x

print(my_function(3))
print(my_function(5))
print(my_function(9))



def my_function(x, /):
  print(x)

my_function(3)
 


def my_function(x):
  print(x)

my_function(x = 3)

def my_function(x, /):
  print(x)

my_function(x = 3) #it is not correct если добавить слеш,но попытаемся отправить ключевой аргумент то ошибка


def my_function(*, x):
  print(x)

my_function(x = 3) #функция может иметь только ключевые аргументы, если добавить*

def my_function(x):
  print(x)

my_function(3)

def my_function(*, x):
  print(x)

my_function(3)#error

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)#Любой аргумент до / является позиционным, а любой аргумент после * является ключевым словом.
