'''
Given two strings, determine the edit distance between them.
The edit distance is defined as the minimum number of edits
(insertion, deletion or subtitution) needed to change on string
to the other.

For example, "biting" and "sitting" have an edit distance of 2
(substitute b for s, and insert a t).
'''


def distance(s1, s2):
    m = len(s1)
    n = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[j - 1] == s2[i - 1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])

    return dp[-1][-1]


print(distance('biting', 'sitting'))
# 2
