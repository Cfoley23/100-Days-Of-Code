# practicing list comprehension in python

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_numbers = [n+2 for n in numbers]
print(numbers)
print(new_numbers)

name = "Josephine Augustynak Williamson Queensly Troubador Harper Geraldine McGabe III"
new_list = [n for n in name]
print(new_list)

new_range = [n*2 for n in range(1,5)]
print(new_range)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(names)
print(short_names)
longer_names = [name.upper() for name in names if len(name) > 5]
print(longer_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num * num for num in numbers]
print(squared_numbers)


numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)

