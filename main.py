import turtle
import pandas

IMAGE = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")

screen.addshape(IMAGE)
turtle.shape(IMAGE)

data = pandas.read_csv("./50_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_input = screen.textinput(title=f"{len(guessed_states)}/50 Correct",
                                    prompt="What's another state's name?").title()

    if answer_input == "Exit":
        missing_states = [state for state in states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_input in states:
        guessed_states.append(answer_input)
        t = turtle.Turtle()
        t.hideturtle()
        t.pu()
        state_data = data[data.state == answer_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_input)

# Getting hold of x and y cords in a screen
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
