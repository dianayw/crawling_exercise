from lxml import etree

# 解析本地文件
tree = etree.parse('xxx.html')

tree.xpath('xpath')
li_list = tree.xpath('//ul/li')
li_list = tree.xpath('//ul/li[@id="abc"]/text()')
li_list = tree.xpath('//ul/li[@class="def"]/text()')
li_list = tree.xpath('//ul/li[contains(@id="abc")]/text()')
li_list = tree.xpath('//ul[starts-with(@id="abc")]/text()')
li_list = tree.xpath('//ul[@id="abc"]/text()')
li_list = tree.xpath('//ul[@id="li" and @class="c1"]/text() ')
li_list = tree.xpath('//ul[@id="li"] | [@id="ul"]/text() ')