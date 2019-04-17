#include <vector>
#include <iostream>

using namespace std;


class BubbleSort
{
    public:
        // 从前往后冒
        void bubbleSort(vector<int> &arr)
        {
            if (arr.size() < 2)
            {
                return;
            }

            for (int end = arr.size()-1; end > 0; end--)
            {
                for (int start=0; start < end; start++)
                {
                    if (arr[start] > arr[start+1])
                    {
                        swap(arr[start], arr[start+1]);
                    }
                }
            }
        }

        void bubbleSort2(vector<int> &arr)
        {
            if (arr.size() < 2)
            {
                return;
            }

            for (int start = 0; start < arr.size(); start++)
            {
                for (int i=arr.size()-1; i >= start; i--)
                {
                    if (arr[i] > arr[i+1])
                    {
                        swap(arr[i], arr[i+1]);
                    }
                }
            }
        }


};



int main()
{
    vector<int> arr = { 2,5,1,5,8,2,12,4,78,43};
    //vector<int> arr = {};

    BubbleSort algo;
    algo.bubbleSort2(arr);
    for (std::vector<int>::iterator m = arr.begin(); m != arr.end(); m++) //用迭代器的方式输出容器对象的值
    {
        cout << *m << endl;
    }
}