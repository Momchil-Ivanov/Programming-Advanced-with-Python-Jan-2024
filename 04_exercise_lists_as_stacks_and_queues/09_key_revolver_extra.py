from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets_left_in_barrel = gun_barrel_size
bullets = deque([int(bullet) for bullet in input().split()])
locks = deque([int(bullet) for bullet in input().split()])
intelligence_value = int(input())

shots = 0

while bullets and locks:

    if bullets_left_in_barrel == 0:
        bullets_left_in_barrel = gun_barrel_size
        print("Reloading!")
    bullets_left_in_barrel -= 1
    current_bullet = bullets.pop()
    shots += 1
    current_lock = locks[0]

    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

if bullets_left_in_barrel == 0 and bullets:
    print("Reloading!")

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    bullet_cost = shots * bullet_price
    earned = intelligence_value - bullet_cost
    print(f"{len(bullets)} bullets left. Earned ${earned}")