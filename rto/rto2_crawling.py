# ============================================ 观察分析 ============================================
# Request URL: https://training.gov.au/Organisation/AjaxDetailsLoadContacts/e72b6b19-ebb9-422e-990e-49e1529b1e3e?tabIndex=2&_=1668041220939

# :authority: training.gov.au
# :method: GET
# :path: /Organisation/AjaxDetailsLoadContacts/e72b6b19-ebb9-422e-990e-49e1529b1e3e?tabIndex=2&_=1668041220939
# :scheme: https
# accept: text/html, */*; q=0.01
# accept-encoding: gzip, deflate, br
# accept-language: en-GB,en-US;q=0.9,en;q=0.8
# content-type: application/x-www-form-urlencoded
# cookie: ASP.NET_SessionId=arjapjauvbwmirk3ttpurny2; ifShowHistory=false; __utmc=185625580; __utmz=185625580.1668035516.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); TgaSearchOption=Nrt; Search_Index_gridRtoSearchResults=100; downloadStarted=false; .ASPXANONYMOUS=Y2eOOdppn6V71DIjeyY78sOmMCijGcyrNqsEA2c0J1hPbfb49oFpoj14-lrPL9vwp2YwbaijYE78vTHmkG2Q1n2_oKN7WD-2RhHDR8-pgiVI8SBO_CEzI_A5AfqhHcBW7Gn_bXk6DU0ax33NB2weOw2; __utma=185625580.1196472828.1668035516.1668035516.1668040645.2; __utmt=1; __utmb=185625580.4.10.1668040645
# referer: https://training.gov.au/Organisation/Details/21159
# sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "Windows"
# sec-fetch-dest: empty
# sec-fetch-mode: cors
# sec-fetch-site: same-origin
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
# x-requested-with: XMLHttpRequest

# Request URL: https://training.gov.au/Organisation/AjaxDetailsLoadRegistration/e72b6b19-ebb9-422e-990e-49e1529b1e3e?tabIndex=1&_=1668041190734

# :authority: training.gov.au
# :method: GET
# :path: /Organisation/AjaxDetailsLoadRegistration/e72b6b19-ebb9-422e-990e-49e1529b1e3e?tabIndex=1&_=1668041190734
# :scheme: https
# accept: text/html, */*; q=0.01
# accept-encoding: gzip, deflate, br
# accept-language: en-GB,en-US;q=0.9,en;q=0.8
# content-type: application/x-www-form-urlencoded
# cookie: ASP.NET_SessionId=arjapjauvbwmirk3ttpurny2; ifShowHistory=false; __utmc=185625580; __utmz=185625580.1668035516.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); TgaSearchOption=Nrt; Search_Index_gridRtoSearchResults=100; downloadStarted=false; .ASPXANONYMOUS=Y2eOOdppn6V71DIjeyY78sOmMCijGcyrNqsEA2c0J1hPbfb49oFpoj14-lrPL9vwp2YwbaijYE78vTHmkG2Q1n2_oKN7WD-2RhHDR8-pgiVI8SBO_CEzI_A5AfqhHcBW7Gn_bXk6DU0ax33NB2weOw2; __utma=185625580.1196472828.1668035516.1668035516.1668040645.2; __utmt=1; __utmb=185625580.4.10.1668040645
# referer: https://training.gov.au/Organisation/Details/21159
# sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "Windows"
# sec-fetch-dest: empty
# sec-fetch-mode: cors
# sec-fetch-site: same-origin
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
# x-requested-with: XMLHttpRequest

# 1668041220939
# 1668041190734
#request url最后面的这个数字可以不要

# ============================================ 第一步 ============================================
# # 解析search_result page，获取每条的 OrganisationId, name, code

# import urllib.parse
# import json

# list_file = open('./rto/organisation_list.json','a',encoding='utf-8')

# for i in range(1, 5):
#   path = './rto/search_result_100_page'+str(i)+'.json'
#   fp = open(path,'r', encoding='utf-8')
#   page = fp.read()
#   result = (json.loads(page))['data']
#   for organisation in result:
#     list_file.write('{'
#     +'"Codes": "'+organisation['Codes']+'",'
#     +'"LegalPersonName": "'+organisation['LegalPersonName']+'",'
#     +'"OrganisationId": "'+organisation['OrganisationId']+'"'
#     +'},')
#   fp.close()

# list_file.close()

# # 还需要手动去掉文件最后一个逗号，然后开头结尾加方括号

# ============================================ 第二步 ============================================
# # 用 OrganisationId 的列表，获取contact的数据

# import json
# import urllib.request

