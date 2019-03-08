#include <queue>


class Solution
{
  public:
    int findKthLargest(vector<int> &nums, int k)
    {
        std::priority_queue<int, std::vector<int>, std::greater<int>> help;

        for(int i = 0; i < nums.size(); i++){
            if (help.size() < k){
                help.push(nums[i]);
            }
            else{
                if (help.top() < nums[i]){
                    help.pop();
                    help.push(nums[i]);
                }
            }
        }
        return help.top();
    }
};