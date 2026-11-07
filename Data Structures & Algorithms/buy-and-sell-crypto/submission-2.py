class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_ele=prices[0]
        max_pro=0
        for i in prices:
            max_pro=max(max_pro,i-min_ele)
            min_ele=min(min_ele,i)
        
            
        return max_pro


        