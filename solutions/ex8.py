'''
Given a list of numbersm where every number shows up
twice except for one number, find that one number.

Example:
Input: [4, 3, 2, 4, 1, 3 ,2]
Output: 1
'''

def singleNumber(nums):
    flag = True
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(i == j): 
                continue
            elif(nums[i] == nums[j]):
                flag = False
                break
        if flag:
            return nums[i]
        flag = True



print(singleNumber([4, 3, 2, 4, 1, 3, 2]))
