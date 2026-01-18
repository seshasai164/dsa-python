class Solution:
    def frequencyLookup(self, nums, m):
        freq = {}

        # build frequency map from nums
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # collect frequency for elements in m
        result = []
        for x in m:
            result.append(freq.get(x, 0))

        return result
nums = [5, 3, 2, 2, 1, 5, 57, 5, 10]
m = [10, 11, 1, 9, 5, 6, 7, 2]

s = Solution()
print(s.frequencyLookup(nums, m))
