'''
You are given a list of numbers, and a target number k.
Return whether or not there are two numbers in the list that
add up to k.

Example:
Given [4, 7, 1, -3, 2] and k=5
return true since 4 + 1 = 5
'''


def two_sum(list, k):
    comp = []
    for el in list:
        if el in comp:
            return print("True")
        else:
            comp.append(k-el)
    return print("False")


two_sum([4, 7, 1, -3, 2], 5)
