class Solution:
    def hasCycle(self):
        nums = [5,3,2,2,1,5,57,5,10]
        m = [10,11,1,9,5,6,7,2]

        hash_list = [0] * 11   # index 0–10

        for num in nums:
            if 0 <= num <= 10:
                hash_list[num] += 1

        result = []

        for num in m:
            if 0 <= num <= 10:
                result.append(hash_list[num])
            else:
                result.append(0)

        return result
s = Solution()
output = s.hasCycle()
print(output)
