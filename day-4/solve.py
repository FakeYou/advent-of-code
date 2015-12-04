import hashlib

input = 'bgvyzdsv'

def part1(input):
    # bruteforce md5 hashes
    for i in range(0, 10000000):
        # create a md5 hash with the 'input' + index
        hash = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()

        # return the 'input' + index when the hash starts with '00000'
        if hash[0:5] == "00000":
            return input + str(i)

def part2(input):
    # bruteforce md5 hashes
    for i in range(0, 100000000):
        # create a md5 hash with the 'input' + index
        hash = hashlib.md5((input + str(i)).encode('utf-8')).hexdigest()

        if i % 1000000 is 0:
            print(i)

        # return the 'input' + index when the hash starts with '000000'
        if hash[0:6] == "000000":
            return input + str(i)

print("Solution to part 1: %s" % part1(input))
print("Solution to part 2: %s" % part2(input))

