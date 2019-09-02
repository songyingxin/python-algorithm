class Solution(object):

    def findNthDigit(self, nth: int) -> int:
        i, max_count = 0, 0
        while max_count < nth:
            i += 1
            max_count += i * ( 9 * 10 ** (i-1))
        
        start_count = max_count - i * (9 * 10 ** (i-1)) # 1000... -- 999...
        power = i - 1 # 最高位位数
        start_val = 10 ** power  # 最高位起始值

        step = nth - start_count - 1 # 剩余移动步数
        step_length = i   # 每增加1 所需要的步长、
        offset, pos = divmod(step, step_length)  # offset: 偏移值， pos： 结果值指向的位数

        curr_val = start_val + offset # 第nth数字所在数值
        result = int(str(curr_val)[pos])
        return result

