class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        list3=nums1+nums2
        list3.sort()
        len1=len(list3)%2
        len2=int(len(list3)/2)
        if len1==1:
                return list3[len2]
        else:
            return (list3[len2]+list3[len2-1])/2

        
        