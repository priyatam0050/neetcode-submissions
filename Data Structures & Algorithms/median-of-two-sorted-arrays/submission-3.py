class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i=0
        j=0
        sorted_Array=[]
        len_nums1=len(nums1)
        len_nums2=len(nums2)
        if len_nums1>len_nums2:
            k=len_nums1
        else:
            k=len_nums2

        while(i<k or j<k):
            print(i,j)
            if i==len(nums1):
                for p in range(j,len_nums2):
                    sorted_Array.append(nums2[p])
                break
            if j==len(nums2):
                for p in range(i,len_nums1):
                    sorted_Array.append(nums1[p])
                break    
            if(nums1[i]>nums2[j]):
                sorted_Array.append(nums2[j])
                j+=1
            elif(nums1[i]<nums2[j]):
                sorted_Array.append(nums1[i])
                i+=1
            else:
                sorted_Array.append(nums1[i])
                sorted_Array.append(nums2[j])
                i+=1
                j+=1
       

        """list3=nums1+nums2
        list3.sort()"""
        list3=sorted_Array
        len1=len(list3)%2
        len2=int(len(list3)/2)
        if len1==1:
                return list3[len2]
        else:
            return (list3[len2]+list3[len2-1])/2

        
        