
# Find-x-value-of-array-i


class Solution:
    def resultArray(self, nums, k):
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k
            r = num % k

            new_dp[r] += 1

            for rem in range(k):
                if dp[rem]:
                    new_dp[(rem * r) % k] += dp[rem]

            dp = new_dp

            for rem in range(k):
                result[rem] += dp[rem]

        return result