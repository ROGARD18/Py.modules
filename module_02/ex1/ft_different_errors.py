# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_different_errors.py                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rogard-antoine <rogard-antoine@student.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/14 00:21:45 by rogard-anto       #+#    #+#              #
#    Updated: 2026/01/14 00:40:44 by rogard-anto      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

def garden_operations() -> None:
    try:
        int_one = int("abc")
        print("Good Value")
    except ValueError:
        print("Is not a valid number")
    try:
        imposible = 8 / 0
    except ZeroDivisionError:
        print("Imposible to divise by 0")
    try:
        f = open("nofile.txt")
    except FileNotFoundError:
        print ("File not found")
    dictionnaire = {'nom': 'Alice', 'age': 30}
    try:
        print(dictionnaire['ville'])
    except KeyError:
        print("'Ville' is not in the dictionnary")


def test_error_types() -> None:
    # Shows how to catch multiple error types with one except block not done !!!!!
    garden_operations()
    print("The program continues running after each error")


def main() -> None:
    test_error_types()


if __name__ == "__main__":
    main()