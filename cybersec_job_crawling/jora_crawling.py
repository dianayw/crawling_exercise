
# Request URL: https://jupiter.jora.com/api/v1/jobs?keywords=cyber%20security&page_num=2&session_id=bffba802cdba738ce6c0ce38dd78be9a&search_id=JTKQjRsgBv7EizJVwH1y-bffba802cdba738ce6c0ce38dd78be9a-MxgygHiUocT_Ff7Ml4JJ&session_type=web&user_id=JTKQjRsgBv7EizJVwH1y&logged_user=false&mobile=false&site_id=1&country=AU&host=https://jupiter.jora.com&full_text_only_search=false&ads_per_page=5&callback=_jsonp_0
# Request Method: GET
# Status Code: 200 
# Remote Address: 104.16.104.16:443
# Referrer Policy: strict-origin-when-cross-origin

# :authority: jupiter.jora.com
# :method: GET
# :path: /api/v1/jobs?keywords=cyber%20security&page_num=2&session_id=bffba802cdba738ce6c0ce38dd78be9a&search_id=JTKQjRsgBv7EizJVwH1y-bffba802cdba738ce6c0ce38dd78be9a-MxgygHiUocT_Ff7Ml4JJ&session_type=web&user_id=JTKQjRsgBv7EizJVwH1y&logged_user=false&mobile=false&site_id=1&country=AU&host=https://jupiter.jora.com&full_text_only_search=false&ads_per_page=5&callback=_jsonp_0
# :scheme: https
# accept: */*
# accept-encoding: gzip, deflate, br
# accept-language: en-GB,en-US;q=0.9,en;q=0.8
# cookie: __cfruid=05db05bf0b4149ed99313693d139044881961cc3-1663229117; _ga=GA1.2.228305745.1663231238; _gid=GA1.2.197332613.1663231238; _fbp=fb.1.1663231237967.1143733742; _gcl_au=1.1.1727770384.1663231238; g_state={"i_p":1663238443704,"i_l":1}; sol_id=1babf692-7414-4cf7-a57d-eeb6203c7519; _jobengine_session=N1ZaM1RPaFQ1VWhSZDBscExDZ2t3Yk8zN05iaE50cmVzUURNOUtoS0oyL200eTV3SDdJZVgwNk9KQ2ZhRkkxRHZSbUU1ZitNa0dWeUl3Q2s2bEJTem5xY0llRlJYc3RHMEIwYXEvbW9scWV4S3hZR3JOM0dGcVp5aGdtZy8zcGFxdE9VazkzazV3YTBsbFNueGlHTVZFQWROZVhvR05rTHFSbTZhRWZRc0drVGRqU0VwZjdlTkpKNzErNnVhaDAranZQSCs1RVlIQjBJVFVCN3U2UnZMN1ZLa2RFLzVGRU1DZko4K2VGQUhFM2c5bGh1NVYwRjhKbWh4STU1TGtJTnpmbnZzL2NSY01PWE9CdzVDZVhFQWRSYkNienROamhxMmVpaU5Ua1JjSUVyL0cyM1Z5NHBTdUpSMXNPZ3ZKV0hzcTNqQ0FsdFlPemZ3T0lDOTh0S2hmSnIyTGgzblJieWJKNmIwdUYvRlpJPS0tVG1mc2Q5d0cvaGtQWGYvRlZZWDdWZz09--60b131dcd85098f07acdf44bfebb58e6357aa257
# referer: https://au.jora.com/
# sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "Windows"
# sec-fetch-dest: script
# sec-fetch-mode: no-cors
# sec-fetch-site: same-site
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36


# &page_num=1&

import urllib.request
import urllib.parse

start_page = int(input('start page:'))
end_page = int(input('end page:'))

base_url = 'https://jupiter.jora.com/api/v1/jobs?keywords=cyber%20security&'
end_url = '&session_id=bffba802cdba738ce6c0ce38dd78be9a&search_id=JTKQjRsgBv7EizJVwH1y-bffba802cdba738ce6c0ce38dd78be9a-MxgygHiUocT_Ff7Ml4JJ&session_type=web&user_id=JTKQjRsgBv7EizJVwH1y&logged_user=false&mobile=false&site_id=1&country=AU&host=https://jupiter.jora.com&full_text_only_search=false&ads_per_page=5&callback=_jsonp_0'

headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

for page in range(start_page, end_page+1):
    url_param = {
        'page_num' : str(page)
    }
    url_append = urllib.parse.urlencode(url_param)
    url = base_url + url_append + end_url

    request = urllib.request.Request(url=url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('utf-8')
    fp = open('cybersec_jora_2_'+str(page)+'.json','a', encoding='utf-8')
    fp.write(content)
    fp.close()




























# click_tracking_url   is the link to the job
# 有的link点开是别的网站，有的还是jora自己的页面
