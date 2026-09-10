class Twitter:

    def __init__(self):
        self.tweetMap = defaultdict(list) # userId: list of [count, tweetIds]
        self.followMap = defaultdict(set) # userId: set of followeeIds
        self.count = 0 # keep track of time

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []
        
        # Gather the most recent tweets from userId's following list
        self.followMap[userId].add(userId) # add user's own ID for its own tweetIds
        for followeeId in self.followMap[userId]:
            # If followeeId has tweeted, append their most recent tweet to the heap
            # in the following format: [count, tweetId, followeeId, index - 1]
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweetId = self.tweetMap[followeeId][index]
                maxHeap.append([count, tweetId, followeeId, index - 1])
        heapq.heapify_max(maxHeap)

        # Build user's news feed with the tweets from most recent to least recent
        while maxHeap and len(res) < 10:
            count, tweetId, followeeId, index = heapq.heappop_max(maxHeap)
            res.append(tweetId)
            # Append the next most recent tweet from followee if there are any more
            if index >= 0:
                count, tweetId = self.tweetMap[followeeId][index]
                heapq.heappush_max(maxHeap, [count, tweetId, followeeId, index - 1])
        
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
