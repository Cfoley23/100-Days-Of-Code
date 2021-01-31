import turtle
import pandas

# screen = turtle.Screen()
# screen.title("U.S. States Game")
# bg_image = "blank_states_img.gif"
# screen.addshape(bg_image)
# turtle.shape(bg_image)

data = pandas.read_csv('50_states.csv')
print(data)

# answer_state = screen.textinput(title="Guess the State", prompt="What is another State's name?")
# print(answer_state)





















# this function returns a mouse click coord on the screen
# def get_mouse_click_coord(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()

