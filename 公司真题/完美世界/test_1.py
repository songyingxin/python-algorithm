N = int(input())

nums = [int(val) for val in input().split()]

val = int(input())

dp = [1000000 for _ in range(val + 1)]

dp[0] = 0
for num in nums:
    dp[num] = 1

for i in range(val + 1):
    for num in nums:
        dp[i] = min(dp[i], dp[i-num] + 1)

if dp[-1] == 1000000:
    print(-1)
else:
    print(dp[-1])
