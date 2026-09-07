import heapq
from collections import defaultdict


class Twitter:
    """
    define three instance attributes, time, user_posts, and user_followees, respectively,
        time represents each post's posted time, this time is across all users,
        not dedicated for each user, so cannot use the length of current user's posts
        to determine the order of posting tweet, though at the same time, each user can post their posts respectively,
        and user_posts collects each user's all posts in ordered by time,
        and user_followees represents each user's all followees, each user must be unique
    
    when get the tweets of the specific user, needed to consider all followees' posts of that specific user,
        so using tuple to store each post along with it's post time, and set to store all followees of user

    complexity, n total tweets, e follow edges, f followees of the queried user, k feed size (10)
        postTweet / follow / unfollow   O(1)
        getNewsFeed                     O(f * k * log k) time, O(f * k) space, so O(f) with k fixed
        overall space                   O(n + e)
    """
    
    def __init__(self):
        self.time = 0
        self.user_posts = defaultdict(list)
        self.user_followees = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_posts[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        posters = {userId} | self.user_followees.get(userId, set())
        posts = [post for poster in posters for post in self.user_posts[poster]]
        return [post for _, post in heapq.nlargest(10, posts)]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_followees[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_followees[followerId].discard(followeeId)


def test_twitter():
    # LeetCode example
    tw = Twitter()
    tw.postTweet(1, 5)
    assert tw.getNewsFeed(1) == [5]
    tw.follow(1, 2)
    tw.postTweet(2, 6)
    assert tw.getNewsFeed(1) == [6, 5]
    tw.unfollow(1, 2)
    assert tw.getNewsFeed(1) == [5]

    # Edge: user with no tweets and no followees
    tw = Twitter()
    assert tw.getNewsFeed(99) == []

    # Edge: feed capped at 10 most recent, newest first
    tw = Twitter()
    for tweet_id in range(1, 13):
        tw.postTweet(1, tweet_id)
    assert tw.getNewsFeed(1) == [12, 11, 10, 9, 8, 7, 6, 5, 4, 3]

    # Edge: following self must not duplicate own tweets
    tw = Twitter()
    tw.postTweet(1, 100)
    tw.follow(1, 1)
    assert tw.getNewsFeed(1) == [100]

    # Edge: unfollow a user never followed is a no-op
    tw = Twitter()
    tw.postTweet(1, 7)
    tw.unfollow(1, 2)
    assert tw.getNewsFeed(1) == [7]

    # Edge: merge across multiple followees, global recency order
    tw = Twitter()
    tw.follow(1, 2)
    tw.follow(1, 3)
    tw.postTweet(2, 20)
    tw.postTweet(3, 30)
    tw.postTweet(1, 10)
    tw.postTweet(2, 21)
    assert tw.getNewsFeed(1) == [21, 10, 30, 20]

    # Edge: cap applies across followees, older tweets from a followee drop out
    tw = Twitter()
    for tweet_id in range(1, 11):
        tw.postTweet(2, tweet_id)
    tw.follow(1, 2)
    tw.postTweet(1, 99)
    assert tw.getNewsFeed(1) == [99, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    print("All tests passed")


if __name__ == "__main__":
    test_twitter()
