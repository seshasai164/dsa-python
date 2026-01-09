class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        num = x
        result = 0
        while num > 0:
            result = result * 10 + num % 10
            num //= 10
        
        return x == result
