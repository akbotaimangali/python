

#Итератор-обьект,который поддерживает функцию next () и помнит о том, какой элемент будет браться следующим
#Списки, кортежи, словари и наборы - все это итеративные объекты. Это итеративные контейнеры, из которых вы можете получить итератор.

#Все эти объекты имеют iter() метод, который используется для получения итератора:
s = [1, 2, 3]
d= iter(s)

print(next(d))
print(next(d))
print(next(d))


#Строки также являются итерируемыми объектами, содержащими последовательность символов:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

b=(i**2 for i in range (1,6))
for i in b:
  print (i) #генераторы можем обойти только один раз

mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)


mystr = "banana"

for x in mystr:
  print(x)


#Метод __iter__() действует аналогично, вы можете выполнять операции (инициализацию и т.д.), но всегда должны возвращать сам объект итератора.

#Метод __next__() также позволяет выполнять операции и должен возвращать следующий элемент в последовательности.
class MyNumbers:
  def __iter__(self):
    self.a = 2
    return self

  def __next__(self):
    x = self.a
    self.a += 2
    return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
