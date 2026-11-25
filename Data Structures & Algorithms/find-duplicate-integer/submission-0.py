class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        k=[]

        for i in nums:

            if i in k:
                return i
            k.append(i)

            
        