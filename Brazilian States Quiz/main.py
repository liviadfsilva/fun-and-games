import turtle
import pandas
from turtle import Screen

screen = Screen()
screen.setup(600, 600)
screen.title("Brazilian States Quiz")
image = "resized_image.gif"
screen.addshape(image)
turtle.shape(image)

guessed_states = []

########################################################
#Get x and y coordinates:
# def get_mouse_click_coordinates(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coordinates)
########################################################

while len(guessed_states) < 26:
    answer = screen.textinput(f"{len(guessed_states)}/26 States Guessed",
                              prompt="Guess a Brazilian State:").title()

    data = pandas.read_csv("states_data.csv")
    all_states = data.states.to_list()

    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
    if answer in all_states:
        guessed_states.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.states == answer]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer)

turtle.mainloop()