
# 俄罗斯方块

line_1 = input()
line_2 = input()

# line_1 = '3 9'
# line_2 = '1 1 2 2 2 3 1 2 3'

N, M = [int(val) for val in line_1.split()]
nums = [int(val) for val in line_2.split()]

result = [0 for _ in range(N)]

for val in nums:
    result[val-1] += 1

print(min(result))
