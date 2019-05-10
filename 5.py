# find all permutations of arrya


class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        start = 0
        end = len(nums) - 1
        res = []
        self.permutation(nums, start, end, res)
        print(res)

    def permutation(self, nums, start, end, res):
        if start == len(nums):
            res.append(nums.copy())
            return

        for i in range(start, end + 1):
            nums[i], nums[start] = nums[start], nums[i]
            self.permutation(nums, start + 1, end, res)
            nums[i], nums[start] = nums[start], nums[i]


s = Solution()

s.permute([1, 2, 3])
