#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

    args = argv[1:]
    counter = len(args)
    i = 0

    if counter == 0:
        print("0 arguments.")
    elif counter == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(counter))

    while i in range(counter):
        print("{}: {}".format(i + 1, args[i]))
        i += 1
