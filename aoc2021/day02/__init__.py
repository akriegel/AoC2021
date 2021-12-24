from aoc2021.utils.parsing import get_input

def main():
    input = get_input("day02")
    commands = [str.split(i) for i in input]
    position = 0
    depth = 0
    aim = 0
    for i in range(len(commands)):
        if commands[i][0] == "forward":
            position += int(commands[i][1])
            depth += (aim * int(commands[i][1]))
        if commands[i][0] == "down":
            aim += int(commands[i][1])
        if commands[i][0] == "up":
            aim -= int(commands[i][1])
    print(f"position is {position}")
    print(f"depth is {depth}")
    print(f"multiplied position and depth is {position * depth}")

if __name__ == "__main__":
    main()
