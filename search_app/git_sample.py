import urllib
import urllib.request
import json
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

url_list = []
title_list = []
snippet_list =[]

API_KEY = "APIのKEYを入れます"
ENGINE_ID="エンジンIDを入れます"
phrase = "tennis"
#phrase = "テニス"
#print(phrase)
#print(str(phrase))
cnt = 1 # 1:1~10位, 11:11~20位

#リクエストURL
req_url = "https://www.googleapis.com/customsearch/v1?hl=ja&key="+API_KEY+"&cx="+ENGINE_ID+"&alt=json&q="+phrase+"&start="+str(cnt)+"&lr=lang_ja&safe=off"

#リクエスト
req = urllib.request.Request(req_url)
res = urllib.request.urlopen(req)
dump = json.loads(res.read())
hit = dump["queries"]["request"][0]["totalResults"]
#print(hit)

#検索結果のURL, TITLE, SNIPPET　をappendしてく
for p in range(len(dump["items"])):
    url_list.append(dump['items'][p]['link'])
    print(dump['items'][p]['link'])
    title_list.append(dump['items'][p]['title'])
    print(dump['items'][p]['title'])
    snippet_list.append(dump['items'][p]['snippet'].replace('\n',''))
    print(dump['items'][p]['snippet'])
    print('---------------------------------')