# org_content = open('./rto/organisation_list.json','r',encoding='utf-8').read()
# org_list = json.loads(org_content)

# headers = {
#     'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
# }
# base_url = 'https://training.gov.au/Organisation/AjaxDetailsLoadContacts/'
# end_url = '?tabIndex=2'

# count = 1

# for org in org_list:
#   url = base_url + org['OrganisationId'] + end_url
#   request = urllib.request.Request(url=url, headers=headers)
#   response = urllib.request.urlopen(request)
#   page_content = response.read().decode('utf-8')
#   page_content=page_content.replace("&nbsp;","") # fix html whitespace problem
#   contact_detail = open('./rto/detail/contact_detail_'+str(count)+'.html','w',encoding='utf-8')
#   contact_detail.write(page_content)
#   contact_detail.close()
#   print('organisation '+str(count)+' done')
#   count = count + 1
  
# ============================================ 第三步 ============================================
# # 解析需要的具体字符串，前三个，名字，职位，座机，手机，邮箱，记得记录公司

import json
from bs4 import BeautifulSoup
import re
import pandas as pd

# constants: 
# get the first 3 result for each organisation
limit = 3 
# get the contact name, job title, phone, mobile, email of each result
label_list = ["Contact name","Job title","Phone","Mobile","Email"]
# target = [0,1,3,4,5] 

# create function to edit results
def turn_tag_to_string(tag):
  tag_value = tag.get_text() # remove html open and end tags
  tag_string = re.search("[\S]+\s?[\S]+\s?[\S]+", tag_value).group() # remove extra whitespace
  tag_result = tag_string.replace("<br />"," ") # remove the break row tag
  return tag_result

csv_file = open('./rto/contacts.csv','a',encoding='utf-8')

# write the title row in csv file
csv_file.write('Organisation Code,')
for i in range (1, limit+1):
  csv_file.write('Contact Type,')
  for label_name in label_list:
    csv_file.write(label_name+',')
csv_file.write('\n')

# loop thru all 339 organisations
for org_num in range(1,340):
  soup = BeautifulSoup(open('./rto/detail/contact_detail_'+str(org_num)+'.html', encoding='utf-8'), 'lxml')
  org_code=json.loads(open('./rto/organisation_list.json','r',encoding='utf-8').read())[org_num-1]['Codes']
  csv_file.write('"'+str(org_code)+'",')
  #for heading in range (1, limit+1):
    #csv_file.write('"'+turn_tag_to_string(tag_heading)+'",')
      #for pair in range(len(target)):
      # csv_file.write(label_list[int(pair)])
      # tag_data = soup.find_all("div", class_ = 'fieldset')[heading-1].find_all("div", class_ = 'display-row')[int(target[pair])].find_all("div", class_ = 'display-field-no-width')[0]
      # csv_file.write('"'+turn_tag_to_string(tag_data)+'",')
  
  # loop thru all 3 subtitles
  for heading in range (1, limit+1):
    tag_heading = soup.select('h2')[heading]
    csv_file.write(turn_tag_to_string(tag_heading)+',')
    contact_array = ['','','','','']
    pair_list = soup.find_all('div', class_ = 'fieldset')[heading-1].find_all('div', class_ = 'display-row')
    
    # loop thru each needed label
    for i in range(len(label_list)):
      #print(label_list[i]+':')
      
      # loop thru all label-data pair on the page
      for pair in pair_list:
        data_find = pair.find('div', string = (label_list[i]+':'))
        #print('pair:'+str(pair))
        #print('string:'+pair.find('div').string)
        #print(data_find)
        if data_find:
          #print("yes data found")
          data_result = pair.find('div',class_ = 'display-field-no-width')
          #print(turn_tag_to_string(data_result))
          contact_array[i] = turn_tag_to_string(data_result)
    for contact_data in contact_array:
      csv_file.write(contact_data+',')
  csv_file.write('\n')
  print('organisation '+str(org_num)+' done')
csv_file.close()

# PS 第一个标签Summary下三个拿不到， 其他的都是html解析
# # ABN: 96 039 601 269 (external link)
# # ACN: 607 053 127
# # RTO type: Community Based Adult Education Provider
# 第五个 Scope有点麻烦
# 其他可以
# # Registration
# # Contacts
# # Addresses
# # Scope
# # Regulatory Decision Information
# # Delivery

# 第四步
# EXCEL FORMULA to match tables
# =INDEX('contacts'!B$1:B$340,MATCH($A1,'Contacts'!$A$1:$A$340,0))
# 下载的csv里code那一列开头有tab space，需要用NotePad打开，replace掉，再放到excel里