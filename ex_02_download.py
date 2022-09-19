import urllib.request

#下载网页
url_page = "http://www.baidu.com"
urllib.request.urlretrieve(url_page,'baidu.html')

#下载图片
url_img = "http://xxxxx.jpg"
urllib.request.urlretrieve(url= url_img, filename= 'name.jpg')