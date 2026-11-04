class Solution:
    def search(self, nums: List[int], target: int) -> int:


    
        l,r=0,len(nums)-1

        if len(nums)==1 and target==nums[0]:
            return 0
        elif len(nums)==1:
            return -1

        while l<r:
            m=l+(r-l)//2
            if nums[m]>nums[l]:
                l=m
            else:
                r=m
        print(nums[l])
        if target==nums[l]:
            return l
        res=l+1
        k=nums[:l+1]
        k1=nums[l+1:]
        
        l2,r2=0,len(k)-1
        l3,r3=0,len(k1)-1
        while l2<=r2:
            m2=l2+(r2-l2)//2
            if k[m2]==target:
                return m2
            if k[m2]>target:
                r2=m2-1
            else:
                l2=m2+1
        while l3<=r3:
            m3=l3+(r3-l3)//2
            if k1[m3]==target:
                return res+m3
            if k1[m3]>target:
                r3=m3-1
            else:
                l3=m3+1
        return -1


        