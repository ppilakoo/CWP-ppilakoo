#!/usr/bin/env python3

num = float(input("Give me a number: ").strip())

if num % 1 == 0:
    print(int(num))
else:
    print(int(num) + 1)