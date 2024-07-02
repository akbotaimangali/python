# Написать программу на Python, которая сопоставляет строку, содержащую букву «a» и два-три символа «b».

import re

txt = "aaaaabbbb"
match = re.search( 'a(b{2,3})', txt)
if match:
    print("ok")
else:
    print("no")