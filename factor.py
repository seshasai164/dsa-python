from math import isqrt

class Solution:
    def factors(self, n):
        result = []

        for i in range(1, isqrt(n) + 1):
            if n % i == 0:
                result.append(i)
                if i != n // i:
                    result.append(n // i)

        return sorted(result)

s = Solution()
print(s.factors(108))   # prints the list of factors
