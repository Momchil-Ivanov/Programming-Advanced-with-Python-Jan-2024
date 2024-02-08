def movie_organizer(*movie_info):
    genre_dict = {}
    for movie in movie_info:
        name = movie[0]
        genre = movie[1]

        if genre not in genre_dict:
            genre_dict[genre] = [name]
        else:
            genre_dict[genre].append(name)

    sorted_genre_dict = dict(sorted(genre_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    for key in sorted_genre_dict.keys():
        sorted_genre_dict[key].sort()

    result = ''

    for key in sorted_genre_dict.keys():
        result += f'{key} - {len(sorted_genre_dict[key])}\n'
        for movie in sorted_genre_dict[key]:
            result += f'* {movie}\n'

    return result


print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
