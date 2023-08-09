import sys
import time
import tkinter as tk
from email.mime import image

sys.path.insert(0, "./src")

from actions import Action
from robot import Robot
from terrain import State, Field

height = 768
width = 704

# Creation of the main window
root = tk.Tk()
root.geometry(f"{height}x{width}")
root.minsize(height, width)
root.maxsize(height, width)

root.title("La guerre des robots")


# https://www.iconexperience.com/v_collection/
icons = {
    "bomb": tk.PhotoImage(file="data/bomb.png"),
    "dead": tk.PhotoImage(file="data/dead.png"),
    "crown": tk.PhotoImage(file="data/crown.png"),
}

game_pause = False

file = ["map1", "map2", "map3"] # all the map
speciality_list = ["furtif", "offensif", "defensif"]
robots_list = list()

indice = 0  # indice for change_map
map_choose = file[0]

t = Field()
t.load_map(map_choose)

# all the frame for our page
frame_page1 = tk.Frame(root)  # main
frame_page1.pack()

frame_page2 = tk.Frame(root)  # configuration
frame_page2.pack()

frame_page3 = tk.Frame(root)  # game
frame_page3.pack()


def switch_page(from_page, to_page) -> None:
    """switch page"""
    from_page.forget()
    to_page.pack()


def pause() -> None:
    """put the game in pause"""
    global game_pause
    game_pause = not game_pause
    print("PAUSE")


###############################################
################# PAGE 1 ######################
###############################################

bg1 = tk.PhotoImage(file="data/robot.png")
label = tk.Label(frame_page1, image=bg1)
label.pack()

button_play = tk.Button(
    frame_page1,
    text="START",
    font=("Arial", 26),
    bg="black",
    relief="raised",
    padx=50,
    pady=20,
    bd=3,
    activeforeground="red",
    command=lambda: switch_page(frame_page1, frame_page2),
)
button_play.place(x=300, y=300)

close_button = tk.Button(
    frame_page1,
    text="EXIT",
    font=("Arial", 16),
    bg="black",
    fg="black",
    command=root.destroy,
)
close_button.place(x=696, y=670)

###############################################
################# PAGE 2 ######################
###############################################

bg2 = tk.PhotoImage(file="data/game3.png")
label2 = tk.Label(frame_page2, image=bg2)
label2.pack()

game_configuration = tk.Label(
    frame_page2, text="CONFIGURATION GAME", font=("Arial", 30)
)
game_configuration.place(x=200, y=0)

button_go_to_game = tk.Button(
    frame_page2,
    text="Let's play !",
    font=("Arial", 30),
    command=lambda: start(frame_page2, frame_page3),
)
button_go_to_game.place(x=300, y=650)

button_change_map = tk.Button(
    frame_page2,
    text="Change map",
    font=("Arial", 22),
    command=lambda: change_map(),
)
button_change_map.place(x=300, y=560)

t.print_map(frame_page2, icons, 6, 50)

add_robot = tk.Spinbox(
    frame_page2,
    from_=2,
    to=6,
    bg="white",
    fg="black",
    font=("Arial", 18),
    justify=tk.CENTER,
    width=8,
)
add_robot.place(x=0, y=620)

text_robot = tk.Label(frame_page2, text="Choose a number of robots", font=("Arial", 16))
text_robot.place(x=0, y=600)

add_health = tk.Spinbox(
    frame_page2,
    from_=500,
    to=3000,
    bg="white",
    fg="black",
    font=("Arial", 18),
    justify=tk.CENTER,
    width=8,
    increment=100,
)
add_health.place(x=650, y=580)

text_health = tk.Label(frame_page2, text="Choose robots hit points", font=("Arial", 16))
text_health.place(x=590, y=560)

add_radar = tk.Spinbox(
    frame_page2,
    from_=2,
    to=6,
    bg="white",
    fg="black",
    font=("Arial", 18),
    justify=tk.CENTER,
    width=8
)
add_radar.place(x=650, y=660)

text_radar = tk.Label(frame_page2, text="Choose robots radar", font=("Arial", 16))
text_radar.place(x=616, y=640)


###############################################
################# PAGE 3 ######################
###############################################

bg3 = tk.PhotoImage(file="data/jeu.png")
image_pause = tk.PhotoImage(file="data/pause.png")

label3 = tk.Label(frame_page3, image=bg3)
label3.pack()

button_pause = tk.Button(frame_page3, image=image_pause, command=lambda: pause())
button_pause.place(x=0, y=550)

listbox = tk.Listbox(
    frame_page3,
    bg="White",
    width=50,  # number of characters
    height=8,  # number of lines
    fg="Black",
    font=("Arial", 18),
)
listbox.place(x=200, y=520)

