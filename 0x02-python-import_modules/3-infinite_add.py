#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    counter = len(argv) - 1
    num, sums, i = 0, 0, 1

    while i <= counter:
        num = int(argv[i])
        sums += num
        i += 1
    print(sums)

