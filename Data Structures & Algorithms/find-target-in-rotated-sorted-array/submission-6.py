class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        if len(nums)==1 and target==nums[0]:
            return 0
        elif len(nums)==1:
            return -1
        
        while l<=r:
            if nums[l]==target:
                return l
            if nums[r]==target:
                return r
            l+=1
            r-=1
        return -1


        