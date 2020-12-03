def part1():
    with open('input.txt') as file:
        list = [int(line) for line in file.read().split()]
        for num1 in list:
            for num2 in list:
                if num1 + num2 == 2020:
                    print(str.format('part1: {}', + num1 * num2))
                    return

def part2():
    with open('input.txt') as file:
        list = [int(line) for line in file.read().split()]
        for num1 in list:
            for num2 in list:
                for num3 in list:
                    if num1 + num2 + num3 == 2020:
                        print(str.format('part2: {}', + num1 * num2 * num3))
                        return

part1()
part2()
