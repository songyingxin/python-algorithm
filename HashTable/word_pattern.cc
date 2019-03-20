#include <map>
class Solution
{
  public:
    bool wordPattern(string pattern, string str)
    {
        std::map<std::string,char> word_map;
        char used[128] = {0};  // 记录 pattern中的字符是否用过
        std::string word;
        int pos = 0;
        str.push_back(' ');

        for (int i = 0; i < str.length(); i++){
            if(str[i] == ' '){
                if (pos == pattern.length()){
                    return false;
                }
                if (word_map.find(word) == word_map.end()){
                    if (used[pattern[pos]]){
                        return false;
                    }
                    word_map[word] = pattern[pos];
                    used[pattern[pos]] = 1;
                }
                else{
                    if (word_map[word] != pattern[pos]){
                        return false;
                    }
                }
                word = "";
                pos++;
            }
            else{
                word += str[i];
            }
        }
        if (pos != pattern.length()){
            return false;
        }

        return true;
    }
};