# http://adventofcode.com/day/2

input = open('input.txt').read()
packages = input.split('\n')

def part1(packages):
    total = 0;

    for package in packages:
        # get the length, width and height as ints from the package
        (l, w, h) = map(int, package.split('x')) 

        # calculate the size of all surfaces
        surfaces = [l*w*2, w*h*2, h*l*2]
        
        # sort from smallest to largest surface
        # then add half of the smallest surface as padding
        surfaces.sort()
        surfaces.append(surfaces[0] / 2)
        
        # add the sum of all the surfaces to the total
        total += sum(surfaces)

    return total

def part2(packages):
    total = 0;

    for package in packages:
        # split the package in the dimensions, conver to string, sort from smallest to largest
        dimensions = list(map(int, package.split('x')))
        dimensions.sort()
        (i, j, k) = dimensions

        # calculate the ribbon to wrap the present
        ribbon = i + i + j + j
        # calculate the ribbon for the bow
        ribbon += i * j * k

        # add the ribbon to the total
        total += ribbon

    return total

print("Solution to part 1: %d" % part1(packages))
print("Solution to part 2: %d" % part2(packages))
