import pandas

# data = pandas.read_csv('weather_data.csv')
# print(type(data))

#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data['temp'].to_list()
# print(temp_list)
# # get the average temp for the week
# print(data['temp'].mean())
# # get the maximum value under the temp series(column)
# print(data.temp.max())
#
# # way to calculate the average without PANDAS
# temp_average = sum(temp_list) / (len(temp_list))
# print(temp_average)
#
# # Get data in columns
# print(data['condition'])
# # you can also get the data this way
# print(data.condition)

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
#
# monday_temp_f = monday_temp * 9 / 5 + 32
# print(monday_temp_f)

# Create a DataFrame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data2 = pandas.DataFrame(data_dict)
#
# data2.to_csv('new_data.csv')

#
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])
cinammon_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinammon_squirrel_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrel_count, cinammon_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
# my longer solution
#gray = 0
# black = 0
# cinnamon = 0
# fur_color = data["Primary Fur Color"]
# for color in fur_color:
#     if color == 'Gray':
#         gray += 1
#     elif color == 'Black':
#         black += 1
#         continue
#     else:
#         if color == "Cinnamon":
#             cinnamon += 1
#             continue

# print(gray)
# print(black)
# print(cinnamon)
# total_squirrels = gray + cinnamon + black
# print(fur_color)
# print(total_squirrels)

