import urllib.request
from lxml import etree

# https://sc.chinaz.com/tupian/kejibeijing.html
# https://sc.chinaz.com/tupian/kejibeijing_2.html


def create_request(page):
    if(page == 1):
        url = 'https://sc.chinaz.com/tupian/kejibeijing.html'
    else:
        url = 'https://sc.chinaz.com/tupian/kejibeijing_' + str(page) + '.html'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url= url, headers= headers)
    return request
    
def get_content(request): 
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    return content

def download_image(content):
    tree = etree.HTML(content)
    name_list = tree.xpath('//div[@class="container"]//img/@alt')
    src_list = tree.xpath('//div[@class="container"]//img/@data-original')
    #for i in range(len(name_list)):
    for i in range(5):
        name = name_list[i]
        src = src_list[i]
        url = 'https:' + src
        print(name,url)
        urllib.request.urlretrieve(url=url,filename = './testfolder/' + name +'.png')

if __name__ == '__main__':
    #start_page = int(input('input start page: '))
    #end_page = int(input('input end page: '))
    start_page =1 # todelete
    end_page =2 # todelete
    for page in range(start_page,end_page+1):
        request = create_request(page)
        content = get_content(request)
        download_image(content)
