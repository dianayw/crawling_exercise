import urllib.request
import urllib.parse


headers = {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
}

# :authority: www.seek.com.au
# :method: GET
# :path: /api/chalice-search/search?siteKey=AU-Main&sourcesystem=houston&userqueryid=4ef1dc8715b2d8f4da50b985fe89180b-6857321&userid=7b474530e9158c136db53659358fd173&usersessionid=7b474530e9158c136db53659358fd173&eventCaptureSessionId=7b474530e9158c136db53659358fd173&where=All+Australia&page=2&seekSelectAllPages=true&keywords=cyber+security&hadPremiumListings=true&include=seodata&solId=2c88f995-d054-4b9e-901e-0507f3e840e2
# :scheme: https
# accept: application/json, text/plain, */*
# accept-encoding: gzip, deflate, br
# accept-language: en-GB,en-US;q=0.9,en;q=0.8
# cookie: JobseekerSessionId=7b474530e9158c136db53659358fd173; JobseekerVisitorId=7b474530e9158c136db53659358fd173; __cf_bm=npE.5cXWCMuOaz9RgJcInZ5cYFkuppMrNLzBFW8d9no-1663226244-0-AfDevyg2/frdlMO5bASogbf7EG2XbVPUrfDhP6rWageFp0H4W0av2biZegAIpQ+bXp7Fl5c09ZFBvfoKHOA2Il8=; sol_id=2c88f995-d054-4b9e-901e-0507f3e840e2; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22fJ82Hd8ri215tKzUKpDS%22%7D; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_162402=eyJpZCI6IjVjMmZhYjVlLWU0MTgtNGEzMy05NTFkLTY3MGE4ZGZlMDQwNSIsImNyZWF0ZWQiOjE2NjMyMjYyNTA3ODIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; da_anz_candi_sid=1663226250093; da_marketing_channel=Natural Search; da_marketing_channel_value=Google:; da_tracking_code=null; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%7D; da_cdt=visid_01834002836c001a9e94ee955fae0506f001806700bd0-sesid_1663226250093; _gid=GA1.3.1241683065.1663226251; _scid=01606771-85ab-4982-a726-d9ed2ce15dee; _fbp=fb.2.1663226251213.1363978821; _gcl_au=1.1.1185559858.1663226251; _sctr=1|1663164000000; _pin_unauth=dWlkPU56aGhNV0k0TkdNdE9HWXpNaTAwWm1aaUxXRXdPVFF0T0RkbVpXWmlZbUl3TjJSbA; sol_id=2c88f995-d054-4b9e-901e-0507f3e840e2; da_searchTerm=cyber security; __gads=ID=50f47cda04546d1c:T=1663226259:S=ALNI_MZ1DWSv-7u4sZgV_jG288YoMsxu3Q; __gpi=UID=000009c881d9b7b2:T=1663226259:RT=1663226259:S=ALNI_MasJkvgSiF0B9LqDZc20Y7bncYQ2w; _hjSessionUser_162402=eyJpZCI6ImUwMWZhNTYzLTYzOGEtNTJmMy04NTBjLWU2YmYxNmE5ZjY5OSIsImNyZWF0ZWQiOjE2NjMyMjYyNTA3NzIsImV4aXN0aW5nIjp0cnVlfQ==; skl-lcid=9219f3c9-1e3c-4382-bff2-fbe070ccfb66; _ga=GA1.1.1080227193.1663226251; _ga_JYC9JXRYWC=GS1.1.1663226251.1.1.1663226851.60.0.0; utag_main=v_id:01834002836c001a9e94ee955fae0506f001806700bd0$_sn:1$_se:6$_ss:0$_st:1663228651925$ses_id:1663226250093%3Bexp-session$_pn:2%3Bexp-session$dc_visit:1$dc_event:6%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session$krux_sync_session:1663226250093%3Bexp-session; main=V%7C2~P%7Cjobsearch~K%7Ccyber%20security~WID%7C3000~N%7C2~L%7C3000~OSF%7Cquick&set=1663226857389
# referer: https://www.seek.com.au/cyber-security-jobs?page=2
# Request Method: GET
# cookie: JobseekerSessionId=7b474530e9158c136db53659358fd173; JobseekerVisitorId=7b474530e9158c136db53659358fd173; __cf_bm=npE.5cXWCMuOaz9RgJcInZ5cYFkuppMrNLzBFW8d9no-1663226244-0-AfDevyg2/frdlMO5bASogbf7EG2XbVPUrfDhP6rWageFp0H4W0av2biZegAIpQ+bXp7Fl5c09ZFBvfoKHOA2Il8=; sol_id=2c88f995-d054-4b9e-901e-0507f3e840e2; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%22fJ82Hd8ri215tKzUKpDS%22%7D; _hjFirstSeen=1; _hjIncludedInSessionSample=0; _hjSession_162402=eyJpZCI6IjVjMmZhYjVlLWU0MTgtNGEzMy05NTFkLTY3MGE4ZGZlMDQwNSIsImNyZWF0ZWQiOjE2NjMyMjYyNTA3ODIsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=1; da_anz_candi_sid=1663226250093; da_marketing_channel=Natural Search; da_marketing_channel_value=Google:; da_tracking_code=null; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%7D; da_cdt=visid_01834002836c001a9e94ee955fae0506f001806700bd0-sesid_1663226250093; _gid=GA1.3.1241683065.1663226251; _scid=01606771-85ab-4982-a726-d9ed2ce15dee; _fbp=fb.2.1663226251213.1363978821; _gcl_au=1.1.1185559858.1663226251; _sctr=1|1663164000000; _pin_unauth=dWlkPU56aGhNV0k0TkdNdE9HWXpNaTAwWm1aaUxXRXdPVFF0T0RkbVpXWmlZbUl3TjJSbA; sol_id=2c88f995-d054-4b9e-901e-0507f3e840e2; da_searchTerm=cyber security; __gads=ID=50f47cda04546d1c:T=1663226259:S=ALNI_MZ1DWSv-7u4sZgV_jG288YoMsxu3Q; __gpi=UID=000009c881d9b7b2:T=1663226259:RT=1663226259:S=ALNI_MasJkvgSiF0B9LqDZc20Y7bncYQ2w; _hjSessionUser_162402=eyJpZCI6ImUwMWZhNTYzLTYzOGEtNTJmMy04NTBjLWU2YmYxNmE5ZjY5OSIsImNyZWF0ZWQiOjE2NjMyMjYyNTA3NzIsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.1.1080227193.1663226251; _ga_JYC9JXRYWC=GS1.1.1663226251.1.1.1663226858.53.0.0; skl-lcid=d0a3f120-e6f2-40d9-bee5-9abd82339afb; _cc_id=5779f78b9ac2af5d508477fa58b4b4fa; panoramaId_expiry=1663831655242; panoramaId=962f10030a989ec60cb708e8d67016d53938c1be0dcc06f2f2dfe09848144ff3; utag_main=v_id:01834002836c001a9e94ee955fae0506f001806700bd0$_sn:1$_se:8$_ss:0$_st:1663228973653$ses_id:1663226250093%3Bexp-session$_pn:2%3Bexp-session$dc_visit:1$dc_event:8%3Bexp-session$dc_region:ap-southeast-2%3Bexp-session$krux_sync_session:1663226250093%3Bexp-session; main=V%7C2~P%7Cjobsearch~K%7Ccyber%20security~WID%7C3000~N%7C3~L%7C3000~OSF%7Cquick&set=1663227177581
# referer: https://www.seek.com.au/cyber-security-jobs?page=3

