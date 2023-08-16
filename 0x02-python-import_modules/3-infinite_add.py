#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    counter = len(argv) - 1
    sum = 0
    i = 1
    num = 0

    while i <= counter:
        num = int(argv[i])
        sum += num
        i += 1
    print(sum)
