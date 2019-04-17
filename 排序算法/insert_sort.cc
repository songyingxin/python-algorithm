#include <iostream>

using namespace std;

template<typename T>
void insertSort(T arr[], int n){

    for (int i = 1; i < n; i++){
        // for(int j=i; j>0 && arr[j] < arr[j-1]; j--){
        //     swap(arr[j], arr[j-1]);
        // }

        /* 将交换操作改为赋值操作可以提高效率 */

        T key = arr[i];
        int j;
        for (j = i; j > 0 && arr[j-1] > key; j--)
        {
            arr[j] = arr[j - 1];
        }
        arr[j] = key;
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
    insertSort(a, 10);
    for (int i = 0; i < 10; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}