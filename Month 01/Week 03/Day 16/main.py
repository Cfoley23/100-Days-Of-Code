# from turtle import Turtle, Screen
#
# timmy = Turtle()
# my_screen = Screen()
# timmy.shape("turtle")
# timmy.color("green")
# timmy.fd(100)
# timmy.lt(90)
# timmy.fd(100)
# timmy.rt(90)
# timmy.bk(100)
# timmy.rt(90)
# timmy.fd(100)
# print(my_screen.canvheight)
# print(timmy)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
# table.field_names = ["Pokemon", "Type"]
# table.add_row(["Pikachu", "Electric"])
# table.add_row(["Squirtle", "Water"])
# table.add_row(["Charmander", "Fire"])
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = 'l'

print(table)
