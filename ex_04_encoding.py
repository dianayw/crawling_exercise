import urllib.request
import urllib.parse

url='https://www.baidu.com/s?wd='
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
# 将汉字转化成Unicode编码
name = urllib.parse.quote('周杰伦')
url = url + name
# print(url)

# data = {
#     'wd':'周杰伦',
#     'sex':'男',
#     'location':'中国台湾'
# }
# new_data = urllib.parse.urlencode(data)
# # print(new_data)
# base_url = 'https://www.baidu.com/s?'
# url = base_url + new_data

request = urllib.request.Request(url= url, headers= headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)