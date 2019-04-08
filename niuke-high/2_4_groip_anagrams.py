class Solution:
    def groupAnagrams(self, strs):

        sort_strs = [str(sorted(val)) for val in strs]
        help_dict = {}
        for i in range(len(sort_strs)):

            if sort_strs[i] in help_dict.keys():
                help_dict[sort_strs[i]].append(strs[i])
            else:
                help_dict[sort_strs[i]] = [strs[i]]

        result = []
        for val in help_dict.values():
            result.append(val)

        return result
