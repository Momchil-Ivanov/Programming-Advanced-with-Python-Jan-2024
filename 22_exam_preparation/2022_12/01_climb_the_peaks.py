from collections import deque

food_portions = deque([int(el) for el in input().split(', ')])
stamina = deque([int(el) for el in input().split(', ')])

mountain_peaks = deque([('Vihren', 80), ('Kutelo', 90), ('Banski Suhodol', 100), ('Polezhan', 60), ('Kamenitza', 70)])
conquered_peaks = []

while food_portions and stamina and mountain_peaks:
    last_food_portion = food_portions.pop()
    first_stamina = stamina.popleft()
    energy = last_food_portion + first_stamina
    current_peak = mountain_peaks.popleft()
    name = current_peak[0]
    difficulty = int(current_peak[1])
    if energy >= difficulty:
        conquered_peaks.append(name)
    else:
        mountain_peaks.appendleft(current_peak)

if not mountain_peaks:
    print(f'Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK')
else:
    print(f'Alex failed! He has to organize his journey better next time -> @PIRINWINS')

if conquered_peaks:
    print(f'Conquered peaks:')
    for peak in conquered_peaks:
        print(f'{peak}')