# &userqueryid=4ef1dc8715b2d8f4da50b985fe89180b-6857321&page=2&
# &userqueryid=4ef1dc8715b2d8f4da50b985fe89180b-7177517&page=3&
# &userqueryid=4ef1dc8715b2d8f4da50b985fe89180b-7574086&page=4&
# &userqueryid=4ef1dc8715b2d8f4da50b985fe89180b-7716300&page=5&
# &userqueryid=4ef1dc8715b2d8f4da50b985fe89180b-7811872&
# &userqueryid=4ef1dc8715b2d8f4da50b985fe89180b-7821023&

url_p1 = 'https://www.seek.com.au/api/chalice-search/search?siteKey=AU-Main&sourcesystem=houston&'
url_p2 = '&userid=7b474530e9158c136db53659358fd173&usersessionid=7b474530e9158c136db53659358fd173&eventCaptureSessionId=7b474530e9158c136db53659358fd173&where=All+Australia&'
url_p3 = '&seekSelectAllPages=true&keywords=cyber+security&hadPremiumListings=true&include=seodata&solId=2c88f995-d054-4b9e-901e-0507f3e840e2'

start_page = 1
end_page = 5

for page in range(start_page, end_page+1):
    url_uqid = {
        'Request URL' : str(8765432+page*10),
    }
    url_append1 = urllib.parse.urlencode(url_uqid)
    print(url_append1)
    url_page = {
        'page' : str(page)
    }
    url_append2 = urllib.parse.urlencode(url_page)

    url = url_p1 + url_append1 + url_p2 + url_append2 + url_p3
    # print(url)
    # request = urllib.request.Request(url=url, headers=headers)
    # response = urllib.request.urlopen(request)
    # content = response.read().decode('utf-8')
    # print('====================')
    # print(content)
    # print('====================')
    # fp = open('sci-fic_'+str(page)+'.json','a', encoding='utf-8')
    # fp.write(content)
    # fp.close()


# 进展220915：
# 因为request需要user query id, 而且referer内容为上一页，
# 推测seek有反爬机制，
# 为防止触发，先尝试别的网站