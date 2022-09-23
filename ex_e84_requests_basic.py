import requests

url = 'http://www.google.com'
response = requests.get(url= url)
print(type(response))
response.encoding = 'utf-8'
# response.text
# response.content 
# response.url
# response.status_code

url = 'http://fanyi.baidu.com/sug'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
data = {
    'kw': 'eye'
}

response = requests.post(url= url, params = data, headers= headers)
content = response.text

# 注意和urllib的区别：
# （1）post请求不需要编解码
# （2）post请求的参数不是param是data #???
# （3）不需要请求对象的定制

# print(content)
import json
obj = json.loads(content)#, encoding='utf-8')
print(obj)