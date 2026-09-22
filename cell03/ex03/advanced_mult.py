#!/usr/bin/env python3
num = 0
k = 0

while(num<=10):
    print("Table de",num,":",end=" ")
    while(k<=10):
        print(k*num,end=" ")
        k = k + 1
    print()
    num = num +1
    k = 0
    