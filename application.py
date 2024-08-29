# test my app
import copy
from constants import PLAYERS


def clean_data():
    player_copy = copy.deepcopy(PLAYERS)
    cleaned_players = []
    for player in player_copy:
        fixed = {}
        fixed['name'] = player['name']
        fixed['guardians'] = player['guardians']
        if player['experience'] =='YES':
            fixed['experience'] = True
        else:
            fixed['experience'] = False
        fixed['height'] = int(player['height'].split(' ')[0])
        cleaned_players.append(fixed)
        print(fixed)
    return cleaned_players


clean_data()
