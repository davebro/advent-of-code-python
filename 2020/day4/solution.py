import re

def parse_file(fileName):
    file = open(fileName).readlines()
    passports = []
    passport = {}
    for line in file:
        parts = line.split()
        if len(parts) > 0:
            for part in parts:
                key_and_value = part.split(':')
                passport[key_and_value[0]] = key_and_value[1]
        else:
            passports.append(passport)
            passport = {}
    passports.append(passport)
    return passports

def part1():
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = parse_file('input.txt')
    valid_passports = 0
    for passport in passports:
        if all(key in passport for key in required_keys):
            valid_passports += 1
    print(str.format('part1: {}', valid_passports))

# ewwww, ewwww, ewwww, ewwww
def part2():
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    passports = parse_file('input.txt')
    invalid_passports = 0

    for passport in passports:
        if not all(key in passport for key in required_keys):
            invalid_passports += 1
            continue

        birth_year = int(passport['byr'])
        issue_year = int(passport['iyr'])
        expiration_year = int(passport['eyr'])
        height = passport['hgt']
        hair_color = passport['hcl']
        eye_color = passport['ecl']
        passport_id = passport['pid']

        if birth_year < 1920 or birth_year > 2002:
            invalid_passports += 1
            continue
        elif issue_year < 2010 or issue_year > 2020:
            invalid_passports += 1
            continue
        elif expiration_year < 2020 or expiration_year > 2030:
            invalid_passports += 1
            continue
        elif not re.match('^#[a-z0-9]{6}$', hair_color):
            invalid_passports += 1
            continue
        elif not eye_color in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
            invalid_passports += 1
            continue
        elif not re.match('^[0-9]{9}$', passport_id):
            invalid_passports += 1
            continue

        # double ewwwww
        height_valid = True
        unit_of_measure = height[-2:]
        height_value = int(height[:-2])
        if unit_of_measure in ['cm', 'in']:
            if unit_of_measure == 'cm':
                if height_value < 150 or height_value > 193:
                    height_valid = False
            elif height_value < 59 or height_value > 76:
                height_valid = False
        else:
            height_valid = False

        if not height_valid:
            invalid_passports += 1
            continue

    print(str.format('part2: {}', len(passports) - invalid_passports))

part1()
part2()

