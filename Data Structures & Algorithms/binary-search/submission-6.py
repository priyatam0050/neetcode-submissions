class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i=0
        j=len(nums)-1
        k=int((i+j)/2)
        if len(nums)==1 and nums[0]==target:
            return 0
        elif len(nums)==1:
            return -1
        if len(nums)==2 and nums[0]==target:
            return 0
        elif len(nums)==2 and nums[1]==target:
            return 1
        elif len(nums)==2:
            return -1
        while target!=nums[k]:
            k=int((i+j)/2)
           
            if abs(i-j)==1:
                if target==nums[i]:
                    return i
                elif target==nums[j]:
                    return j
                return -1
            if target>nums[k]:
                i=k
            elif target<nums[k]:
                j=k
            elif target==nums[k]:
                return k
           
           
        return k