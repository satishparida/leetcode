class Solution:

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ret = []
        nums.sort()
        for i in range(0, len(nums)):
            a1 = nums[i]
            if i>0 and nums[i]==nums[i-1]:
                continue
            j=i+1
            k=len(nums)-1
            while j < k:
                a2 = nums[j]
                a3 = nums[k]
                total = nums[i] + nums[j] + nums[k]
                if total == 0:
                        ret.append([nums[i], nums[j], nums[k]])
                        j += 1
                        while j<k and nums[j]==nums[j-1]:
                            j += 1
                elif total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
        return ret
    
s = Solution()
s.threeSum([-1,-1,-1,0,1,2,-1,-4,0,2,3])