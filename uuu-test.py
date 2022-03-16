#!/usr/bin/env python
# coding: utf-8

# In[1]:


pwd


# In[2]:


pip install tweepy


# In[3]:


pip install pandas


# In[4]:


pip install pytz


# In[10]:


import tweepy
from datetime import datetime,timezone
import pytz
import pandas as pd

# 取得したAPI KEY、TOKENを入力
api_key = 
api_secret = 
access_key = 
access_secret = 


auth = tweepy.OAuthHandler(api_key, api_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)      
#検索条件の設定
searchkey = '親ガチャ'
item_num = 90
#検索条件を元にツイートを抽出
tweets = tweepy.Cursor(api.search_tweets,q=searchkey,lang='ja').items(item_num)
#関数:　UTCをJSTに変換する
def change_time_JST(u_time):
    #イギリスのtimezoneを設定するために再定義する
    utc_time = datetime(u_time.year, u_time.month,u_time.day,     u_time.hour,u_time.minute,u_time.second, tzinfo=timezone.utc)
    #タイムゾーンを日本時刻に変換
    jst_time = utc_time.astimezone(pytz.timezone("Asia/Tokyo"))
    # 文字列で返す
    str_time = jst_time.strftime("%Y-%m-%d_%H:%M:%S")
    return str_time
#抽出したデータから必要な情報を取り出す
#取得したツイートを一つずつ取り出して必要な情報をtweet_dataに格納する
tweet_data = []
for tweet in tweets:
    #ツイート時刻とユーザのアカウント作成時刻を日本時刻にする
    tweet_time = change_time_JST(tweet.created_at)
    create_account_time = change_time_JST(tweet.user.created_at)
    #tweet_dataの配列に取得したい情報を入れていく
    tweet_data.append([
        tweet_time,
        tweet.text,
        tweet.favorite_count, 
        tweet.retweet_count
                       ])
#取り出したデータをpandasのDataFrameに変換
#CSVファイルに出力するときの列の名前を定義
labels=[
    'ツイート時刻',
    'ツイート内容',
    'いいね数',
    'リツイート数'
    ]
#tweet_dataのリストをpandasのDataFrameに変換
df = pd.DataFrame(tweet_data,columns=labels)
#CSVファイルに出力する
#CSVファイルの名前を決める
file_name='tweet_data3.csv'
#CSVファイルを出力する
df.to_csv(file_name,encoding='utf-8-sig',index=False)


# In[11]:


pwd


# In[12]:


ls


# In[14]:


import json
import pandas as pd
import glob
#変換したいJSONファイルを読み込む
file_lists = glob.glob(r"/Users/maruyamakouta/Desktop/kotori/kotoriotoko/APPS/親ガチャ/RAW/20220213/07/20220213_073002.json")
datas = []

# ファイルを1つずつ読み込んでリストに格納して最後にcsvに吐き出す
for file in file_lists:
    json_open = open(file,'r', encoding='utf-8')
    data = json.load(json_open)
    for d in data['statuses']:
        year = d['created_at'][-4:]
        if d['created_at'][4:7]=='Feb':
            month = 2 #9月だったらSEP 8月だったらAUGなど任意に変更してください
        day = d['created_at'][8:10]
        hour = d['created_at'][11:13]
        minute = d['created_at'][14:16]
        second = d['created_at'][17:19]
        d_time= f'{year}-{month}-{day} {hour}:{minute}:{second}'
        datas.append([d_time, d['user']['name'],d['full_text']])
pd.DataFrame(datas, columns=['日付', 'アカウント名', 'ツイート']).to_csv('oya.csv', index=False,encoding='utf-16',errors='ignore')


# In[15]:


pwd


# In[16]:


ls


# In[17]:


cat oya.csv


# In[26]:


import json
import pandas as pd
import glob
#変換したいJSONファイルを読み込む
file_lists = glob.glob(r"/Users/maruyamakouta/Desktop/kotori/kotoriotoko/APPS/親ガチャコピー/RAW/*.json")
datas = []

