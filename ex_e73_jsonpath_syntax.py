import urllib.request
import json
import jsonpath

obj = json.load(open('somedata.json','r',encoding='utf-8'))
list = jsonpath.jsonpath(obj,'')
# $..author
# $.store.*
# $.store..price
# $..book[2]
# $..book[(@.length-1)]
# $..book[0,1]
# $..book[:2]
# $..book[?(@.isbn)]
# $..book[?(@.price>10)]