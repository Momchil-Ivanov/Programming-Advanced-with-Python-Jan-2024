def start_spring(**spring_objects_info):
    objects_dict = {}

    for key, value in spring_objects_info.items():
        if value not in objects_dict.keys():
            objects_dict[value] = [key]
        else:
            objects_dict[value].append(key)

    for key in objects_dict:
        objects_dict[key] = sorted(objects_dict[key])

    sorted_dict = dict(sorted(objects_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    result = ''

    for key in sorted_dict:
        result += f'{key}:\n'
        for item in sorted_dict[key]:
            result += f'-{item}\n'

    return result

# example_objects = {"Water Lilly": "flower",
#                    "Swifts": "bird",
#                    "Callery Pear": "tree",
#                    "Swallows": "bird",
#                    "Dahlia": "flower",
#                    "Tulip": "flower",}
# print(start_spring(**example_objects))

# example_objects = {"Swallow": "bird",
#                    "Thrushes": "bird",
#                    "Woodpeckers": "bird",
#                    "Swallows": "bird",
#                    "Warblers": "bird",
#                    "Shrikes": "bird",}
# print(start_spring(**example_objects))

example_objects = {"Magnolia": "tree",
                   "Swallow": "bird",
                   "Thrushes": "bird",
                   "Pear": "tree",
                   "Cherries": "tree",
                   "Shrikes": "bird",
                   "Butterfly": "insect"}
print(start_spring(**example_objects))
