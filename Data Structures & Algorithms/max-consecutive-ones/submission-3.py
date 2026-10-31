class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == 0:
                    break
                else:
                    cnt += 1
            res = max(res, cnt)
        
        return res