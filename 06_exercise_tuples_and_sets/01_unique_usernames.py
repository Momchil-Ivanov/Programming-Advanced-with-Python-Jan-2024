n_lines = int(input())

usernames_set = set()

for _ in range(n_lines):
    usernames_set.add(input())

for username in usernames_set:
    print(username)