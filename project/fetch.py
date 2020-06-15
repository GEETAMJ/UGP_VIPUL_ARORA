import tweepy
import codecs
def fun(ifname):
  tweets = []
  fp = codecs.open(ifname,'r','utf-8')
  for l in fp:
    tweets.append(l.strip(' #\t\n\r').lower())
  fp.close()
  return tweets
def main():
    try:
        _, ifname,ofname
    except Exception as e:
        print(e)
        sys.exit(0)
    consumer_key = "AcKjilPdm9WCWucdJdLzo35lY"
    consumer_secret = "8cZzfod5uAXx1DfjHxmHQZzM6tqsSRdPfkZ2SdHk4Lz654Q7eJ"
    access_token = "1127204428212080641-BQku1j2GJWWJpdMn1p6rPOVGVZLOQY"
    access_token_secret = "3rARg9cqf64POg87LVQONK3dkvOKVZnoZJ59XsMgnnY1U"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    id_list=fun(ifname)
    tweets = api.statuses_lookup(id_list) # id_list is the list of tweet ids
    tweet_txt = []
    fo = codecs.open(ofname,'w','utf-8')
    for i in tweets:
      fo.write(i.text)
      fo.write('\n')
      
