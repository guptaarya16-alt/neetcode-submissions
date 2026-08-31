class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currentlow=prices[0]
        proft=[]
        for i in range(len(prices)):
            if prices[i]<currentlow:
                currentlow=prices[i]
            profit=prices[i]-currentlow
            proft.append(profit)
            maxprofit=max(proft)
               
        return maxprofit
        
            
                   