class MinStack:

    def __init__(self):
        self.stack = [[]]  


    def push(self, val: int) -> None:
        if self.stack[-1]:
            currMin = min(self.getMin(),val)
        else:
            currMin = val

        self.stack.append([val,currMin])


    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        if self.stack[-1]:
            return self.stack[-1][1]
        else:
            return None 

                
