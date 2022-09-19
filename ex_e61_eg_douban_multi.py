import urllib.request
import urllib.parse

base_url = 'https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&'
headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}
#https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&
# start=0&limit=20
#https://movie.douban.com/j/chart/top_list?type=17&interval_id=100:90&action=&
# start=20&limit=20
start_page = 1
end_page = 2

for page in range(start_page, end_page+1):
    url_param = {
        'start' : str((page - 1)*20),
        'limit' : '20'
    }
    url_append = urllib.parse.urlencode(url_param)
    url = base_url + url_append
    print(url)
    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')

    fp = open('sci-fic_'+str(page)+'.json','a', encoding='utf-8')
    fp.write(content)
    fp.close()
