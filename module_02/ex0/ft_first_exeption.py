# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_first_exeption.py                               :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rogard-antoine <rogard-antoine@student.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/13 23:49:14 by rogard-anto       #+#    #+#              #
#    Updated: 2026/01/14 00:20:16 by rogard-anto      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def check_temperature(temp_str) -> None:
    try:
        int_temp = int(temp_str)
        if (int_temp <= 40 and int_temp >= 0):
            print(f"Temperature {int_temp} is perfect for plant!")
        elif (int_temp > 40):
            print(f"Error: {int_temp} is too hot for plants (max 40 degrees)")
        elif (int_temp < 0):
            print(f"Error: {int_temp} is too cold for plants (max 40 degrees)")
    except:
        print(f"Error: '{temp_str}' is not a valid number")


def test_temperature_input() -> None:
    check_temperature("abc")


def main():
    test_temperature_input()


if __name__=="__main__":
    main()