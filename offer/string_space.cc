class Solution
{
  public:
    void replaceSpace(char *str, int length)
    {
        if(str == nullptr || length <= 0)
        {
            return;
        }

        // 计算替换后字符串的长度
        int origin_length = 0;
        int number_of_blank = 0;

        int i = 0;
        while(str[i] != '\0')
        {
            ++origin_length;
            if(str[i] == ' ')
            {
                ++number_of_blank;
            }
            ++i;
        }

        int new_length = origin_length + number_of_blank * 2;
        if (new_length > length)
        {
            return;
        }

        // 替换字符串
        int index_of_origin = origin_length;  
        int index_of_new = new_length;

        while(index_of_origin >= 0 && index_of_new > index_of_origin)
        {
            if(str[index_of_origin] == ' ')
            {
                str[index_of_new--] = '0';
                str[index_of_new--] = '2';
                str[index_of_new--] = '%';
            }
            else
            {
                str[index_of_new--] = str[index_of_origin];
            }
            --index_of_origin;
        }
    }
};