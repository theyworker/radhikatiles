def markMatched(tile1, tile2):
    global unlocked
    unlocked[tile1] = True
    unlocked[tile2] = True


unlocked = [False] * 12
print(unlocked)

markMatched(1, 2)

print(unlocked)
