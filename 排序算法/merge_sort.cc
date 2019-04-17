#include <iostream>

using namespace std;


// 将arr[l...mid] 和 arr[mid+1...r] 两部分进行归并
template<typename T> 
void __merge(T arr[], int l, int mid, int r){
    T aux[r-l+1];

    for (int i = l; i <=r; i++){
        aux[i-l] = arr[i];
    }

    int i = l, j = mid+1;
    for (int k = l; k <= r; k++){

        if (i > mid){
            arr[k] = aux[j-l];
            j++;
        }
        else if (j>r) {
            arr[k] = aux[i - l];
            i++;
        }
        else if(aux[i-l] < aux[j-l]){
            arr[k] = aux[i-l];
            i++;
        }
        else{
            arr[k] = aux[j-l];
            j++;
        }
    }
}

// 递归使用归并排序，对arr[l...r] 的范围进行排序
template<typename T> 
void  __mergeSort(T arr[], int l , int r){
    if( l >= r)
        return;

    // // 元素较少时，采用插入排序
    // if (r - l <= 15){
    //     insertSort(arr, l, r);
    //     return;
    // }

    int mid = (l+r)/2;

    __mergeSort(arr, l, mid);
    __mergeSort(arr, mid+1, r);
    if (arr[mid] > arr[mid+1])  
        __merge(arr, l, mid, r);
}

template<typename T> 
void mergeSort(T arr[], int n){
    __mergeSort(arr, 0, n-1);
}



// 自底向上的归并排序： 可以在O(nlogn) 对链表进行排序
template<typename T> 
void mergeSortBU( T arr[], int n){
    for( int sz = 1; sz <= n; sz += sz){
        for( int i = 0; i + sz < n; i += sz + sz){
            // 对arr[i...j+sz-1] 和 arr[i+sz...i+2*sz-1] 进行归并  
            __merge(arr, i, i+sz-1, min(i+sz+sz-1, n-1));
        }
    }
}

int main()
{
    int a[10] = {
        10,
        9,
        8,
        4,
        3,
        2,
        17,
        6,
        5,
    };
    mergeSortBU(a, 10);
    for (int i = 0; i < 10; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}