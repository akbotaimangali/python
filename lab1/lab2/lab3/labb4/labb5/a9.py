# Написать программу на Python для вставки пробелов между словами, начинающимися с заглавных букв.
import re

str ="Tomorrow afternoonI wIll make soup"
x = re.sub(r"([A-Z])", r" \1", str)
print(x) ##Функция sub() заменяет совпадения текстом по нашему выбору