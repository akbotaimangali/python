#Написать программу на Python для преобразования заданной строки в стиле Camel в стиле Snake.

import re
snake = "London _is_ the _capital_ and _largest_ city _of _England, _and_ the_ United_ Kingdom"
camel = snake.replace('_', '')
camel = camel.upper()

print(camel)