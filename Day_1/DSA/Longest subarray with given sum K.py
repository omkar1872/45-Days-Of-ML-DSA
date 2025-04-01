class Solution:
    def longestSubarray(self, arr, k):
        n=len(arr)
        length=0
        for i in range(n):
            summ=0
            for j in range(i,n):
                summ+=arr[j]
                if summ==k:
                    length=max(length,j-i+1)
        return length