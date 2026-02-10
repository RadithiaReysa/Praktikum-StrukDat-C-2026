#Python Sets
thisset = {"apple", "banana", "cherry"}
print(thisset)

#tidak boleh memiliki dua item dengan nilai yang sama
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

#nilai 1 = True , 0 = False
thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)

#type data
myset = {"apple", "banana", "cherry"}
print(type(myset)) #set


#Access Set
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x) #tidak bisa mengakses menggunakan index

thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)

#Add Set
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)

thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

#menambahkan objek iterable apa pun 
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)

#Remove Set
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)

thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x) #removed item
print(thisset) #the set after removal

thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

#Loop Sets
thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)

#Join Sets
#Union
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)

#Join Multiple Sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}

myset = set1.union(set2, set3, set4)
print(myset)

#Join a Set and a Tuple
x = {"a", "b", "c"}
y = (1, 2, 3)

z = x.union(y)
print(z)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#Simpan HANYA yang duplikat
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)

#Perbedaan
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3) #Simpan semua item dari set1 yang tidak ada di set2

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3) #Simpan semua item dari set1 yang tidak ada di set2

#Perbedaan Simetris
#Simpan barang-barang yang tidak ada di kedua set
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)

#Python frozenset
x = frozenset({"apple", "banana", "cherry"})
print(x)
print(type(x)) #buat sebuah objek frozensetdan periksa tipenya
