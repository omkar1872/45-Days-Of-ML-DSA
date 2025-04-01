class Solution(object):
    def reverseArray(self, nums, start, end):
        n=len(nums)
        while start<end:
            nums[start],nums[end]=nums[end],nums[start]
            start+=1
            end-=1
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        self.reverseArray(nums,0,n-1)
        self.reverseArray(nums,0,k-1)
        self.reverseArray(nums,k,n-1)