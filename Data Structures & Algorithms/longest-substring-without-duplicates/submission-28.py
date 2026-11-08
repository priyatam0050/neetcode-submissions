class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        rest_len=len(set(list(s)))
        res_list=[]
        max_len=0
        uniq=True
        l=0
        r=0
        len_s=len(s)
        lis=s.split(" ")
        if len_s==0 or len_s==1:
            return len_s
        k=' '
        while l<len_s:
            #print(res_list)
            if r==len_s:
                l+=1
                r=l
                continue

            if s[r]==' ':
                if k not in res_list:
                    res_list.append(k)
                    r+=1
                else:
                    max_len=max(max_len,len(res_list))
                    res_list=[]
                    l+=1
                    r=l
                    if max_len>(len_s-l) or max_len==rest_len:
                        return max_len
            elif s[r] not in res_list:
                res_list.append(s[r])
                r+=1
            else:
                max_len=max(max_len,len(res_list))
                res_list=[]
                l+=1
                r=l
                if max_len>(len_s-l) or max_len==rest_len:
                        return max_len
        return max_len

                