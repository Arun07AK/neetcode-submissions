import heapq
class Twitter:

    def __init__(self):
        self.time = 0
        self.T={}
        self.F={}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.T:
            self.T[userId]=[]
        self.T[userId].append((self.time,tweetId))
        self.time-=1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap=[]
        candidates=[]
        candidates.append(userId)
        if userId in self.F:
            for f in self.F[userId]:
                candidates.append(f)
        for c in candidates:
            if c in self.T:
                tweets_of_that_c=self.T[c]
                min_heap.extend(tweets_of_that_c)
        heapq.heapify(min_heap)
        res=[]
        n=0
        while min_heap and n<10:
            res.append(heapq.heappop(min_heap)[1])
            n+=1
        return res
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId==followeeId:
            return 
        if followerId not in self.F:
            self.F[followerId]=set()
        self.F[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.F and followeeId in self.F[followerId]:
            self.F[followerId].remove(followeeId)
