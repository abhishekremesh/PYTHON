#3. Write a Python program to read each row from a given csv file and print a list of strings.

f = open("D:\\csv.csv" , 'r')

c = f.readlines()

list = list(c)

print(list)
f.close()