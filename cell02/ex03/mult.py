#!/usr/bin/env python3

stnum = int(input("Enter the first number: ").strip())
ndnum = int(input("Enter the second number: ").strip())
ans = stnum*ndnum
print(stnum,"x",ndnum,"=",ans)
if ans > 0:
    print("The result is positive.")
elif ans < 0:
    print("The result is negative.")
else:
    print("The result is positive and negative.")