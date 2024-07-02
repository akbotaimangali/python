#Написать программу на Python, которая сопоставляет строку, содержащую букву «a», за которой следует любая буква, заканчивающаяся на «b».
import re
txt = "sdfghjkqawertyb"
x = re.search('a.*b$', txt)
if x:
    print("Match")
else:
    print("No match")
print(x)