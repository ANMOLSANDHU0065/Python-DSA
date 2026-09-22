# Longest Common Prefix


class Solution:
    def longestCommonPrefix(self, strs):
        prefix = strs[0]

        for word in strs[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]

                if prefix == "":
                    return ""

        return prefix