"""
https://leetcode.com/problems/set-mismatch/description/
The set S originally contains numbers from 1 to n. But unfortunately, due to the data error, one of 
the numbers in the set got duplicated to another number in the set, which results in repetition of 
one number and loss of another number.

Given an array nums representing the data status of this set after the error. Your task is to firstly find 
the number occurs twice and then find the number that is missing. Return them in the form of an array.

Example 1:
Input: nums = [1,2,2,4]
Output: [2,3]
"""
from collections import Counter
def findErrorNums(nums):
    #guessing this is O(n)
    duplicate = Counter(nums).most_common(1)[0][0]


    missing = 0
    #O(n) worst, best O(1)
    for i in range(1, len(nums) + 1):
        if i not in nums:
            missing = i
            return [duplicate, missing]

    #overall, O(n**2), will come back and try to optimize
    
print(findErrorNums([1,2,2,4]))

