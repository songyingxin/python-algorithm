#include <vector>

class Solution
{
  public:
    bool canJump(vector<int> &nums)
    {
        int jump = 0;
        int max_index = nums[0];

        while (jump < nums.size() && jump <= max_index)
        {
            int cur_index = nums[jump] + jump;

            if (cur_index > max_index)
            {
                max_index = cur_index;
            }
            jump++;
        }

        if (max_index >= nums.size() - 1)
        {
            return true;
        }

        return false;
    }
};