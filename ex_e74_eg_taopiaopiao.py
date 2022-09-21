import urllib.request
import json
import jsonpath

url = 'https://www.taopiaopiao.com/cityAction.json?activityId&_ksTS=1663567379160_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true'

headers = {
    'authority': 'www.taopiaopiao.com',
    #':method': 'GET',
    #':path': '/cityAction.json?activityId&_ksTS=1663567379160_108&jsoncallback=jsonp109&action=cityAction&n_s=new&event_submit_doGetAllRegion=true',
    #':scheme': 'https',
    'accept': 'text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
    'bx-v': '2.2.3',
    'cookie': 't=116b427de0a245560f932d77f0c7747a; _tb_token_=ebbbffe7b395f; cookie2=13946d723d117eac3b7ea671e267ea8a; cna=sPOuGwQ99TMCAQGRa1Xbup6K; xlly_s=1; tfstk=cByABw6GmabcOx1JWlCo70VCzQShZ9btPngMBRcYrMx9VmJOiM23pOoNGcgEkgC..; l=eBLz60s7TaEtRq1MBO5CFurza779uIRb4sPzaNbMiInca6_htFs7INCEXDWeSdtjQtCnWetz5TzfvdLHR3AiBwKF_6aeVerZ3xvO.; isg=BBoash2lLT1GLKGRUbL8vUAQa8A8S54lFCBMQiSTUq14l7rRDNtVNd_pZ3sLRxa9',
    'referer': 'https://www.taopiaopiao.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}


request = urllib.request.Request(url= url, headers= headers)
response = urllib.request.urlopen(request)
content = response.read()

# fix gzip encoding issue
import gzip
content = gzip.decompress(content).decode('utf-8')

# # fix extra character that prevents json file formating
# # atguigu way is better
# content = content[content.index('{') : ]
# content = content[ : content.index('}') + 1 ]

#切割（）外多余字符
content = content.split('(')[1].split(')')[0]

with open('test.json','w', encoding='utf-8)') as fp:
    fp.write(content)

obj = json.load(open('test.json','r',encoding='utf-8'))
city_list = jsonpath.jsonpath(obj,'$..regionName')
print(city_list)