# ファイルを1つずつ読み込んでリストに格納して最後にcsvに吐き出す
for file in file_lists:
    json_open = open(file,'r', encoding='utf-8')
    data = json.load(json_open)
    for d in data['statuses']:
        year = d['created_at'][-4:]
        if d['created_at'][4:7]=='Feb':
            month = 2 #9月だったらSEP 8月だったらAUGなど任意に変更してください
        day = d['created_at'][8:10]
        hour = d['created_at'][11:13]
        minute = d['created_at'][14:16]
        second = d['created_at'][17:19]
        d_time= f'{year}-{month}-{day} {hour}:{minute}:{second}'
        datas.append([d_time, d['user']['name'],d['full_text']])
pd.DataFrame(datas, columns=['日付', 'アカウント名', 'ツイート']).to_csv('oya3.csv', index=False,encoding='utf-16',errors='ignore')


# In[27]:


pwd


# In[28]:


ls


# In[29]:


cat *.csv


# In[30]:


cd Download/


# In[31]:


cd /Download


# In[32]:


cd Downloads


# In[33]:


import re
import pandas as pd
import string


# In[53]:


df=pd.read_csv('oyasample2.csv', header=None)


# In[36]:


df=pd.read_xlsx('oyasample2.xlsx', header=None)


# In[52]:


df=pd.read_csv('oyagatya.csv')


# In[49]:


df


# In[41]:


def remove_URL(text):
    return re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "" ,text)


# In[42]:


example="New competition launched :https://www.kaggle.com/c/nlp-getting-started"
print('出力結果', remove_URL(example))


# In[58]:


df[2]=df[2].apply(lambda x : remove_URL(x))


# In[57]:


df.head(50)


# In[59]:


df[2]


# In[60]:


import pandas as pd


# In[66]:


import MeCab
tagger = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")


# In[63]:


import os
print(os.getenv('PATH'))


# In[68]:


tagger=MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd -u /usr/local/lib/mecab/dic/userdic/oyagatya.dic")


# In[69]:


pwd


# In[70]:


df[2].to_csv('sample2.txt',encoding='utf-8',sep=',',index=False)


# In[82]:


df.head()


# In[83]:


def preprocess_wordcloud(doc): 
    # 数字を０に 
    doc = re.sub(r'\d+', '0', doc) 
    # メンション除去 
    doc = re.sub(r"@(\w+) ", "", doc) 
    # url除去 
    doc = re.sub(r"http\S+", "", doc)
    #リツイートを消す
    doc = re.sub(r"(^RT.*)", "", doc, flags=re.MULTILINE | re.DOTALL)
    # 大文字・小文字変換 
    doc = doc.lower() 
    #絵文字を消す
    emoji_pattern = re.compile("["
    u"\U0001F600-\U0001F64F"
    u"\U0001F300-\U0001F5FF"
    u"\U0001F680-\U0001F6FF"
    u"\U0001F1E0-\U0001F1FF"
    "]+", flags=re.UNICODE)
    doc = emoji_pattern.sub("", doc)
    # 不要記号削除
    pattern = '[!"#$%&\'\\\\()*+,-./:;<=>?@[\\]^_`{|}~「」〔〕“”◇ᴗ●↓→♪★⊂⊃※△□◎〈〉『』【】＆＊・（）＄＃＠。、？！｀＋￥％]' 
    doc = re.sub(pattern, ' ', doc) 
    return doc


# In[84]:


df[2]=df[2].astype(str)
df[2]=df[2].apply(lambda x : preprocess_wordcloud(x))


# In[91]:


df.head()


# In[92]:


df[2].to_csv('sample3.txt',encoding='utf-8',sep=',',index=False)


# In[93]:


with open('sample3.txt', encoding='utf-8') as fi:
    source_text = fi.read()


# In[ ]:





# In[94]:


tagger.parse('')
node = tagger.parseToNode(source_text)


# In[95]:


word_list = []
while node:
    word_type = node.feature.split(',')[0]
    if word_type == '名詞':
        word_list.append(node.surface)
    node = node.next


# In[101]:


word_chain = ' '.join(word_list)
W = WordCloud(width=1000, height=800, background_color='white', colormap='bone', font_path='/Users/maruyamakouta/Library/Fonts/ipaexg.ttf',stopwords={'の', 'ん','これ','もの','そう','こと'},collocations = False).generate(word_chain)


# In[102]:


from matplotlib import pyplot as plt
from wordcloud import WordCloud
plt.imshow(W)
plt.axis('off')
plt.show()


# In[103]:


W.to_file("oyagatya_kai2.png")


# In[ ]:




