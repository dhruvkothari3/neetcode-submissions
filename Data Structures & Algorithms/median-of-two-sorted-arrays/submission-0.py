class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:

        arr = nums1 + nums2
        arr.sort()

        length = len(arr)
        mid = length // 2

        if length % 2 == 1:
            return float(arr[mid])

        return (arr[mid - 1] + arr[mid]) / 2