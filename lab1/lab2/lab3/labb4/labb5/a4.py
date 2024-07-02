# Написать программу на Python для поиска последовательностей из одной заглавной буквы, за которой следуют строчные буквы.
import re
txt = "LOnDon is the capital and largest city of England, and the United Kingdom"
x = re.findall("[A-Z]{1}[a-z]+", txt)
if x:
    print("Match")
else:
    print("No match")
print(x)
