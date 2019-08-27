
"""
dp[0][0] = vals[0][0]

dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + vals[i][j]
"""

N = int(input())
M = int(input())

vals = [int(val) for val in input().split()]

result = []

min_val = 1

for i in range(1, N+1):
    result.append(vals[(i-1) * M : i * M])

vals = result

dp = [
    [0 for _ in range(M)]
    for _ in range(N)
]

dp[0][0] = vals[0][0]

for i in range(M):
    dp[0][i] = dp[0][i-1] + vals[0][i]

for j in range(N):
    dp[j][0] = dp[j-1][0] + vals[j][0]

for i in range(1, N):
    for j in range(1, M):
        dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + vals[i][j]

if dp[-1][-1] > 0:
    print(1)
else:
    print(abs(dp[-1][-1]-1))

