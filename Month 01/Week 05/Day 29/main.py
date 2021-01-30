import csv

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        list.append(temperatures(row[1]))
        print(temperatures)

