class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l=0
        s1_list=list(s1)
        s1_count={}
        for i in s1_list:
            s1_count[i]=s1_list.count(i)
        print(s1_count)

        s1_len=len(s1)
        s2_len=len(s2)
        r=s1_len
        k=list(s1)
        while l<s2_len:
            #print(k)
            #print(l,r)
            k=s2[l:r]
            k_count={}
            for i in s1_list:
                k_count[i]=k.count(i,0)
            count=0
            #print(k_count)
            for i in s1_list:
                if k_count[i]==s1_count[i]:
                    count+=1
            if count==s1_len:
                return True

            l+=1
            r=l+s1_len
        return False

