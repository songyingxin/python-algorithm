

n = int(input())
nums = [int(val) for val in input().split()]

judge = {}

for i in range(1, n+1):
    judge[i] = n - i + 1


result = [0 for _ in range(n)]

for i in range(n):
    result[i] = judge[nums[i]]

result = [str(val) for val in result]
print(' '.join(result))