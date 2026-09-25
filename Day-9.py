
#   FIND MISSING ELEMENT...


class Solution:
    def findMissingElements(self, nums):
        minimum = min(nums)
        maximum = max(nums)

        missing = []

        for i in range(minimum, maximum + 1):
            if i not in nums:
                missing.append(i)

        return missing