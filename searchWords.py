import os 
import shutil

filename = input("Enter the file name")

f = open(filename)
fileline = f.readlines()

found = False

searchString=input("Enter your word you want to search")

for lines in fileline:
    words = lines.split()
    for word in words:
        if word == searchString:
            found = True

if found == True:
    print("word is present")

else:            
    print("word is not found")