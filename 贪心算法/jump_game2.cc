#include <vector>

class Solution
{
  public:
    int jump(vector<int> &nums)
    {
        if (nums.size() < 2)
        {
            return 0;
        }
        int current_max_index = nums[0];
        int next_max_index = nums[0];
        int result = 1;

        for(int i = 1; i < nums.size(); i++){
            if ( i > current_max_index){
                result++;
                current_max_index = next_max_index;
            }

            if (nums[i] + i > next_max_index){
                next_max_index = nums[i] + i;
            }
        }

        return result;
    }
};