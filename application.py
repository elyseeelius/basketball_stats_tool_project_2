# test my app
import copy
import keyboard
from constants import PLAYERS, TEAMS


#
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
    return cleaned_players


# if __name__ == "__main__":
if __name__ == "__main__":
    clean_data()


def balance_teams():
    num_players_team = len(clean_data())/len(TEAMS)
    return int(num_players_team)

# for data in clean_data():
#     print(data)


# print(TEAMS)
def play_game():
    print('BASKETBALL TEAM STATS TOOL\n')

    print('---- MENU----\n')

    print('Here are your choices:')
    print("     A) Display Team Stats")
    print("     B) Quit")
    print("\n")
    option = ""
    while option != 'a' and option != 'b':
        option = input("Enter an option > ").lower()
        print("\n")
        if option == 'b':
            break
        else:
            print("Please enter A or B or C")
            continue

    if option == 'a':
        print("A) Panthers")
        print("B) Bandits")
        print("C) Warriors")
        print("\n")
        option_team = input("Enter an option: ")
        print("\n")

        def print_team_stats(option_team, team_name, start_index, end_index):
            print(f"Team: {team_name} Stats \n {'-' * 50}")
            print(f"Total players: {balance_teams()}")
            print("\n\n")
            print(f"Players on Team: ")
            list_data = []
            for player in clean_data()[start_index:end_index]:
                list_data.append(player['name'])
            print(", ".join(list_data))
            print("\n\n")

        if option_team.lower() == 'a':
            print_team_stats('a', 'Panthers', 0, 6)
        elif option_team.lower() == 'b':
            print_team_stats('b', 'Bandits', 6, 12)
        elif option_team.lower() == 'c':
            print_team_stats('c', 'Warriors', 12, 18)

        print("Press ENTER to continue... ")
        # End of the game
    elif option.lower() == "b":
        print("See you soon")


play_game()

