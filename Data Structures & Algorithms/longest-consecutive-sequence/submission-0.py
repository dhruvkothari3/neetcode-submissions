class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        nums = sorted(nums)

        count = 1
        max_count = 1

        i = 0
        j = 1

        while j < len(nums):

            if nums[j] == nums[i] + 1:
                count = count + 1

            elif nums[j] == nums[i]:
                pass

            else:
                count = 1

            max_count = max(max_count, count)

            i = j
            j = j + 1

        return max_count