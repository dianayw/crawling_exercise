# Workforce Australia
# https://www.workforceaustralia.gov.au/individuals/jobs/search?searchText=cyber%20security
# port: ?searchText=cyber%20security

# Request URL: https://www.workforceaustralia.gov.au/api/v1/global/vacancies/?searchText=cyber%20security
# Request Method: GET
# Status Code: 200 OK
# Remote Address: 165.12.220.49:443
# Referrer Policy: strict-origin-when-cross-origin

# Request URL: https://www.workforceaustralia.gov.au/api/v1/global/vacancies/?searchText=cyber%20security&pageNumber=2

# Accept: application/json, text/plain, */*
# Accept-Encoding: gzip, deflate, br
# Accept-Language: en-GB,en-US;q=0.9,en;q=0.8
# Connection: keep-alive
# Cookie: .AspNetCore.Antiforgery.ziEn_S86G8U=CfDJ8NkYqY-KhAFDrxpvKzAhISHOdrp-Gcl4geW5qt_D7ewaRmUJqojLqH3xsXwpNEq0LXz7ZrjQCSk1kJ1LaoOdc8WSg1VM2Xc_FUaXKcnFc_zHsn9QhJ5Dmr1GerWdfiGbOBMXytSpVRKMvqez9wTvxmI; ASP.NETCore_SessionId=CfDJ8NkYqY%2BKhAFDrxpvKzAhISH3McLidty3XqQ3no1SXgRsljRomVCXtt7E%2FHpFdQY0hB9ayh9loFFYoZ9d15x366%2FUbJB8U1Q6XurZJhvwKeiQA5QtnBcQacCWHyvY4f%2B9XE1UwFE8DWkKqC%2FD6Aq1k%2FaRSJZRYSFc5cPuyruSWk%2Fy; dtCookie=v_4_srv_12_sn_DE24AE4629C7B964F765CF017E52124B_perc_100000_ol_0_mul_1_app-3Ae02032f51f3dcd5f_1; TS01b34024=01e68e16122e88cc731288fa3505f77ef05118b4711d071b41aca90df1ab018e3d61868b9988b3bea354c54b93ef166808c4b0fd9b4234ff760e7f2141006f6a96af4b4d7c816c75351af33fd1618fb59d433250603e9f9d96aa09704448b417c82eecd229; TS01b34024=01e68e16122e88cc731288fa3505f77ef05118b4711d071b41aca90df1ab018e3d61868b9988b3bea354c54b93ef166808c4b0fd9b4234ff760e7f2141006f6a96af4b4d7c816c75351af33fd1618fb59d433250603e9f9d96aa09704448b417c82eecd229; rxVisitor=166374157827072JA1I5O5ASQLMREDFAMSS27EC9TJ7IA; _ga=GA1.3.1765935219.1663741579; _gid=GA1.3.1051734892.1663741579; _gat=1; dtLatC=2; dtSa=-; rxvt=1663743395925|1663741578272; dtPC=12$541595607_534h2vFLWPORMCREJRVPFDBCOTFULCRNHGSPET-0e0
# Host: www.workforceaustralia.gov.au
# Referer: https://www.workforceaustralia.gov.au/individuals/jobs/search?searchText=cyber%20security
# RequestVerificationToken: CfDJ8NkYqY-KhAFDrxpvKzAhISFVTeT6Gi1aEaHOQ7kgwJ8LQK62R3PUJKmwJxTE2K6dgyq4u79SGjzMoEWD1ucLEHIyapGOjPLF5Y7Hvll7g-3ytz3_3PTZnp1LeG4EcxQyQZDXW3e-rbHzzfKrazUmUxg
# sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"
# sec-ch-ua-mobile: ?0
# sec-ch-ua-platform: "Windows"
# Sec-Fetch-Dest: empty
# Sec-Fetch-Mode: cors
# Sec-Fetch-Site: same-origin
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36
# x-dtpc: 12$541595607_534h2vFLWPORMCREJRVPFDBCOTFULCRNHGSPET-0e0
# X-Requested-With: XMLHttpRequest

# Referer: https://www.workforceaustralia.gov.au/individuals/jobs/search?searchText=cyber%20security&pageNumber=2

# x-dtreferer: https://www.workforceaustralia.gov.au/individuals/jobs/search?searchText=cyber%20security

import urllib.request
import urllib.parse

if __name__ == '__main__':
    start_page = 1
    end_page = 267 #267 in total

    base_url = 'https://www.workforceaustralia.gov.au/api/v1/global/vacancies/?searchText=cyber%20security&'

    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'
    }

    for page in range(start_page, end_page+1):
        if page != 1:
            url_param = {
                'pageNumber' : str(page)
            }
            url_append = urllib.parse.urlencode(url_param)
            url = base_url + url_append
        else:
            url = base_url
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        content = response.read().decode('utf-8')
        fp = open('./testfolder/workforce_220921_'+str(page)+'.json','a', encoding='utf-8')
        fp.write(content)
        fp.close()
        print("page "+str(page)+" done")
