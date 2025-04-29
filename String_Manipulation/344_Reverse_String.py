class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]

# s = s[::-1] is invaild because it uses O(n) extra memory
# s.reverse() is also solution, but may be slower