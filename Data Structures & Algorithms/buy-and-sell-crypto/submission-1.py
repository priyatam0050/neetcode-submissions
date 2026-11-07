class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res=0
        for i,n in enumerate(prices):
            print(n)
            for j in range(i+1,len(prices)):
                if prices[j]>n:
                    print(n,prices[j])
                    temp=prices[j]-n
                    res=max(res,temp)
        return res


        