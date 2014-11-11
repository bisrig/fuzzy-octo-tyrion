from bs4 import BeautifulSoup
#import urllib2

def extract_table(table):
    table_to_extract = soup.find('table', id=table)
    table_heading = []
    for th in table_to_extract.thead.find_all("th"):
        table_heading.append(th['data-stat'])

    extracted_table = []
    for tr in table_to_extract.tbody.find_all("tr"):
        player = {}
        for k,v in zip(table_heading, tr.find_all("td")):
            if v.string:
                player[k] = v.string.encode('ascii','ignore')
            else:
                player[k] = '0'
        extracted_table.append(player)

    return extracted_table

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
    team_roster = extract_table('roster')
    for player in team_roster:
        for s in player['summary'].split(','):
            sep = s.strip().split(' ')
            player[sep[1].lower().encode('ascii','ignore')] = float(sep[0])

    return team_roster

def get_player_list(team_roster):
    player_list = []
    for player in team_roster:
        player_list.append(player['player'])
    return player_list
    
def add_mpg_to_team_roster(team_roster):
    per_game_table = extract_table('per_game')
    for player in team_roster:
        for pg_entry in per_game_table:
            if pg_entry['player'] == player['player']:
                player['mpg'] = float(pg_entry['mp_per_g'])
    
    return team_roster

# test driver code

#url = 'http://www.sports-reference.com/cbb/schools/syracuse/2014.html'
#soup = BeautifulSoup(urllib2.urlopen(url).read())
soup = BeautifulSoup(open('./test/syr.html').read())

#extract_table('per_game')

team_roster = get_simple_roster(soup)
player_list = get_player_list(team_roster)
team_roster = add_mpg_to_team_roster(team_roster)