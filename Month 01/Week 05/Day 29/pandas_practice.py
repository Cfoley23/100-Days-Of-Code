import pandas

data = pandas.read_csv('weather_data.csv')
#print(type(data))


data_dict = data.to_dict()
print(data_dict)

temp_list = data['temp'].to_list()
print(data['temp'].mean())

temp_average = sum(temp_list) / (len(temp_list))
print(temp_average)

