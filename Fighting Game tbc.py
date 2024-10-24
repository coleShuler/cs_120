import tbc

def main():
    user = tbc.Character()
    user.name = "user"
    user.Health = 10
    user.Chance = 50
    user.Damage = 5
    user.armor = 2

    monster = tbc.Character("Monster", 20, 30, 5, 0)

    user.printStats()
    monster.printStats()

    tbc.fight(user, monster)

if __name__ == "__main__":
    main()