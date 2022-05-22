


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ops = set(['+', '-', '*', '/'])
        op_to_binary_fn = {
            "+": add,
            '-': sub,
            '*': mul,
            '/': lambda x,y: int(x/y)
        }

        stack = list()
        for token in tokens:
            if token in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                num = op_to_binary_fn[token](num1, num2)
            else:
                num = int(token)
            stack.append(num)

        return stack[0]


