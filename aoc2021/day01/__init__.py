from aoc2021.utils.parsing import get_input

def main():
    input = get_input("day01")
    kermit = [int(i) for i in input]
    j = 0
    k = 0
    for i in range(len(kermit) - 1):
        if kermit[i] < kermit[i+1]:
            j += 1
    for i in range(len(kermit) - 3):
        if kermit[i] + kermit[i+1] + kermit[i+2] < kermit[i+1] + kermit[i+2] + kermit[i+3]:
            k += 1
    print(f"{j} one-measurment increases")
    print(f"{k} three-measurment increases")

if __name__ == "__main__":
    main()
