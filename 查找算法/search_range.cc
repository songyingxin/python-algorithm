#include <vector>

class Solution
{
  public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        int low = 0, right = nums.size() - 1; // 在[l...r] 的范围里寻找target
        std::vector<int> result;
        while (low <= right)
        {
            int mid = low + (right - low) / 2;
            if (nums[mid] == target)
            {
                cout << mid << endl;
                int result_left = mid;
                while (nums[result_left] == target && result_left - 1 >= 0)
                {
                    result_left--;
                }

                int result_right = mid;
                while (nums[result_right] == target && result_right + 1 <= nums.size() - 1)
                {
                    result_right++;
                }
                if (nums[result_left] == target)
                {
                    result.push_back(result_left);
                }
                else
                {
                    result.push_back(result_left + 1);
                }
                if (nums[result_right] == target)
                {
                    result.push_back(result_right);
                }
                else
                {
                    result.push_back(result_right - 1);
                }
                return result;
            }
            if (nums[mid] < target)
            {
                low = mid + 1; /* target 在[mid+1 ... r] 中 */
            }
            else
            {
                right = mid - 1; /* target 在 [l...mid-1] 中 */
            }
        }

        result.push_back(-1);
        result.push_back(-1);
        return result;
    }
};

int left_bound(std::vector<int> &nums, int target)
{
    int begin = 0;
    int end = nums.size() - 1;

    while (begin <= end)
    {
        int mid = (begin + end) / 2;
        if (target == nums[mid])
        {
            if (mid == 0 || nums[mid - 1] != target)
            {
                return mid;
            }
            end = mid - 1;
        }
        else if (target < nums[mid])
        {
            end = mid - 1;
        }
        else if (target > nums[mid])
        {
            begin = mid + 1;
        }
    }

    return -1;
}

int right_bound(std::vector<int> &nums, int target)
{
    int begin = 0;
    int end = nums.size() - 1;

    while (begin <= end)
    {
        int mid = (begin + end) / 2;
        if (target == nums[mid])
        {
            if (mid == nums.size() - 1 || nums[mid + 1] != target)
            {
                return mid;
            }
            begin = mid + 1;
        }
        else if (target < nums[mid])
        {
            end = mid - 1;
        }
        else if (target > nums[mid])
        {
            begin = mid + 1;
        }
    }
    return -1;
}

class Solution
{
  public:
    vector<int> searchRange(vector<int> &nums, int target)
    {
        std::vector<int> result;
        result.push_back(left_bound(nums, target));
        result.push_back(right_bound(nums, target));
        return result;
    }
};

