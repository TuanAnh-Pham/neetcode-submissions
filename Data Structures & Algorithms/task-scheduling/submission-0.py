class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)

        maxHeap = [-c for c in count.values()]
        heapq.heapify(maxHeap)
        
        #number of CPU cycles 
        times = 0
        #keep track of which task are waiting for cooldown 
        q = deque()

        # when there are still tasks to do / waiting for cool down
        while maxHeap or q:
            times +=1
            if maxHeap:
                #count number of work time left for certain task
                # +1 because we use negative value in maxheap -> decrement by +1
                work = 1 + heapq.heappop(maxHeap)
                if work < 0 : # if there are still work left
                    q.append([work,times+n])

            if q and q[0][1] == times: #when it's cooldown time
                heapq.heappush(maxHeap,q.popleft()[0])
        return times