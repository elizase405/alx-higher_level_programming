#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

add_result = add(a, b)
sub_result = sub(a, b)
mul_result = mul(a, b)
div_result = div(a, b)

print("{0:d} + {1:d} = {2:d}".format(a, b, add_result))
print("{0:d} - {1:d} = {2:d}".format(a, b, sub_result))
print("{0:d} * {1:d} = {2:d}".format(a, b, mul_result))
print("{0:d} / {1:d} = {2:d}".format(a, b, div_result))
