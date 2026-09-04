class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r= 0, len(heights)-1
        biggest=0
        while l<r:
            if heights[l]<heights[r]:
                hite=heights[l]
                width=r-l
                A=hite*width
                l+=1
            
            else:
                hite=heights[r]
                width=r-l
                A=hite*width
                r-=1
            biggest=max(biggest,A)
        return biggest