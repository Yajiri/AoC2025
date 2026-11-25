#had to make it into a function in order to run the unittest_solution.py
from pathlib import Path


def count_stops(file_path):
    startpoint = 50
    x = 0

    with open(file_path, "r") as file:
        for line in file:
            command = line.strip().upper()

            if not command:
                continue

            direction = command[0]
            move_steps = int(command[1:])

            if direction == "L":
                startpoint = (startpoint + move_steps) % 100
                if startpoint == 0:
                    x += 1

            if direction == "R":
                startpoint = (startpoint - move_steps) % 100
                if startpoint == 0:
                    x += 1

    return x


if __name__ == "__main__":
    file = Path(__file__).parent / ".." / "inputs" / "input1.txt"
    print("Stopped at 0", count_stops(file), "times")