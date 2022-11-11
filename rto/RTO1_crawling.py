
# :authority: training.gov.au
# :method: POST
# :path: /Search/AjaxOrganisationSearch?searchTitleOrCode=&SearchType=Rto&searchTgaSubmit=Search&registrationStatus=0%2C1%2C2%2C3&nrtScopeDeliveryStates=01%2C02%2C03%2C04%2C05%2C06%2C07%2C08%2C99&includeImplicitScope=true&scopeNationalCode=CHC30121
# :scheme: https
# accept: text/plain, */*; q=0.01
# accept-encoding: gzip, deflate, br
# accept-language: en-GB,en-US;q=0.9,en;q=0.8
# content-length: 40
# content-type: application/x-www-form-urlencoded
# cookie: ASP.NET_SessionId=arjapjauvbwmirk3ttpurny2; ifShowHistory=false; __utma=185625580.1196472828.1668035516.1668035516.1668035516.1; __utmc=185625580; __utmz=185625580.1668035516.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); TgaSearchOption=Nrt; .ASPXANONYMOUS=PPtl-n2eIk4M-W70BkxfWiolhac8NhErrjeAYjDFAcfx2u0djeJ23DokW6IkFLoqAhdCx0JFBSOG1TBClkANGOqjd7dX5Ya64otp8gY9dubCvSPPQdwUehdhV8kmXUnR2GsANFXgj4bi0-VRf5pEiw2; __utmt=1; __utmb=185625580.9.10.1668035516
# origin: https://training.gov.au
# referer: https://training.gov.au/Search?searchTitleOrCode=&SearchType=Rto&searchTgaSubmit=Search&registrationStatus=0%2C1%2C2%2C3&nrtScopeDeliveryStates=01%2C02%2C03%2C04%2C05%2C06%2C07%2C08%2C99&includeImplicitScope=true&scopeNationalCode=CHC30121
# sec-ch-ua: "Google Chrome";v="107", "Chromium";v="107", "Not=A?Brand";v="24"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "Windows"
# sec-fetch-dest: empty
# sec-fetch-mode: cors
# sec-fetch-site: same-origin
# user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36
# x-requested-with: XMLHttpRequest

# https://training.gov.au/Search/AjaxOrganisationSearch?searchTitleOrCode=&SearchType=Rto&searchTgaSubmit=Search&registrationStatus=0%2C1%2C2%2C3&nrtScopeDeliveryStates=01%2C02%2C03%2C04%2C05%2C06%2C07%2C08%2C99&includeImplicitScope=true&scopeNationalCode=CHC30121

# 进展
# 因为每页的request url和request head是完全一样的
# 没法用循环写出全部页面的request
# 发现页面可以一次显示100条，那么总共300多结果可以手动获取
# 然后解析json，获得每页的url
# 再扒具体页的内容
# 见rto2——scrawling
