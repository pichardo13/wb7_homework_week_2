"""
https://leetcode.com/problems/distribute-candies/

You have n candies, the ith candy is of type candies[i].

You want to distribute the candies equally between a sister and a brother so that each of them gets 
n / 2 candies (n is even). The sister loves to collect different types of candies, so you want to give 
her the maximum number of different types of candies.

Return the maximum number of different types of candies you can give to the sister.


Example 1:

Input: candies = [1,1,2,2,3,3]
Output: 3
Explanation:
There are three different kinds of candies (1, 2 and 3), and two candies for each kind.
Optimal distribution: The sister has candies [1,2,3] and the brother has candies [1,2,3], too. 
The sister has three different kinds of candies. 

Example 2:

Input: candies = [1,1,2,3]
Output: 2
Explanation: For example, the sister has candies [2,3] and the brother has candies [1,1]. 
The sister has two different kinds of candies, the brother has only one kind of candies.

Example 3:

Input: candies = [1,1]
Output: 1

Example 4:

Input: candies = [1,11]
Output: 1

Example 5:

Input: candies = [2,2]
Output: 1
"""
def distributeCandies(candies):

    # candiesSet = set(candies)
    # if len(candiesSet) < len(candies)/2:
    #     return len(candiesSet)
    # else:
    #     return len(candies)//2

    return min(len(candies)//2, len(set(candies)))

# sis = [1,2,3] bro = [1,2,3], will have 3 types of candies
input_1 = [1,1,2,2,3,3]
print(distributeCandies(input_1) == 3)


#sis = [1,2,3] bro = [1,2,2], will have 3 types of candies 
input_2 = [1,1,2,2,2,3]
print(distributeCandies(input_2) == 3)

#sis = [1,1] bro = [1,1], will only have 1 type of candy
input_3 = [1,1,1,1]
print(distributeCandies(input_3) == 1)

#sis = [1,2,3] or [2,3,4] or etc. will always have 3 diff candies
input_4 = [1,2,3,4,5,6]
print(distributeCandies(input_4) == 3)
