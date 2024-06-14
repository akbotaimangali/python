fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 



for x in range(6):
  print(x)  #Note that range(6) is not the values of 0 to 6, but the values 0 to 5.



for x in range(2, 6):
  print(x) 


for x in range(2, 30, 3):
  print(x) 



adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)



