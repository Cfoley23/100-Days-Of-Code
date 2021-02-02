import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.bgcolor('grey')
bg_image = "blank_states_img.gif"
screen.addshape(bg_image)
turtle.shape(bg_image)

data = pandas.read_csv('50_states.csv')
all_states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What is another State's name?").title()
    if answer_state == "Exit":
        # [new_item for item in list if test]
        missing_states = [state for state in all_states_list not in guessed_states]
        # missing_states = []
        # for state in all_states_list:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('states_to_learn.csv')
        break
    # If answer_state is one of the states in .csv file
    if answer_state in all_states_list:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.ht()
        t.pu()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        # t.write(state_data.state.item())
        t.write(answer_state)



# this function returns a mouse click coord on the screen
# def get_mouse_click_coord(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coord)
# turtle.mainloop()

