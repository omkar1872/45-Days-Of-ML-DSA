class Solution:
    def findMaxConsecutiveOnes(self, nums):
        n=len(nums)
        count=0
        maxi=0
        for i in range(n):
            if nums[i]==1:
                count+=1
                maxi=max(maxi,count)
            else:
                count=0
        return maxi
