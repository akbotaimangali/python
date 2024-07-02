# Написать программу на Python, которая сопоставляет строку, содержащую букву «a», за которой следует ноль или более букв «b».

import re

txt ="abbbbb"
x = re.search('a.*b', txt)
if x:
  print("YES! We have a match!")
else:
  print("No match")

print(x)
