# filenotfounderror
# with open("a_file.txt", "r") as file:
#     file.read()

#one method of handling the filenotfounderror
try:
    file = open("a_file.txt")
except:
    file = open("a_file.txt", "w")


# nonexistantkeyerror
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existent key"]


#indexoutofrangeerror
# fruit_list = ["Apples", "Bananas", "Oranges"]
# fruit = fruit_list[3]

#typeerror
# text = "abc"
# print(text + 5)
