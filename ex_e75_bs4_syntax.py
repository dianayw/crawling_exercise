from bs4 import BeautifulSoup

# # soup = BeautifulSoup(response.read().decode(), 'lxml')
# soup = BeautifulSoup(open('test.html', encoding='utf-8'), 'lxml')

# list = soup.find('a') # returns the first a tag
# .find('a', title="a2")
# .find('a', class_="a1") # use 'class_' instead of 'class'
# list = soup.find_all('a')
# .find_all(['a', 'span']) # returns both a tag and span tag
# .find_all('li', limit=2) # returns first 2 results
# list = soup.select('a')
# .select('.a1')
# .select('#l1')
# .select('li[id]')
# .select('li[id="l2"]')
# .select('div li') # ancestor
# .select('div > ul > li') # direct child
# .select('a, li')
# .select('#d1')[0]
# print(list)
# print(list.attrs) # returns the attributes
# print(list.name) # returns the name of the tag
# print(list.attrs.get('class')) # returns the attribute
# print(list.string.get('class')) 
# print(list.get_text()) # always works, preferred