def evaluate_letter(letter, positions, direction):
    low, high = positions
    lower, upper = direction
    if letter == upper:
        low = high - ((high - low) / 2)
    elif letter == lower:
        high = high - ((high - low) / 2) - 1
    return low, high

def part1(showOutput):
    ids = []
    with open('input.txt') as file:
        boarding_passes = file.read().splitlines()
        for boarding_pass in boarding_passes:
            low, high = 0, 127
            row, column = 0, 0
            for index, letter in enumerate(boarding_pass[:7]):
                if index == 6:
                    row = min(low, high) if letter == 'F' else max(low, high)
                    low, high = 0, 7
                else:
                    low, high = evaluate_letter(letter, [low, high], ['F', 'B'])
            for index, letter in enumerate(boarding_pass[-3:]):
                if index == 2:
                    column = min(low, high) if letter == 'L' else max(low, high)
                else:
                    low, high = evaluate_letter(letter, [low, high], ['L', 'R'])
            ids.append(row * 8 + column)
        if showOutput:
            print(max(ids))
    return ids

def part2():
    ids = part1(False)
    ids.sort()
    counter = ids[0]
    for id in ids:
        if id != counter:
            break
        counter += 1
    print(counter)

part1(True)
part2()

