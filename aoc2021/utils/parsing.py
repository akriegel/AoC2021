import os

def get_input(day):
    dir = os.path.dirname(__file__)
    path = os.path.join(dir, "../../inputs", day, "input.txt")
    with open(path) as f:
        return f.readlines()
