# binary search in rotated array


class Solution:

    def search_right(self, nums: [], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if mid == len(nums) - 1:
                    return mid

                if nums[mid] == nums[mid + 1]:
                    left = mid + 1
                    continue
                else:
                    return mid

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def search_left(self, nums: [], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                if mid == 0:
                    return mid

                if nums[mid] == nums[mid - 1]:
                    right = mid - 1
                    continue
                else:
                    return mid

            if target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return -1

    def search_range(self, nums: [], target: int) -> []:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        right_idx = self.search_right(nums, target)
        left_idx = self.search_left(nums, target)
        return [left_idx, right_idx]


s = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
res = s.search_range(nums, target)
print(res)
