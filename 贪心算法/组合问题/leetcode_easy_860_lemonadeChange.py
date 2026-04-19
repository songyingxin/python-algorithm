class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

      five = 0
      ten = 0

      for val in bills:
        if val == 5:
          five += 1
        elif val == 10:
          five -= 1
          ten += 1
        else:
          if ten > 0:
            ten -= 1
            five -= 1
          else:
            five -= 3
        
        if five < 0:
          return False
      
      return True
  
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:

        help_dict = {
            5:0,
            10:0
        }

        for num in bills:
            if num == 5:
                help_dict[5] += 1
            if num == 10:
                if help_dict[5] == 0:
                    return False
                else:
                    help_dict[10] += 1
                    help_dict[5] -= 1
            if num == 20:
                if help_dict[10] != 0:
                    help_dict[10] -= 1
                    if help_dict[5] > 0:
                        help_dict[5] -= 1
                    else:
                        return False
                else:
                    if help_dict[5] < 3:
                        return False 
                    else:
                        help_dict[5] -= 3
        return True