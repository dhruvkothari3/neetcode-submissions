from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        answer = []

        for num, frequency in count.most_common(k):
            answer.append(num)

        return answer