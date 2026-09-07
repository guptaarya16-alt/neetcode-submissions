class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        
        l,r= 0, len(height)-1
        MaxL,MaxR=height[l],height[r]
        calc=0
        while l<r:
            if MaxL<MaxR:
                l+=1
                MaxL=max(MaxL,height[l])
                calc += MaxL-height[l]
            else:
                r-=1
                MaxR=max(MaxR, height[r])
                calc+= MaxR-height[r]
        return calc
                    
                
                


         
        
        
        
                 