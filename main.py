import xml.etree.ElementTree as ET

squads_path = 'opta-mls/srml-98-2014-squads.xml'
squads_tree = ET.parse(squads_path)
squads_root = squads_tree.getroot()

'''
for season in root:
  for team in season:
    for item in team:
      print item.tag, item.attrib
'''

match_path = 'opta-mls/2014/f24-98-2014-741362-eventdetails.xml'
match_tree = ET.parse(match_path)
match_root = match_tree.getroot()

for game in match_root:
  home_team_name = game.attrib['home_team_name']
  home_team_id = game.attrib['home_team_id']
  away_team_name = game.attrib['away_team_name']
  away_team_id = game.attrib['away_team_id']
  game_date = game.attrib['game_date']

  print 'Examining game: {0} vs {1} on {2}.'.format(home_team_name, away_team_name, game_date)

  for event in game:
    print event.tag, event.attrib