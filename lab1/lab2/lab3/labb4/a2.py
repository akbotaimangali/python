#Даты Python Дата в Python не является самостоятельным типом данных, но мы можем импортировать модуль с именем datetime для работы с датами как объектами date.

import datetime

x = datetime.datetime.now()

print(x) #2024-06-28 04:36:59.342394

#x.strftime — это метод, используемый для форматирования объектов даты и времени в Python(директивы)
import datetime

x = datetime.datetime.now()

print(x.year)
print(x.strftime("%A")) #Friday



import datetime

x = datetime.datetime(2020, 5, 17)

print(x) #2020-05-17 00:00:00


import datetime

x = datetime.datetime(2018, 6, 1)

print(x.strftime("%B")) #June



import datetime

x = datetime.datetime.now()

print(x.strftime("%a")) #короткая версия день недели Fri


import datetime

x = datetime.datetime.now()

print(x.strftime("%A")) #День недели, полная версия #Friday


import datetime

x = datetime.datetime.now()

print(x.strftime("%w")) #Будний день в виде числа 0-6, 0 - воскресенье output 5 because today is Friday


import datetime

x = datetime.datetime.now()

print(x.strftime("%d")) #какой сегодня день 28 


import datetime

x = datetime.datetime.now()

print(x.strftime("%b"))  #Название месяца, краткая версия Jun


import datetime

x = datetime.datetime.now()

print(x.strftime("%B")) #	Название месяца, полная версия June



import datetime

x = datetime.datetime.now()

print(x.strftime("%m")) #Месяц в виде числа 06


import datetime

x = datetime.datetime.now()

print(x.strftime("%y")) #Год, сокращенная версия, без столетия 24


import datetime

x = datetime.datetime.now()

print(x.strftime("%Y")) #	Год выпуска, полная версия 2024


import datetime

x = datetime.datetime.now()

print(x.strftime("%p")) #PM or AM  AM because it is morning now 


import datetime

x = datetime.datetime.now()

print(x.strftime("%M")) #Минута 


import datetime

x = datetime.datetime.now()

print(x.strftime("%j")) #Номер дня в году 001-366   180day today


import datetime

x = datetime.datetime.now()

print(x.strftime("%U")) #Номер недели в году, воскресенье как первый день недели, 00-53  it is 25


import datetime

x = datetime.datetime(2018, 5, 31)

print(x.strftime("%W")) #Номер недели в году, понедельник как первый день недели, 00-53  it is 22


import datetime

x = datetime.datetime.now()

print(x.strftime("%c")) #Thu Jun 27 23:49:05 2024   	Локальная версия даты и времени


import datetime

x = datetime.datetime.now()

print(x.strftime("%x")) #Локальная версия даты  28.06.2024

import datetime

x = datetime.datetime.now()

print(x.strftime("%X")) #Локальная версия времени  04:42:29 












