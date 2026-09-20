
# Reverse-degree-of-a-string


class Solution:
    def reverseDegree(self, s):
        total = 0

        for i in range(len(s)):
            value = 26 - (ord(s[i]) - ord('a'))
            total += value * (i + 1)

        return total