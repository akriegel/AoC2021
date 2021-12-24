import enum

from aoc2021.utils.parsing import get_input


class Direction(enum.Enum):
    forward = "forward"
    up = "up"
    down = "down"


def main():
    tokens = (str.split(i) for i in get_input("day02"))
    commands = [(Direction(command), int(x)) for [command, x] in tokens]
    position = 0
    depth = 0
    aim = 0
    for command, x in commands:
        if command is Direction.forward:
            position += x
            depth += (aim * x)
        if command == Direction.down:
            aim += x
        if command == Direction.up:
            aim -= x
    print(f"position is {position}")
    print(f"depth is {depth}")
    print(f"multiplied position and depth is {position * depth}")

if __name__ == "__main__":
    main()
