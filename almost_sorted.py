# #Given an array of integers, determine whether the array can be sorted in ascending order using only one of the following operations one time.

# #Swap two elements.
# #Reverse one sub-segment.
# # Determine whether one, both or neither of the operations will complete the task. Output is as follows.

# If the array is already sorted, output yes on the first line. You do not need to output anything else.

# If you can sort this array using one single operation (from the two permitted operations) then output yes on the first line and then:

# If elements can only be swapped,  and , output swap l r in the second line.  and  are the indices of the elements to be swapped, assuming that the array is indexed from  to .
# If elements can only be reversed, for the segment , output reverse l r in the second line.  and  are the indices of the first and last elements of the subarray to be reversed, assuming that the array is indexed from  to . Here  represents the subarray that begins at index  and ends at index , both inclusive.
# If an array can be sorted both ways, by using either swap or reverse, choose swap.

# If the array cannot be sorted either way, output no on the first line.


#!/bin/python3

import math
import os
import random
import re
import sys
from copy import *
#
# Complete the 'almostSorted' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def almostSorted(arr):
    sorted=deepcopy(arr)
    sorted.sort()
    
    if sorted==arr:
        print("yes")
        return
    
    for i in range(len(arr)):
        if arr[i]>arr[i+1]:
            low=i
            break
    for l in range(len(arr)-1,0,-1):
        if arr[l]<arr[l-1]:
            high=l
            break
        
    temp=deepcopy(arr)
    temp[high],temp[low]=temp[low],temp[high]
    if temp==sorted:
        print("yes")
        print("swap",low+1,high+1)
        return
    temp=deepcopy(arr)
    temp=temp[0:low]+temp[low:high+1][::-1]+temp[high+1:]
    if temp==sorted:
        print("yes")
        print("reverse",low+1,high+1)
        return
    
    print("no")
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
