from bs4 import BeautifulSoup
import urllib2

#url = 'http://www.sports-reference.com/cbb/schools/syracuse/2014.html'
#soup = BeautifulSoup(urllib2.urlopen(url).read())
soup = BeautifulSoup(open('./test/syr.html').read())

#print soup.prettify()

#body_tag = soup.body
#page_container = body_tag.find(id="page_container", recursive=False)
#page_content = page_container.find(id="page_content", recursive=False)
#all_roster = page_content.find(id="all_roster", recursive=False)
#all_roster = soup.find(id="all_roster")
#div_roster = all_roster.find(id="div_roster", recursive=False)
#roster = div_roster.find(id="roster", recursive=False)
roster = soup.find('table', id='roster')
#thead = roster.find("thead", recursive=False)
roster_attributes = []
for th in roster.thead.find_all("th"):
   roster_attributes.append(th['data-stat'])

#tbody = roster.find("tbody", recursive=False)

team_roster = []
for tr in roster.tbody.find_all("tr"):
   player = {}
   for k,v in zip(roster_attributes, tr.find_all("td")):
      player[k] = v.string
   team_roster.append(player)
