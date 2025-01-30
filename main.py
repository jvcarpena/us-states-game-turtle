from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
states_img = Turtle()  # It is use as map.
states_img.shape(image)
t = Turtle()  # It is use as the state text.

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()

correct_guesses = []
game_is_on = True
while game_is_on:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/{len(state_list)} States Correct",
                                    prompt="What's another State's name?").title()
    if answer_state in state_list:
        t.penup()
        t.hideturtle()
        correct_guesses.append(answer_state)
        state_coor = data[data.state == answer_state]
        x_cor = int(state_coor.x)
        y_cor = int(state_coor.y)
        t.teleport(x_cor, y_cor)
        t.write(arg=answer_state, align="center", font=('Courier', 8, "bold"))

    if len(correct_guesses) == len(state_list):
        t.teleport(0, 0)
        t.write(arg="Great job! You've completed it.", align="center", font=('Courier', 25, "bold"))
        game_is_on = False

    if answer_state == "Exit":
        missing_states = [state for state in state_list if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False

# screen.exitonclick()
