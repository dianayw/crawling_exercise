import urllib.request
import urllib.parse

url = 'http://www.baidu.com'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

data = {
    'kw':'spider'
}
data = urllib.parse.urlencode(data).encode('utf-8')
request = urllib.request.Request(url=url, data=data, headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)

# print(type(content))
# import json
# obj = json.loads(content)
# print(obj)
