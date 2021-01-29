file = open('/Users/colin/Desktop/my_file.txt')
contents = file.read()
print(contents)
file.close()

# This method of opening and reading a file automatically closes it once the function is performed
# with open('my_file.txt') as file:
#     contents = file.read()
#     print(contents)

# with open('this_is_a_new_file.txt', mode='w') as file:
#     file.write('\nNew text')
