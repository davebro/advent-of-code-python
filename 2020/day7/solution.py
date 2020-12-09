import re

def search_for_new_bags(file, bags, excluded_bags):
    new_bags = bags
    for bag in bags:
        for line in file:
            parts = line.split('contain')
            if bag in parts[1]:
                color = re.search(r'(.*?)bag', parts[0])
                if color is not None and color.group(1).strip() not in excluded_bags:
                        new_bags.append(color.group(1).strip())
    return list(set(new_bags))

def part1():
    file = open('input.txt').readlines()
    bags = []
    excluded_bags = ['shiny gold']
    for line in file:
        parts = line.split('contain')
        bag = re.search(r'(.*?)bag', parts[0]).group(1).strip()
        if 'no other' in parts[1]:
            if bag not in excluded_bags:
                excluded_bags.append(bag)
        elif 'shiny gold' in parts[1]:
            if bag not in excluded_bags:
                bags.append(bag)
    bag_count = len(bags)
    still_searching = True
    while still_searching:
        new_bags = search_for_new_bags(file, bags, excluded_bags)
        if len(new_bags) != bag_count:
            bag_count = len(new_bags)
            bags.extend(list(set(new_bags)))
        else:
            still_searching = False
    print(str.format('part1: {}', len(set(bags))))

part1()
