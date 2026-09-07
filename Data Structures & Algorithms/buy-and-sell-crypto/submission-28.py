class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        minbuy=prices[0]
        for p in prices:
            
            minbuy=min(minbuy,p) 
            maxp=max(maxp,p-minbuy)
            
        return maxp
      

        