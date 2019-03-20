#include <vector>

class Solution
{
  public:
    int wiggleMaxLength(vector<int> &nums)
    {
        if (nums.size() < 2)
        {
            return nums.size();
        }

        int pre = 0;
        int pre_val = nums[0];
        int result = 1;
        for (int i = 1; i < nums.size(); i++)
        {
            int cur;
            if (nums[i] - pre_val > 0)
            {
                cur = 1;
            }
            else if (nums[i] - pre_val < 0)
            {
                cur = -1;
            }
            else
            {
                continue;
            }

            if (pre == cur)
            {
                pre_val = nums[i];
                continue;
            }
            else
            {
                pre = cur;
                result++;
                pre_val = nums[i];
            }
        }

        return result;
    }
};


class Solution{

public: 
    int wiggleMaxLength(std::vector<int> & nums){
        if (nums.size() < 2){
            return nums.size();
        }

        static const int BEGIN = 0;
        static const int UP = 1;
        static const int DOWN = 2;

        int STATE = BEGIN;
        int max_length = 1;

        for (int i = 1; i < nums.size(); i++){
            switch (STATE)
            {
                case BEGIN:
                    if (nums[i] > nums[i-1] ){
                        STATE = UP;
                        max_length++;
                    }
                    else if (nums[i] < nums[i-1]){
                        STATE = DOWN;
                        max_length++;
                    }
                    break;

                case UP:
                    if (nums[i] < nums[i-1]){
                        STATE = DOWN;
                        max_length++;
                    }
                    break;
                case DOWN:
                    if (nums[i] > nums[i-1]){
                        STATE = UP;
                        max_length++;
                    }
                    break;
                default:
                    break;
            }
        }
        return max_length;
    }
};