#!/usr/bin/env python3

# Created by: Hertz
# Created on: May , 2, 2022
# This program asks the user to enter a number
# And divide by 1 from 0 to the user number


def main():
    # valuables
    loop_sum = 0
    counter = 0
    total_sum_list = []
    # Ask theuser to enter a number
    user_num = input("Enter a whole number: ")

    try:
        # corverting into int
        user_int = int(user_num)
        # checking if it is a positive number and adding
        # them all together.
        if user_int >= 0:
            for counter in range(1, user_int + 1):

                total_sum_list.append(counter)

                print(
                    "1/{} = {}".format(
                        counter,
                        1 / counter,
                    )
                )
                loop_sum = loop_sum + 1 / counter

            print("")
            print(*total_sum_list, sep=" + 1/", end=" ")
            print(" = {}".format(loop_sum))
            print("")
            print("The sum of {} = {}".format(user_int, loop_sum))

        else:
            print("Negative number. Please input a whole number.")

    # catching error
    except:
        print("Invalid input. Enter numbers{1,2,3..}")


if __name__ == "__main__":
    main()
