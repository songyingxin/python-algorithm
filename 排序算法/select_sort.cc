#include <iostream>

using namespace std;

template<typename T>
void selectionSort( T arr[], int n){
    for(int i=0; i<n; i++){
        // 寻找 [i,n) 区间内 的最小值
        int minIndex = i;
        for (int j = i+1; j < n; j++){
            if(arr[j] < arr[minIndex]){
                minIndex = j;
            }
        }

        swap(arr[i], arr[minIndex]);
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
    selectionSort(a, 10);
    for(int i = 0; i < 10; i++){
        cout<< a[i] << " ";
    }
    cout << endl;
}