#1. Write a Python program to read a file line by line and store it into a list.

f = open("D:\Python.txt", 'r')
x = []
c = f.read()
x.append(c)
print(x)
f.close()