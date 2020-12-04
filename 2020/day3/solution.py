def part1():
	file = [line.rstrip('\n') for line in open('input.txt')]
	file.pop(0)
	current_index = 3
	tree_count = 0
	step_count = 3
	for line in file:
		if line[current_index] == '#':
			tree_count += 1
		remaining_steps = (len(file[0]) - 1) - current_index
		if remaining_steps < step_count:
			current_index = (remaining_steps * -1) + 2
		else:
			current_index += step_count
	print(str.format('part1: {}', tree_count))

def part2():
	file = [line.rstrip('\n') for line in open('input.txt')]
	file.pop(0)
	all_trees = []
	slopes = [[(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]
	for slope in slopes:
		for coordinates in slope:
			tree_count = 0
			current_index = coordinates[0]
			step_count = coordinates[0]
			step_down = coordinates[1]
			for i, line in enumerate(file):
				if i % step_down == 0 and step_down > 1:
					continue
				if line[current_index] == '#':
					tree_count += 1
				remaining_steps = (len(file[0]) - 1) - current_index
				if remaining_steps < step_count:
					current_index = (remaining_steps * -1) + (step_count - 1)
				else:
					current_index += step_count
			all_trees.append(tree_count)
	print(str.format('part2: {}', reduce(lambda x, y: x * y, all_trees)))

part1()
part2()

