'''
Given a list of numbers with only 3 unique numbers
(1, 2, 3), sort the list in O(n) time.

Esse é o 'Dutch national flag problem'

Example:
Input: [3, 3, 2, 1, 3, 2, 1]
Output: [1, 1, 2, 2, 3, 3, 3]
'''


def sortNums(nums):
    mid = 2
    i = 0
    j = 0
    n = len(nums) - 1
    while(j <= n):
        if(nums[j] < mid): # Se for menor, coloco no começo do array da esquerda pra direita
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j += 1
        elif(nums[j] > mid): # Se for maior, coloco no final do array, da direita pra esquerda
            nums[n], nums[j] = nums[j], nums[n]
            n -= 1
        else:
            j += 1
    return nums


print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]
