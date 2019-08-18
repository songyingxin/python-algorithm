


def  is_right(n, nums):
    nums = sorted(nums)
    delay_times = 0

    for i in range(2, len(nums)):

        if nums[i] >= nums[i-1] + nums[i-2]:
            delay_times += 1

    if n - delay_times > 2:
        return True
    else:
        return False

t = int(input())
result = []
for i in range(t):
    n = int(input())
    nums = [int(val) for val in input().split()]
    if is_right(n, nums):
        result.append('YES')
    else:
        result.append('NO')

for val in result:
    print(val)
