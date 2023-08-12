#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5
    
    sums = add(a, b)
    diff = sub(a, b)
    product = mul(a, b)
    quotient = div(a, b)

    print(f"{a} + {b} = {sums}")
    print(f"{a} - {b} = {diff}")
    print(f"{a} * {b} = {product}")
    print(f"{a} / {b} = {quotient}")
