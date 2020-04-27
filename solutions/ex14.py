'''
Given a list of numbers, find if there exists a pythagorean triplet
in that list.

Example:
Input: [3, 5, 12, 5, 13]
Output: True
'''


def findPythagoreanTriplets(nums):
    for c in nums:
        for b in nums:
            for a in nums:
                if(a**2 + b**2 == c**2):
                    return True
    return False


print(findPythagoreanTriplets([3, 12, 5, 13]))
# True

print(findPythagoreanTriplets([10, 4, 6, 12, 5]))
# False
