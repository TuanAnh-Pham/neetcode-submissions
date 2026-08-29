class Solution:
    def isValid(self, s: str) -> bool:
        checking_dict = {''}
        if len(s) == 1 or len(s)%2 > 0:
            return False

        stack = []
        for char in s:
            if char in '([{':
                stack.insert(0,char)
            elif char in ')]}':
                if len(stack) > 0 \
                    and (char == ')' and stack[0] == '(' \
                    or char == ']' and stack[0] == '[' \
                    or char == '}' and stack[0] == '{') :
                        del stack[0]
                else:
                    return False
        
        return len(stack) == 0
            