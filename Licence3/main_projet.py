import sys
sys.path.insert(0, "./src")

from actions import Action
from robot import Robot
from terrain import Terrain

health = 50


def main() -> None:
    file = "map1"
    speciality_list = ["furtif", "offensif"]
    t = Terrain(file=file)
    t.load_map(file)

    while True:
        nbr_r = input("Choose a number in [2 - 6]: ")
        if int(nbr_r) < 2 or int(nbr_r) > 6:
            print("Seriously ? Try again !")
        else:
            break

    # On rajoute les robots à la Map
    for i in range(int(nbr_r)):
        speciality = speciality_list[i % len(speciality_list)]
        t.add_object(Robot(name=f"robot{i}", health=health, speciality=speciality))

    print(t)
    print()
    # exit()

    # On place les robots sur la Map
    t.define_robots_position()

    # On initialise les robots avec leurs programmes et on crée une liste de robots
    robots_list = list()
    for obj in t.objects_list:
        if obj.isRobot():
            obj.load_program()
            robots_list.append(obj)
            print(obj)

    # On lance la partie
    while len(robots_list) > 1:
        for robot in robots_list:
            radar = t.is_a_robot_close(robot)
            instruction = robot.next_instruction(radar)
            if instruction == "MI":
                t.set_mine(robot.get_position())
            print(robot)
            print()
            if instruction == "AL":
                t.robots_move_AL(robot)

            if (
                instruction == "DD D"
                or instruction == "DD G"
                or instruction == "DD H"
                or instruction == "DD B"
            ):
                t.robots_move_DD(robot, robot.get_position(), robot.get_speciality())

            if robot.get_health() <= 0:
                robots_list.remove(robot)
                t.robot_is_dead(robot)
    t.print_map()


if __name__ == "__main__":
    main()
