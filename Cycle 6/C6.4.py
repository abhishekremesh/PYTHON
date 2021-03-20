#4.Write a Python program to read specific columns of a given CSV file and print the content  of the columns.

import csv

f =open('D:\csv.csv','r')
c=csv.reader(f)
for row in c:
    print(row)


