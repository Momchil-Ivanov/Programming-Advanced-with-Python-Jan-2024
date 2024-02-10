def forecast(*weather_info):
    states_dict = {}
    for location in weather_info:
        city = location[0]
        state = location[1]
        if state not in states_dict:
            states_dict[state] = [city]
        else:
            states_dict[state].append(city)

    sorted_states_dict = {}

    if 'Sunny' in states_dict.keys():
        sorted_states_dict['Sunny'] = sorted(states_dict['Sunny'])
    if 'Cloudy' in states_dict.keys():
        sorted_states_dict['Cloudy'] = sorted(states_dict['Cloudy'])
    if 'Rainy' in states_dict.keys():
        sorted_states_dict['Rainy'] = sorted(states_dict['Rainy'])

    result = ''
    for key in sorted_states_dict.keys():
        cities = sorted_states_dict[key]
        for current_city_index in range(len(cities)):
            result += f'{cities[current_city_index]} - {key}\n'

    return result


print(forecast(
    ("Tokyo", "Rainy"),
    ("Sofia", "Rainy")))
