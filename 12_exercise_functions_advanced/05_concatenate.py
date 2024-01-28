def concatenate(*args, **kwargs):
    ini_string = ""
    for word in args:
        ini_string += word

    for key in kwargs:
        if key in ini_string:
            ini_string = ini_string.replace(key, kwargs[key])

    return ini_string


print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))