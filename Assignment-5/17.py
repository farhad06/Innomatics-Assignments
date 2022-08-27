#!/bin/python3

import math
import os
import random
import re
import sys





x,y = map(int, input().split())
i,j = [], ""
for _ in range(x):
    i.append(input())

for z in zip(*i):
    j+= "".join(z)

print(re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", j))
