


def get_result(string):

    stack = []
    index = 0
    while index < len(string):
        if string[index] == '(' or string[index].isalpha():
            stack.append(string[index])
            index += 1
        elif string[index] == ')':
            tmp = []
            while stack:
                val = stack.pop()
                if val == '(':
                    break
                else:
                    tmp.append(val)
            index += 1
            times = int(string[index])
            index += 1
            while index < len(string) and string[index].isdigit():
                times = times * 10 + int(string[index])
                index += 1
            tmp *= times
            stack.extend(tmp[::-1])
        else:
            tmp = []
            val = stack.pop()
            times = int(string[index])
            index += 1
            while index < len(string) and string[index].isdigit():
                times = times * 10 + int(string[index])
                index += 1
            stack.extend([val] * times)
    return ''.join(stack)

print(get_result('A11B'))
print(get_result('(AA)2A'))
print(get_result('((A2B)2)2G'))
print(get_result('(YUANFUDAO)2JIAYOU'))
print(get_result('A2BC4D2'))




# C = int(input())

# for i in range(C):
