class Solution:
    def twoSum(self, nums: List[int], target: int):
        arr = []

        # Store value with its original index
        for i in range(len(nums)):
            arr.append([nums[i], i])

        # Sort by value
        arr.sort()

        start = 0
        end = len(arr) - 1

        while start < end:
            total = arr[start][0] + arr[end][0]

            if total == target:
                if total == target:
                    return sorted([arr[start][1], arr[end][1]])
            elif total < target:
                start += 1
            else:
                end -= 1