#include<set>

class Solution
{
  public:
    int lengthOfLongestSubstring(string s)
    {
        if (s.size() < 2){
            return s.size();
        }

        int max_length = 1;

        for (i = 1; i < s.size(); i++){
            std::set<char> s_set;
            for (j = i; j >= 0;  j--){
                if (s_set.find(s[j]) == s_set.end()){
                    s_set.insert(s[j]);
                }
                else{
                    break;
                }
            }

            if(max_length < s_set.size()){
                max_length = s_set.size();
            }
        }

        return max_length;
    }
};

class Solution
{
  public:
    int lengthOfLongestSubstring(string s)
    {
        int begin = 0;
        int result = 0;
        std::string word = "";
        int char_map[128] = {0};
        for(int i = 0; i < s.length(); i++){
            char_map[s[i]]++;
            if (char_map[s[i]] == 1){
                word += s[i];
                if (result < word.length()){
                    result = word.length();
                }
            }
            else{
                while (begin < i && char_map[s[i]] > 1)
                {
                    char_map[s[begin]]--;
                    begin++;
                }
                word = "";
                for (int j = begin; j <= i; j++){
                    word += s[j];
                }
            }
        }

        return result;
    }
};