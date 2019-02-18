class Solution(object):
    def twosum(self,nums,target):
        h = {}
        for i,num in enumerate(nums):
            n = target - num
            if n in h:
                return [h[n],i]
            h[num] = i

s = Solution()
print(s.twosum([2,7,11,15],9))

