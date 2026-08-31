class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        openp=["(","{","["]
        closedp=[")","}","]"]
        for i in range(len(s)):
            current=s[i]
            if current in openp:
                stack.append(current)
            elif current in closedp:
                if stack==[]:
                    return False 
                if current==")" and stack[-1]=="(":
                    stack.pop()
                elif current=="]" and  stack[-1]=="[":
                    stack.pop()
                elif current=="}" and stack[-1]=="{":
                    stack.pop() 
                else:
                    return False  
        if stack==[]:
            return True
            
        else:
            return False
            

            
        