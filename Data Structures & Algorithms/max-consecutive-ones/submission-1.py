class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = cnt = 0
        n = len(nums)
        
        for i in range(n):
            if (nums[i] == 0):
                cnt = 0
            else:
                cnt += 1
            res = max(res, cnt)
        
        return res
        