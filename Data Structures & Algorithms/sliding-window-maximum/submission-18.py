class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        res=[]
       
       
        if k==1:
            return nums
        if len(nums)==1:
            res.append(nums[0])
            return res
        if len(nums)==0:
            return res
        max_len=nums[0]

        for r in range(len(nums)-k+1):
            if r==0:
                max_len=max(nums[l:r+k])
            if nums[r+k-1]>max_len:
                max_len=nums[r+k-1]
           
            res.append(max_len)
            
            if max_len==nums[l]:
                max_len=max(nums[l+1:r+k])
           
            l+=1
           
            
        return res
        