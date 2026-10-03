class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list) # [count, tweetId]
        self.userMap = defaultdict(set) # (user1,user2)


    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count,tweetId])
        self.count -= 1


    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []

        #add self
        self.userMap[userId].add(userId)

        for follower in self.userMap[userId]:
            if follower in self.tweetMap:
                idx = len(self.tweetMap[follower]) - 1
                count, tweetId = self.tweetMap[follower][idx]
                heapq.heappush(minHeap,[count, tweetId, follower, idx-1])

        while minHeap and len(res) < 10:
            count, tweetId, follower, index = heapq.heappop(minHeap)
            res.append(tweetId)
            #while follower still has more tweet, add next tweet
            if index >= 0:
                count, tweetId = self.tweetMap[follower][index]
                heapq.heappush(minHeap,[count, tweetId, follower, index-1])

        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.userMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.userMap[followerId]:
            self.userMap[followerId].remove(followeeId)
