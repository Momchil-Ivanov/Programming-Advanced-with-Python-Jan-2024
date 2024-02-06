def team_lineup(*player_info):
    player_dict = {}
    for player in player_info:
        if player[1] not in player_dict.keys():
            player_dict[player[1]] = [player[0]]
        else:
            player_dict[player[1]].append(player[0])

    sorted_dict = dict(sorted(player_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    result = ''

    for key in sorted_dict.keys():
        result += f'{key}:\n'
        for player in sorted_dict[key]:
            result += f"  -{player}\n"

    return result

    # sorted_result = sorted(
    #     kwargs.items(),
    #     key=lambda kvp: (-len(kvp[1]), kvp[0])
    # )


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


