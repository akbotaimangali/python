#модуль - это то же самое, что библиотека кода.

#Файл, содержащий набор функций, которые мы хотим включить в свое приложение.

import mymodule

mymodule.greeting("Akbota")



import mymodule1

a = mymodule1.person1["age"]
print(a)   ##Мы можем назвать файл модуля как нам угодно, но он должен иметь расширение файла .py


import mymodule3 as mx

a = mx.person1["name"]
print(a) #Мы можемм создать псевдоним при импорте модуля, используя ключевое слово as вызываемого mx:

from mymodule2 import person1

print(person1["age"]) ##Мы можем импортировать только части из модуля, используя ключевое слово from .

#Модуль с именем mymodule имеет одну функцию и один словарь:

#Модули в Python используются для организации и структурирования кода, 
# а также для повышения его повторного использования и читаемости. 
# Они позволяют вам разбить ваш код на отдельные файлы и компоненты, 
# что облегчает его поддержку и масштабирование.