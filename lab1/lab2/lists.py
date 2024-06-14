thislist = ["apple", "banana", "cherry"]
print(thislist)


thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)


thislist = ["apple", "banana", "cherry"]
print(len(thislist))


list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


list1 = ["abc", 34, True, 40, "male"]

print(list1)


mylist = ["apple", "banana", "cherry"]

print(type(mylist))


thislist = list(("apple", "banana", "cherry"))
print(thislist)


thislist = ["apple", "banana", "cherry"]
print(thislist[1])


thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")


#change list
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"

print(thislist)


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]

thislist[1:3] = ["blackcurrant", "watermelon"]

print(thislist)


thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)


thislist = ["apple", "banana", "cherry"]

thislist[1:3] = ["watermelon"]

print(thislist)


thislist = ["apple", "banana", "cherry"]

thislist.insert(2, "watermelon")

print(thislist) #Чтобы вставить новый элемент списка, не заменяя ни одно из существующих значений, мы можем использовать метод insert().


thislist = ["apple", "banana", "cherry"]

thislist.append("orange")

print(thislist) #To add an item to the end of the list, use the append() method:


thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)


thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)

print(thislist) #To append elements from another list to the current list, use the extend() method.


thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")

thislist.extend(thistuple)

print(thislist) 


thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) #delete


thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  #delete



thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort()

print(thislist)#по алфавитному порядку


thislist = [100, 50, 65, 82, 23]

thislist.sort()

print(thislist) #по возрастанию


thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]

thislist.sort(reverse = True)

print(thislist)#для сортировки по убыванию


thislist = [100, 50, 65, 82, 23]

thislist.sort(reverse = True)

print(thislist)


thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort()

print(thislist) #заглавные буквы первые


thislist = ["banana", "Orange", "Kiwi", "cherry"]

thislist.sort(key = str.lower)

print(thislist) #маленькие буквы первые отсортируются
