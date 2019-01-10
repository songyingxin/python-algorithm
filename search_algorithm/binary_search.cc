#include <iostream>
#include <cmath>
#include <ctime>
#include <cassert>

using namespace std;

template<typename T>

int binary_search(T arr[], int n, T target){

    int l = 0, r = n - 1;  // 在[l...r] 的范围里寻找target

    while (l <= r){    // 当 l == r 时， 区间[l...r] 依然是有效的

        // int mid = (l+r)/2;  // 可能会导致整型溢出
        int mid = l + (r-l)/2;

        if (arr[mid] == target){
            return mid;
        }

        if (arr[mid] < target){
            l = mid + 1;    /* target 在[mid+1 ... r] 中 */
        }
        else{
            r = mid - 1;   /* target 在 [l...mid-1] 中 */
        }
    }
  
    return -1;  
}



