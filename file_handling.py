import os

FILE_NAME = "test_file.txt"

#writing data to file
with open(FILE_NAME,'w',encoding='utf-8') as file:
    file.write("This is PCU and AI & DS Branch\n")
    file.write("Sessions on Python from Bitcode Tech")
print("Data has been written to file")

#appending additional text to the files
with open(FILE_NAME,'a',encoding='utf-8') as file:
    file.write("\nAI & DS Branch has three classes with 180 students intake approx\n")
    file.write("Also there is a branch for AI & ML")
    file.write("\n")
print("new additional info has been appended to file")


#reading from file
try:
    with open(FILE_NAME, 'r', encoding='utf-8') as file:
        for each_line in file:
            print(each_line.strip())
except FileNotFoundError:
    print("File is missing")
