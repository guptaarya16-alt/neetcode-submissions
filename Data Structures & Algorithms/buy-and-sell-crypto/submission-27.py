class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minbuy=prices[0]
        for p in prices:
            maxp=max(maxp,p-minbuy)
            minbuy=min(minbuy,p) 
            
        return maxp
      

        