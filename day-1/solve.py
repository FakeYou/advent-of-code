input = open('input.txt').read()

def part1(input):
    floor = 0;

    for n in list(input):
        if n is '(':
            floor += 1
        if n is ')':
            floor -= 1

    return floor

def part2(input):
    floor = 0;

    for i, n in enumerate(list(input)):
        if n is '(':
            floor += 1
        if n is ')':
            floor -= 1

        if floor is -1:
            return i

print("Solution to part 1: %d" % part1(input))
print("Solution to part 2: %d" % part2(input))
