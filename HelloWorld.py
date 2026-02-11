
print("Hello World")

# variable
# Tidak perlu ditulis dulu jenis variable
var = "ganteng"
print(type(var)) # ini buat debug jenis data nya

# package 
import numpy 
from numpy import sqrt #ini impport fungsi tertentu doang
import numpy as np 
# import matplotlib.pyplot as plt #ini karna saya belum pip install matplotlib makanya cacing kuning


print(numpy.sqrt(5))

#typecasting
age = 15
age = str(age)
age2 = float(age)

print(age *2)
print(age2 *2)

#Operator
# ** itu pangkat, sisanya sama

#user input
# by defult string
name = input("input anma: ")
age = int(input("input umur: "))
print(name) 
print(age)
name = None


#if statement
a = 12
b = 5 
if (a < b):
    print("kecil", end="")
elif (b < a):
    print("besar")
else:
    print("entah")
    

#Collection 
#list (array tanpa size)
    #dinamic jadinya
iniList = [1,"aceng", 3,2]
print(iniList)

#Set 
iniSet = {"nasi", "jeruk", "ikan"}
print(iniSet)



#Dictionary

iniDict = {
    "nasi" : "ikan",
    "lau" : "nis"
}

# For loop & enum
#i otomatis dari 0 sampai 9
#range (awal, eksklusif (selalu kurang dari), step (++2, ++1))
for i in range(0,10, 2):
    print(i)

colors = ("red", "green", "blue")
#by default enum dari idx 0, kalau start = 1 mulai i nya dari 1
#kalau parameter nya 1 doang, dia jadi tuple kecil
for i, color in enumerate(colors, start = 1):
    print(i, color)
    
while i < 6:
    print(i)
    if (i == 5):
        break
    i += 1
    
    

