""" 
This program connects to Twitter to get the last 10 user-defined tweets. 
It then finds how many followers each one has and multiplies it by the number of words 
that appear in each user's tweets and shows which of the two users has the larger product. 
"""
import tweepy

consumer_key = "Y74fK1vUZa1OUNy3utdpGTrBf"
consumer_secret = "GYCiFBzpPJS8AVYiFLIejhr9ecQG8BJTheWAB3xpQqku2hUArj"
access_key = "1095091627163611138-IH30HAO7WuxkrsC5qAobZJv219SuNz"
access_secret = "CG3phNf10WG2pM8ZeE3e7SnjTqOMeJHbfLTBwzHlflofe"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)

api = tweepy.API(auth)

u1= input("Give 1st user's username: ")
u2 = input("Give 2nd user's username: ")


#word count 

user1_status=api.user_timeline(screen_name=u1,count=10, tweet_mode="extended")
user2_status=api.user_timeline(screen_name=u2, count=10, tweet_mode="extended")


user1_word_counter=0
temp1=0
for tweet in user1_status:
 
  temp1=len(tweet.full_text.split())
  user1_word_counter = user1_word_counter + temp1

print(u1+ " total words in last 10 tweets: "+str(user1_word_counter)) # print total words for last 10 tweets  of user1

user2_word_counter=0
temp2=0
for tweet in user2_status:
   
    temp2=len(tweet.full_text.split())
    user2_word_counter= user2_word_counter + temp2

print(u2+" total words in last 10 statuses: " +str(user2_word_counter)) #>> print total words for 10 statuses of user2

#number of followers

user1_followers=api.get_user(u1)
user2_followers=api.get_user(u2)

print(u1+" total followers: "+str(user1_followers.followers_count))
print(u2+ " total followers: "+str(user2_followers.followers_count))

final1=user1_word_counter*user1_followers.followers_count
final2=user2_word_counter*user2_followers.followers_count

if final1>final2:
    print("Biggest sum is user's: "+u1+" and it's: "+str(final1))
else:
    print("Biggest sum is user's: "+u2+" and it's: "+str(final2))
