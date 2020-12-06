def part1():
	file = open('input.txt').readlines()
	group_answers = []
	answer = 0
	for line in file:
		if line != '\n':
			group_answers.extend(list(line.split()[0]))
		else:
			answer += len(set(group_answers))
			group_answers = []
	answer += len(set(group_answers))
	print(answer)

def part2():
	file = open('input.txt').readlines()
	group_answers = []
	answer = 0
	for line in file:
		if line != '\n':
			group_answers.append(set(line.split()[0]))
		else:
			answer += len(group_answers[0].intersection(*group_answers))
			group_answers = []
	answer += len(group_answers[0].intersection(*group_answers))
	print(answer)

part1()
part2()

