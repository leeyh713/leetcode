class Solution:
    def isPalindrome(self, x: int) -> bool:
        c1 = str(x)
        c2 = c1[::-1]
        if c1 == c2:
            return True
        return False