class Solution:
    def minWindow(self, s: str, t: str) -> str:
       windows={}
       need=Counter(t)
       l=0
       have=0
       required=len(t)
       result=""
       for r,ch in enumerate(s):
            
            windows[ch]=1+windows.get(ch,0)
            #print(windows[ch],need[ch])
            if ch in need and windows[ch]<=need[ch]:
                have+=1
            #print(have,required)
            while have==required:
                #print(s[l:r+1])
                if result=="" or r-l+1<len(result):
                    result=s[l:r+1]
                out=s[l]
                windows[out]-=1
                if out in need and windows[out]<need[out]:
                    have-=1
                l+=1
                
       return result
            
            
      
    