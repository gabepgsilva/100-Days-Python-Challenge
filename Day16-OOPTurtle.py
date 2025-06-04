from turtle import Turtle, Screen
from prettytable import PrettyTable


# #Object
# jimmy = Turtle()
# print(jimmy)

# jimmy.shape("turtle")
# jimmy.color("green")
# jimmy.forward(300)

# #Attribute 
# my_screen = Screen()
# print(my_screen.canvheight)


# my_screen.exitonclick()


table = PrettyTable()

table.add_column("Pokemon name", ["Pikachu", "Charmander", "Squirtle"])
table.add_column("Type", ["Electric", "Fire", "Water"])
table.align = "l"
print(table)