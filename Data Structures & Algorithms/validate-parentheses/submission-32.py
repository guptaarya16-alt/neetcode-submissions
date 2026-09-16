class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        thing= {'(': ')', '{': '}', '[' : ']'}
        for i in s:
            if i in thing:
                stack.append(i)
            else:
                if not stack:
                    return False
                else:
                    if thing[stack[-1]] == i:
                        stack.pop()
                    else:
                        return False
                
        if not stack:
            return True
        else:
            return False



                
            
        