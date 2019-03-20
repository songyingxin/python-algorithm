#include <vector>
#include <string>

class Solution
{
  public:
    vector<vector<string>> groupAnagrams(vector<string> &strs)
    {
        std::map<std::string, std::vector<std::string>> anagram;
        std::vector<std::vector<std::string>> result;

        for (int i = 0; i < strs.size(); i++){
            std::string str = strs[i];
            std::sort(str.begin(), str.end());

            if (anagram.find(str) == anagram.end()){
                std::vector<std::string> item;
                anagram[str] = item;
            }
            anagram[str].push_back(strs[i]);
        }

        std::map<std::string, std::vector<std::string>>::iterator it;
        for (it = anagram.begin(); it != anagram.end(); it++){
            result.push_back((*it).second);
        }

        return result;
    }
};