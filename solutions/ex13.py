'''
You are given a positive integer N which represents the number of steps
in a staircase. You can either climb 1 or 2 steps at a time. Write a function
that returns the number of unique ways to climb the stairs
'''
import math


def staircase(n):
    spaces = n//2 + n % 2
    num2 = n//2
    answer = 0
    while(spaces <= n):
        answer += math.factorial(spaces) / \
            (math.factorial(spaces-num2)*math.factorial(num2))
        num2 -= 1
        spaces += 1
    return answer


print(staircase(4))
# 5

print(staircase(5))
# 8
