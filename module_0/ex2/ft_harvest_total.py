# def ft_harvest_total() -> None :
#     one = input("Day 1 harvest: ")
#     two = input("Day 2 harvest: ")
#     three = input("Day 3 harvest: ")
#     print("Total harvest:", int(one) + int(two) + int(three))
# ft_harvest_total()

def ft_harvest_total() -> None:
    total = 0
    for i in range(1, 4):
        total += int(input(f"Day {i} harvest: "))
        print(f"Total harvest: {total}")


ft_harvest_total()
