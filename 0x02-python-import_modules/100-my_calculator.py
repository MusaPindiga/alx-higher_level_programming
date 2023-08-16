#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div

    length = len(argv)

    if length != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])

        if operator == "+":
            print("{} {} {} = {}".format(a, operator, b, add(a, b)))
        elif operator == "-":
            print("{} {} {} = {}".format(a, operator, b, sub(a, b)))
        elif operator == "*":
            print("{} {} {} = {}".format(a, operator, b, mul(a, b)))
        elif operator == "/":
            print("{} {} {} = {}".format(a, operator, b, div(a, b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
