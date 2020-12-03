def part1():
    found = 0
    file = [line.rstrip('\n') for line in open('input.txt')]
    for line in file:
        rules, value, password = line.split();
        min, max = rules.split('-');
        instances = password.count(value[0])
        if instances >= int(min) and instances <= int(max):
            found += 1
    print(str.format('part1: {}', found))

def part2():
    found = 0
    file = [line.rstrip('\n') for line in open('input.txt')]
    for line in file:
        rules, value, password = line.split();
        i1, i2 = rules.split('-');
        first_matches = password[int(i1) - 1] == value[0]
        second_matches = password[int(i2) - 1] == value[0]
        if (first_matches or second_matches) and not (first_matches and second_matches):
            found += 1
    print(str.format('part2: {}', found))

part1()
part2()
