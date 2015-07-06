"""
Longest Common Subsequence
ex input)
 ABCDBDD VBDDSD
"""
n, m = map(int, input().split())
s_str = input()
b_str = input()
dp = [[0 for i in range(m + 1)] for i in range(n + 1)]
for i in range(n):
    for j in range(m):
        if s_str[i] == b_str[j]:
            print(s_str[i], b_str[j], i, j)
            dp[i + 1][j + 1] = dp[i][j] + 1
        else:
            dp[i + 1][j + 1] = max(dp[i][j+1], dp[i+1][j])

print(dp[n][m])
