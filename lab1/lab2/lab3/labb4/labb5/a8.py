#Напишите программу на Python для разбиения строки по заглавным буквам.
import re
txt = "Red, GlaSs, PRETTY"
result = re.split(r'(?=[A-Z])', txt)
print(result)
# ?=[A-Z] это позитивный просмотр вперед (positive lookahead). Это означает, что разделение будет происходить в позиции перед символом, который соответствует шаблону [A-Z].