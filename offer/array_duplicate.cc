class Solution
{
  public:
    bool duplicate(int numbers[], int length, int *duplication)
    {
        // 参数检查
        if (numbers == nullptr || length <= 0)
        {
            return false;
        }
        // 条件检查
        for (int i = 0; i < length; ++i)
        {
            if (numbers[i] < 0 || numbers[i] > length - 1)
            {
                return false;
            }
        }

        // 核心代码
        int hashTable[255] = {0};

        for(int i = 0; i < length; i++)
        {
            hashTable[numbers[i]]++;
            if (hashTable[numbers[i]] > 1)
            {
                *duplicate = numbers[i];
                reeturn true;
            }
        }

        return false;
    }
};

class Solution
{
  public:
    bool duplicate(int numbers[], int length, int *duplication)
    {
        // 参数检查
        if (numbers == nullptr || length <= 0)
        {
            return false;
        }
        // 条件检查
        for (int i = 0; i < length; ++i)
        {
            if (numbers[i] < 0 || numbers[i] > length - 1)
            {
                return false;
            }
        }

        // 核心代码
        for (int i = 0; i < length; ++i)
        {
            while (numbers[i] != i)
            {
                if (numbers[i] == numbers[numbers[i]])
                {
                    *duplication = numbers[i];
                    return true;
                }

                int tmp = numbers[i];
                numbers[i] = numbers[tmp];
                numbers[tmp] = tmp;
            }
        }

        return false;
    }
};
