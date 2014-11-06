from bs4 import BeautifulSoup
import urllib2

url = 'http://www.sports-reference.com/cbb/schools/syracuse/2014.html'
soup = BeautifulSoup(urllib2.urlopen(url).read())

#print soup.prettify()

body_tag = soup.body
page_container = body_tag.find_all(id="page_container", recursive=False)
page_content = page_container[0].find_all(id="page_content", recursive=False)
all_roster = page_content[0].find_all(id="all_roster", recursive=False)
div_roster = all_roster[0].find_all(id="div_roster", recursive=False)
roster = div_roster[0].find_all(id="roster", recursive=False)
