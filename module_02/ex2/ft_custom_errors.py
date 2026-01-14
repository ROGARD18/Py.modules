# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_custom_errors.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rogard-antoine <rogard-antoine@student.    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/14 01:53:15 by rogard-anto       #+#    #+#              #
#    Updated: 2026/01/14 02:50:07 by rogard-anto      ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

class GardenError(Exception):
    pass

class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def garden_area(meters: int) -> None:
    if meters < 20:
        raise GardenError(f"{meters} is not enought for a garden")
    print("Good garden's size")


def plant_age(age: int) -> None:
    if age > 10:
        raise PlantError(f"{age} is too old for plant.")
    print(f"{age} this can be a posible age.")


def plant_watter(liters: int) -> None:
    if (liters > 2):
        raise WaterError(f"{liters} is too much ! The plant will die.")
    print(f"{liters} it's good for this plant")
    

def test_error() -> None:
    try:
        garden_area(30)
        plant_watter(11) # un fail et ca s'arrete
        plant_age(11)
    except GardenError as e:
        print(f"stop : {e}")

def main() -> None:
    test_error()


if __name__=="__main__":
    main()