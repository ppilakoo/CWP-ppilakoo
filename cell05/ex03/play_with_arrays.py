#!/usr/bin/env python3

OA = [2, 8, 9, 48, 8, 22, -12, 2]
ModA = [x for x in OA if x>5]
NA = {x+2 for x in ModA}
print("Original array:",OA)
print("New array:",NA)