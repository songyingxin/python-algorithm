class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        dict_arr = {}
        str_list = str.split()
        pattern_set = set()

        if len(str_list) != len(pattern):
            return False

        for i in range(len(str_list)):
            if str_list[i] in dict_arr:
                if pattern[i] != dict_arr[str_list[i]]:
                    return False
            elif pattern[i] in pattern_set:
                return False
            else:
                dict_arr[str_list[i]] = pattern[i]

            pattern_set.add(pattern[i])

        return True
