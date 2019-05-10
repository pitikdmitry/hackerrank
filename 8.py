class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp = [-1 for _ in range(len(nums))]

        for i in range(0, len(nums)):
            if i == 0:
                dp[i] = nums[i]

            elif i == 1:
                dp[i] = max(nums[i - 1], nums[i])

            else:
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

        return max(dp[len(dp) - 1], dp[len(dp) - 2])


s = Solution()
nums = [2, 7, 9, 3, 1]
s.rob(nums)
