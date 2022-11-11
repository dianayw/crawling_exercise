import urllib.request
from lxml import etree

url = 'http://www.baidu.com'

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url= url, headers= headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

tree=etree.HTML(content)
result = tree.xpath('//div[@id="rtoDetails-3"]/div[@class="outer"]/h2@value')
print(result)
