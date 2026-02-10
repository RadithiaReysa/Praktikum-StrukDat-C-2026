#Python Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple)

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

thistuple = ("apple",)
print(type(thistuple))
#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))

#Access Tuple
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) #dimulai dari awal

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) #dimulai dari akhir

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

#update tuples
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
#Remove Items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

#unpack Tuples
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

#Jika jumlah variabel kurang dari jumlah nilai
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

#Loop Tuples
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#menggunakan while loop
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
  print(thistuple[i])
  i = i + 1

#Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#menggandakan tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

