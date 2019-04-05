class Solution:
    def lemonadeChange(self, bills):

        money = {
            5:0,
            10:0,
            20:0
        }

        for val in bills:
            if val == 5:
                money[5] += 1
            
            if val == 10:
                if money[5] == 0:
                    return False
                else:
                    money[5] -= 1
                    money[10] += 1
            if val == 20:
                # 思路1：贪心策略
                change = 15
                while(change >= 10 and money[10] != 0):
                    change -= 10
                    money[10] -= 1
                
                while(change >= 5 and money[5] != 0):
                    change -= 5
                    money[5] -= 1

                if change != 0:
                    return False

                # 思路2：
                # if money[5] == 0:
                #     return False
                # elif money[5] * 5 + money[10] * 10 < 15:
                #     return False
                # else:
                #     if money[10] == 0:
                #         money[5] -= 3
                #     else:
                #         money[10] -= 1
                #         money[5] -= 1
        
        return True

if __name__ == "__main__":
    
    bills = [5,5,5,10, 20]
    print(Solution().lemonadeChange(bills))
