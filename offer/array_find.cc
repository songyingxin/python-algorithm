class Solution
{
  public:
    bool Find(int target, vector<vector<int>> array)
    {
        bool flag = false;
        if (array.size() != 0){
            int rows = array.size();
            int columns = array[0].size();

            int row = 0;
            int column = columns - 1;

            while(row < rows && column >= 0)
            {
                if(array[row][column] == target)
                {
                    flag = true;
                    break;
                }
                else if (array[row][column] > target)
                {
                    --column;
                }
                else
                {
                    ++row;
                }
                
            }
        }
        return flag;
    }
};