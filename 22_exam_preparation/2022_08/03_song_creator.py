def add_songs(*songs_info):
    song_dict = {}
    for song in songs_info:
        name = song[0]
        if name not in song_dict.keys():
            song_dict[name] = []
        lyrics_lines = song[1]

        for line in lyrics_lines:
            song_dict[name].append(line)

    result = ''

    for key, values in song_dict.items():
        result += f'- {key}\n'
        for value in values:
            result += f'{value}\n'

    return result

print(add_songs(
    ("Love of my life",
     ["Love of my life, you've hurt me",
      "You've broken my heart, and now you leave me",
      "Love of my life, can't you see?",
      "Bring it back, bring it back"]),
    ("Beat It", []),
    ("Love of my life",
     ["Don't take it away from me",
      "Because you don't know",
      "What it means to me"]),
    ("Dream On",
     ["Every time that I look in the mirror"]),
))
