# Написать программу на Python для поиска последовательностей строчных букв, соединенных подчеркиванием.
import re

txt = "deep_learningmodel or machine_learning"
match = re.findall("[a-z]+\_+[a-z]",  txt)  #	Сигнализирует о специальной последовательности 
if match:
    print("Match")
else:
    print("No match")
print(match)
