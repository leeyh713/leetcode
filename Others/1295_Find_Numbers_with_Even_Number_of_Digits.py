class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        even_cnt = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                even_cnt += 1
        return even_cnt