class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False
        
        stack = []
        
        start = '[{('
        end = ']})'        
        
        i = 0
        
        while i < len(s):
            
            # print(stack)
        
            if s[i] in start:
                stack.append(s[i])
                
            elif s[i] in end:
                if len(stack) == 0:
                    return False
                
                if start[end.index(s[i])] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
            i += 1
                
        if len(stack) == 0:
            return True
        return False