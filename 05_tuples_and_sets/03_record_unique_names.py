n_names = int(input())

set_names = set([])

for _ in range(n_names):
    set_names.add(input())

for name in set_names:
    print(name)