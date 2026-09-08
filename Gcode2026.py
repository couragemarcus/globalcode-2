import random

SIZE = 5

# Player position
player_x = 0
player_y = 0

# Random treasure and trap locations
treasure = (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))
trap = (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))

while trap == treasure or trap == (0, 0):
    trap = (random.randint(0, SIZE - 1), random.randint(0, SIZE - 1))

print("🗺️  TREASURE HUNT")
print("Find the 💎 treasure and survive the ☠️ trap!")
print("Use W/A/S/D to move.")
print()

while True:
    print(f"You are at position ({player_x}, {player_y})")
    move = input("Move (W/A/S/D): ").lower()

    # Move player
    if move == "w" and player_y > 0:
        player_y -= 1
    elif move == "s" and player_y < SIZE - 1:
        player_y += 1
    elif move == "a" and player_x > 0:
        player_x -= 1
    elif move == "d" and player_x < SIZE - 1:
        player_x += 1
    else:
        print("❌ You can't move that way!")
        continue

    position = (player_x, player_y)

    # Check treasure
    if position == treasure:
        print("\n🎉 YOU FOUND THE TREASURE! 💎")
        print("🏆 YOU WIN!")
        break

    # Check trap
    if position == trap:
        print("\n☠️ OH NO! You stepped on a trap!")
        print("💀 GAME OVER!")
        break

    # Give hints
    distance = abs(player_x - treasure[0]) + abs(player_y - treasure[1])

    if distance <= 2:
        print("🔥 You're very close to the treasure!")
    elif distance <= 4:
        print("👀 You're getting warmer...")
    else:
        print("🥶 The treasure is far away.")

    print()
