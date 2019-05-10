class Solution:
    def canJump(self, nums) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        res = self.jump(nums, 0)
        return res

    def jump(self, nums, index) -> bool:
        if index == len(nums) - 1:
            return True

        dist = nums[index]
        end = min(index + dist, len(nums) - 1)

        for j in range(index + 1, end + 1):
            if self.jump(nums, j):
                return True

        return False


s = Solution()

nums = [3, 2, 1, 0, 4]
print(s.canJump(nums))
