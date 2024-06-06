x = "Hello World"
print(len(x))
txt = "Hello World"
print (txt[0])
b = "Hello, World!"
print(b[:5])
b = "Hello, World!"
print(b[2:])
txt = "Hello World"
print(txt[2:5])
txt = " Hello World "
print(txt.strip())
txt = "Hello World"
print(txt.upper())
txt = "Hello World"
print(txt.lower())
txt = "Hello World"
print(txt.replace("H","J"))
age = 36
txt = "My name is John, and I am {} "
print(txt.format(age))


print("Hello")
print('Hello')
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

a = "Hello"
print(a)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
print("expensive" not in txt)

txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")

a = "Hello"
b = "World"
c = a + b
print(c)

a = "Hello"
b = "World"
c = a + " " + b
print(c)

price = 59
txt = f"The price is {price} dollars"
print(txt)

txt = f"The price is {20 * 59} dollars"
print(txt)

txt = "We are the so-called \"Vikings\" from the north."
print(txt) 
#We are the so-called "Vikings" from the north.

