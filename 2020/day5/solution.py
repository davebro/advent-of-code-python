def evaluate_letter(letter, positions, direction):
    low, high = positions
    lower, upper = direction
    if letter == upper:
        low = high - ((high - low) / 2)
    elif letter == lower:
        high = high - ((high - low) / 2) - 1
    return low, high

def part1():
    with open('input.txt') as file:
        boarding_passes = file.read().splitlines()
        ids = []
        for boarding_pass in boarding_passes:
            low, high = 0, 128
            row, column = 0, 0
            for index, letter in enumerate(boarding_pass[:7]):
                if index == 6:
                    row = min(low, high) if letter == 'F' else max(low, high)
                else:
                    low, high = evaluate_letter(letter, [low, high], ['F', 'B'])
            low, high = 0, 8
            for index, letter in enumerate(boarding_pass[-3:]):
                if index == 2:
                    column = min(low, high) if letter == 'L' else max(low, high)
                else:
                    low, high = evaluate_letter(letter, [low, high], ['L', 'R'])
            ids.append(row * 8 + column)
        print(max(ids))

part1();


