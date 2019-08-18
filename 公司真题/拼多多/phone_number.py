

# line1 = input()
# line2 = input()

line1 = '6 5'
line2 = '787585'

N, K = [int(i) for i in line1.split()]
line2 = [int(i) for i in line2]

result = []

line2_set = set(line2)

min_money = 99999999

for val in line2_set:

    sub_vals = [abs(val - number) for number in line2]
    sort_sub_vals = sorted( list(range(len(sub_vals))), key=lambda x: sub_vals[x] )

    pay_money = sum([sub_vals[i] for i in sort_sub_vals[:K]])
    equal_val = sub_vals[sort_sub_vals[K-1]]

    copy_line2 = line2[:]
    for i in sort_sub_vals[:K-1]:
        copy_line2[i] = val
    
    last_change = None
    for i in range(len(copy_line2)):
        if abs(copy_line2[i]-val) == equal_val:
            last_change = i
    copy_line2[last_change] = val

    copy_line2 = [str(i) for i in copy_line2]
    copy_line2 = ''.join(copy_line2)
    if pay_money > min_money:
        continue
    elif pay_money < min_money:
        result = []
        result.append(copy_line2)
        min_money = pay_money
    else:
        result.append(copy_line2)

result = sorted(result)

print(min_money)
print(result[0])









