running = True
enemy_lives = 3
enemy_chakra = 0
print("Welcome to Will Dixon's Naruto Arena Helper")
print("This will help you keep track of your opponents chakra")
print("t = end turn, d = one of your opponents dies, e = exit")
print("1, 2, 3 = your opponent 1 chakra, 2 chakra or 3 chakra has been used")
print("You first? (y = yes): ")
if input() == "y":
    enemy_chakra = 3
else:
    enemy_chakra = 1

while running:
    print("enemy chakra:", enemy_chakra)
    print("next_input (t,d,e,1,2,3): ")
    s = input()
    if s == "e":
        running = False
    elif s == "d":
        enemy_lives = max(0, enemy_lives - 1)
    elif s == "t":
        enemy_chakra += enemy_lives
    elif s == "1":
        enemy_chakra -= 1
        if enemy_chakra < 0:
            enemy_chakra = 0
    elif s == "2":
        enemy_chakra -= 2
        if enemy_chakra < 0:
            enemy_chakra = 0
    elif s == "3":
        enemy_chakra -= 3
        if enemy_chakra < 0:
            enemy_chakra = 0
    else:
        print("Key Not Recognized")
