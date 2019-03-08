#include <queue>


class MedianFinder
{
  public:
    /** initialize your data structure here. */
    MedianFinder()
    {
    }

    void addNum(int num)
    {
         
    }

    double findMedian()
    {
        
    }

    private:
        std::priority_queue<int> max_heap;
        std::priority_queue<int, std::vector<int>, std::greater<int>> min_heap;
};