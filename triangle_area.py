#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: November 2019
# This program calculates the area of a triangle when given length and width


def calculate(length, width):
    # find the area with the given inputs and prints the output
    area = (length * width) / 2
    print("{} cm²".format(area))


def main():
    numcheck_1 = input("enter length (cm): ")
    numcheck_2 = input("enter width (cm): ")
    try:
        number_1 = int(numcheck_1)
        number_2 = int(numcheck_2)
        if number_1 < 0 | number_2 < 0:
            print("invalid input")
    except ValueError:
        print("invalid input")
    calculate(number_1, number_2)


if __name__ == "__main__":
    main()
