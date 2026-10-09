class TimeMap:

    def __init__(self):
        self.eventDict = {} # {key:[value, timestamp]}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.eventDict:
            self.eventDict[key] = []
        
        self.eventDict[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        if key not in self.eventDict:
            return res
        else:
            l,r = 0, len(self.eventDict[key]) - 1
            while l <= r:
                m = l + (r-l)//2

                if self.eventDict[key][m][1] <= timestamp:
                    res = self.eventDict[key][m][0]
                    l = m +1
                else:
                    r = m - 1
        return res

