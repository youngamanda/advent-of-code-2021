# -*- coding: utf-8 -*-
"""
Advent of code 1
10/04/2022
"""

# Read in input data
nums = []
with open('input_1') as f:
    for line in f:
        nums.append(int(line))

# Loop through and see if increasing
n_prev = nums[0]
count = 0
for n in nums[1:]:
   if n > n_prev:
       count += 1
   n_prev = n

print('The answer is: ' + str(count))