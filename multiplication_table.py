#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: October 2019
# This takes a number
#  and prints which its multiplication table


def main():
    while True:
        try:
            number = int(input("Please enter a positive number: "))

            for variable in range(0, 11):
                calculation = number * variable
                print(calculation)

        except ValueError:
            print()
            print("Invalid Input")
            print()
            continue

        else:
            break


if __name__ == "__main__":
    main()
