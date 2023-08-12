#!/usr/bin/python3
import importlib

calc_module = importlib.import_module("calculator_1")

add = calc_module.add
sub = calc_module.sub
mul = calc_module.mul
div = calc_module.div

a = 10
b = 5

print(f"{a} + {b} = {add(a, b)}")
print(f"{a} - {b} = {sub(a, b)}")
print(f"{a} * {b} = {mul(a, b)}")
print(f"{a} / {b} = {div(a, b)}")
