# Написать программу на Python, которая заменит все пробелы, запятые и точки на двоеточие.
import re
txt =" The rain in Spain,wow"
x = re.sub('[ .,]', ':', txt, 5)
print(x)  #Функция sub() заменяет совпадения текстом по нашему выбору