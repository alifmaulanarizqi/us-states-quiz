import turtle
import pandas as pd


def write_state(state_name):
    state_obj = turtle.Turtle()
    state_obj.hideturtle()
    state_obj.penup()
    state_obj.color("black")
    index = state_list.index(state_name)
    state_obj.goto(state_x_cor_list[index], state_y_cor_list[index])
    state_obj.write(f"{state_name}")


def check_state_in_list(check_answer):
    if check_answer in correct_state:
        return True
    return False


def append_missing_state():
    return [state for state in state_list if state not in correct_state]


def create_file():
    data_dict = {
        "state": missing_state
    }
    new_data = pd.DataFrame(data=data_dict)
    new_data.to_csv("missing_state.csv")


image_path = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Quiz")
screen.addshape(image_path)
turtle.shape(image_path)

data = pd.read_csv("50_states.csv")
state_list = data["state"].to_list()
state_x_cor_list = data["x"].to_list()
state_y_cor_list = data["y"].to_list()

correct_state = []
missing_state = []
for _ in range(50):
    answer = screen.textinput(title=f"{len(correct_state)}/{len(state_list)} States Correct", prompt="What's another state's name?")

    if not answer:
        missing_state = append_missing_state()
        create_file()
        break
    else:
        answer = answer.title()
        if answer in state_list and not check_state_in_list(answer):
            write_state(answer)
            correct_state.append(answer)

if len(missing_state) == 0:
    missing_state = append_missing_state()
    create_file()
