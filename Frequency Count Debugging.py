class Solution:
    def __init__(self):
        self.nums = [5, 6, 7, 11, 9, 5, 1, 1, 1]
        self.frequency = {}

        for i in range(len(self.nums)):
            if self.nums[i] in self.frequency:
                self.frequency[self.nums[i]] += 1
            else:
                self.frequency[self.nums[i]] = 1


# create object
obj = Solution()

# access frequency
print(obj.frequency)
