class Solution:
    def findMin(self, nums: List[int]) -> int:
        i=0


        while True and i<len(nums)-1:
            if nums[i+1]>nums[i]:
                i+=1
            else:
                return nums[i+1]
        return nums[0]
        