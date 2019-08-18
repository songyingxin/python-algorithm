
n = input()
nums = input()
nums = [int(val) for val in nums.split()]

is_all_odd = True
for val in nums:
    if val % 2 == 0:
        is_all_odd = False
        break

is_all_ou = True
for val in nums:
    if val % 2 != 0:
        is_all_ou = False
        break

if is_all_odd or is_all_ou:
    pass
else:
    nums = sorted(nums)

nums = [str(val) for val in nums]
print(' '.join(nums))
