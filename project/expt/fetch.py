import sys
import tweepy
import codecs
def lookup_tweets(tweet_IDs, api):
    full_tweets = []
    tweet_count = len(tweet_IDs)
    try:
        for i in range(int((tweet_count / 98) + 1)):
            # Catch the last group if it is less than 100 tweets
            end_loc = min((i + 1) * 98, tweet_count)
            full_tweets.extend(api.statuses_lookup(tweet_IDs[i * 98:end_loc]))
        return full_tweets
    except tweepy.TweepError:
        print('Something went wrong, quitting...')
def fun(ifname):
  tweets = []
  fp = codecs.open(ifname,'r','utf-8')
  for l in fp:
    tweets.append(l.strip(' #\t\n\r').lower())
  fp.close()
  return tweets
def main():
    try:
        _, ifname,ofname = sys.argv
    except Exception as e:
        print(e)
        sys.exit(0)
    consumer_key = "5HnadXxPYFcWXdDmqiBeVW8Kx"
    consumer_secret = "Ek9J3Mn5ciNj6p2NwOebILhBhIkad3YUfli97REbWxNfzrhDGT"
    access_token = "1127204428212080641-y4tQN9jefOCXAgiD60qLh89CakKHIs"
    access_token_secret = "syZXb6s9kFob3P7kUoWHMGdqKWWQuyWRRaDz9eweb7Xry"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    id_list=fun(ifname)
    for x in id_list:
        #print(x)
    tweets = lookup_tweets(id_list, api) # id_list is the list of tweet ids
    fo = codecs.open(ofname,'w','utf-8')
    for i in tweets:
      fo.write('11')
      fo.write('\t')
      mystring=i.text
      for j in range(len(mystring)):
          if mystring[j]=='\n' or mystring[j]=='\r' or mystring[j]=='\r\n':
              mystring=mystring[0:j]+'|'+mystring[j+1:len(mystring)]
      fo.write(mystring)
      fo.write('\t')
      fo.write('0.9')
      #fo.write(i.text)
      fo.write('\n')
      #print(i.text)
if __name__=='__main__':
    main()
