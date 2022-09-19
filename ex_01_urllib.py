import urllib.request

url = 'http://www.baidu.com'
response = urllib.request.urlopen(url)
content = response.read().decode('utf-8')

# #读取的字节数
# .read() 
# #读取某一行
# .readline()
# #读取的行数
# .readlines()
# 获取状态码
# .getcode()
# #获取url地址
# .geturl()
# #获取状态信息
# .getheaders()

print(content)