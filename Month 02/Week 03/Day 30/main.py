# filenotfounderror
# with open("a_file.txt", "r") as file:
#     file.read()

#one method of handling the filenotfounderror
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["not_found"])
except FileNotFoundError:
    file = open("a_file.txt", "a")
    file.write("This is a new sentence.\n")
except KeyError as error_message:
    print(f"The {error_message} Does Not Exist")
else:
    content = file.read()
    print(content)
finally:
    raise TypeError("This is an error that I made up.")
    file.close()
    print("File Closed")


# nonexistantkeyerror
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existent key"]


#indexoutofrangeerror
# fruit_list = ["Apples", "Bananas", "Oranges"]
# fruit = fruit_list[3]

#typeerror
# text = "abc"
# print(text + 5)
