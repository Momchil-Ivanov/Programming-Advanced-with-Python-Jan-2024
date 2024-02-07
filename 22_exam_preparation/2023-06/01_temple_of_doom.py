from collections import deque

tools = deque([int(el) for el in input().split()])
substances = deque([int(el) for el in input().split()])
challenges = deque([int(el) for el in input().split()])

while tools and substances and challenges:
    first_tool = tools.popleft()
    last_substance = substances.pop()

    result = first_tool * last_substance

    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(first_tool + 1)
        if last_substance - 1 > 0:
            substances.append(last_substance - 1)

if (not tools or not substances) and challenges:
    print(f'Harry is lost in the temple. Oblivion awaits him.')
if not challenges:
    print(f'Harry found an ostracon, which is dated to the 6th century BCE.')

if tools:
    print(f'Tools: {", ".join([str(el) for el in tools])}')
if substances:
    print(f'Substances: {", ".join([str(el) for el in substances])}')
if challenges:
    print(f'Challenges: {", ".join([str(el) for el in challenges])}')
