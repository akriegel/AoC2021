from aoc2021.utils.parsing import get_input
import typing as t
import sys

def main():
    input = get_input("day03")
    ints = [int(i, 2) for i in input]
    gamma = 0
    epsilon = 0
    bit_op = 1 << 11
    while bit_op:
        ones = 0
        zeroes = 0
## PART 1 ##
        for i in range(len(ints)):
            if ints[i] & bit_op:
                ones += 1
            else:
                zeroes += 1
        if ones > zeroes:
            gamma += bit_op
        elif ones < zeroes:
            epsilon += bit_op
        else:
            print("FOK")
            sys.exit()
        bit_op = bit_op >> 1
    print(f"gamma rate = {gamma}")
    print(f"epsilon rate = {epsilon}")
    print(f"power consumption = {gamma * epsilon}")

## PART 2 ##
    o2 = ints
    co2 = ints
    bit_op = 1 << 11
    while len(o2) > 1:
        ones = 0
        zeroes = 0
        for i in range(len(o2)):
            if o2[i] & bit_op:
                ones += 1
            else:
                zeroes += 1
        if ones < zeroes:
            o2 = floss(o2, 0, bit_op)
        else:
            o2 = floss(o2, 1, bit_op)
        bit_op = bit_op >> 1
    bit_op = 1 << 11
    while len(co2) > 1:
        ones = 0
        zeroes = 0
        for i in range(len(co2)):
            if co2[i] & bit_op:
                ones += 1
            else:
                zeroes += 1
        if ones < zeroes:
            co2 = floss(co2, 1, bit_op)
        else:
            co2 = floss(co2, 0, bit_op)
        bit_op = bit_op >> 1
    print(f"oxygen generator rating = {o2[0]}")
    print(f"CO2 scrubber rating = {co2[0]}")
    print(f"life support rating = {o2[0] * co2[0]}")

def floss(i_list: t.List[int], bit: int, bit_op: int) -> t.List[int]:
    o_list = []
    for i in range(len(i_list)):
        if (i_list[i] & bit_op) == (bit * bit_op):
            o_list.append(i_list[i])
    return o_list

if __name__ == "__main__":
    main()
