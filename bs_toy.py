from bs4 import BeautifulSoup
#import urllib2

def get_simple_roster(soup):
    """
    Extract the "simple roster" table from a team page.
    Returns team_roster, a list of dicts, where each list item
    corresponds to the information for a single player
    
    Drill down soup to get to the roster table. Extract the table
    headings to use as keys for the player dicts. Initialize an empty
    list to store the information extracted for each player. Loop over
    each row of the table, producing a player dict with keys corresponding
    to the table headings and appending to the player list.
    
    Parameters:
    - 'soup': a BeautifulSoup object created from the team page
    """
    roster = soup.find('table', id='roster')
    roster_attributes = []
    for th in roster.thead.find_all("th"):
        roster_attributes.append(th['data-stat'])

    team_roster = []
    for tr in roster.tbody.find_all("tr"):
        player = {}
        for k,v in zip(roster_attributes, tr.find_all("td")):
            if k == 'summary':
                for s in v.string.split(','):
                    sep = s.strip().split(' ')
                    player[sep[1].lower().encode('ascii','ignore')] = float(sep[0])
            else:
                player[k] = v.string.encode('ascii','ignore')
        team_roster.append(player)

    return team_roster

# test driver code

#url = 'http://www.sports-reference.com/cbb/schools/syracuse/2014.html'
#soup = BeautifulSoup(urllib2.urlopen(url).read())
soup = BeautifulSoup(open('./test/syr.html').read())

team_roster = get_simple_roster(soup)