label_robot = tk.Label(
    frame_page3, text="Results", font=("Arial", 30), bg="White", fg="Black"
)
label_robot.place(x=62, y=520)

listbox_robot = tk.Listbox(
    frame_page3,
    bg="White",
    width=12,  # number of characters
    height=6,  # number of lines
    fg="Black",
    font=("Arial", 18),
)
listbox_robot.place(x=62, y=564)

###############################################
################# END of page #################
###############################################

def change_map() -> None:
    """change the map"""
    global indice
    indice += 1
    map_choose = file[indice % len(file)]
    t.load_map(map_choose)
    t.print_map(frame_page2, icons, 6, 50)


def start(from_frame, to_frame) -> None:
    """start game"""
    switch_page(from_frame, to_frame)
    init_game()

    t.print_map(frame_page3, icons, 5, 5)
    time.sleep(1)

    print(robots_list)
    # Start the game
    while len(robots_list) > 1:
        for robot in robots_list:

            while game_pause:
                root.update()

            x, y = robot.get_position()
            t.set_state((x, y), State.ROBOT)
            robot.set_type(State.ROBOT)
            radar, closest_robot = t.is_a_robot_close(robot)
            instruction, insert_str = robot.next_instruction(radar, "")

            if instruction == "IN":
                t.set_state((x, y), State.INVISIBLE)

            if instruction == "MI":
                mine_position = t.get_mine_position((x, y))
                if mine_position != (-1, -1):
                    t.set_state(mine_position, State.MINE)
                    robot.remember_my_mine(mine_position)

            if instruction == "TV" or instruction == "TH":
                a, b = t.shoot(robot, instruction)
                if (a, b) == (-2, -2):
                    insert_str = insert_str + f", hit a wall"
                elif (a, b) != (-1, -1):
                    for r in robots_list:
                        if r.get_position() == (a, b):
                            r.decrease_health(Action("TH").get_damage())
                            print(f"{r.name} was hit and has now {r.get_health()}")
                            insert_str = insert_str + f", hit {r.name}"

            if instruction == "PS" and radar:
                next_position_close = t.get_closest_position(
                    robot.get_position(), closest_robot.get_position()
                )

                if next_position_close == robot.get_position():
                    print("NOOP")
                    continue

                t.set_state(robot.get_position(), State.EMPTY)
                t.set_state(next_position_close, State.ROBOT)
                robot.set_position(*next_position_close)
                print(f"{robot.name} move to {next_position_close}")

            if instruction == "FT" and radar:
                next_position_far = t.get_farthest_position(
                    robot.get_position(), closest_robot.get_position()
                )

                if next_position_far == robot.get_position():
                    print("NOOP")
                    continue

                t.set_state(robot.get_position(), State.EMPTY)
                t.set_state(next_position_far, State.ROBOT)
                robot.set_position(*next_position_far)
                print(f"{robot.name} move to {next_position_far}")

            print(robot)
            print()
            # robot will move if needed
            t.move_robot(instruction, robot)
            if robot.get_health() <= 0:
                robots_list.remove(robot)
                t.set_state(robot.get_position(), State.DEAD)
                print(f"{robot.name} is dead")
                insert_str = insert_str + f", is dead"
                # listbox_robot.delete(int(robot.name))
                # listbox_robot.insert(int(robot.name), f"{robot.name} is dead")

            # Updating the instructions frame
            listbox.insert(0, f"{insert_str}, {robot.print_hp()}")
            t.print_map(frame_page3, icons, 5, 5)
            time.sleep(1.5)

    t.set_state(robots_list[0].get_position(), State.WINNER)
    print("END of GAME")
    t.print_map(frame_page3, icons, 5, 5)
    robot = robots_list[0]
    listbox.insert(0, f"{robot.name} is the Winner !!!")
    listbox_robot.delete(int(robot.name[-1]))
    listbox_robot.insert(int(robot.name[-1]), f"{robot.name} wins")


def init_game() -> tuple:
    """init the robot, their position, their programm"""
    number_of_robots = int(add_robot.get())
    health = int(add_health.get())
    radar = int(add_radar.get())

    for i in range(int(number_of_robots)):
        robot_name = ["R2D2", "C3PO", "WALL-E", "BAYMAX", "TURBO", "TITAN"]
        speciality = speciality_list[i % len(speciality_list)]
        t.add_object(r := Robot(name=f"{robot_name[i]}", health=health, speciality=speciality, radar=radar))
        listbox_robot.insert(i, f"{r.name} ({r.speciality})")

    # We place the robots on the Map
    t.define_robots_position()

    # We initialize the robots with their programs and we create a list of robots
    for obj in t.objects_list:
        if obj.isRobot():
            obj.load_program()
            robots_list.append(obj)
            print(obj)

    return t, robots_list


if __name__ == "__main__":
    # Starting the main loop of the interface
    root.mainloop()
