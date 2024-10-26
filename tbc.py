class Character(object):
    def __init__(user, name = "Player",
               health = 100,
               chance = 75,
               damage = 10,
               armor = 3):
        super().__init__()
        user.name = name
        user.Health = health
        user.Chance = chance
        user.Damage = damage
        user.armor = armor

    @property
    def name(user):
        return user.__name

    @name.setter
    def name(user, value):
        user.__name = value

    @property
    def health(user):
        return user.__health

    @Health.setter
    def health(value)
        user.__health = value

    @property
    def chance(user):
        return user.__chance

    @Chance.setter
    def chance(user, value):
        user.__chance = value

    @property
    def damage(user):
        return user.__damage

    @Damage.setter
    def damage(user, value):
        user.__damage = value

    @property
    def armor(user):
        return user.__armor

    @armor.setter
    def armor(user, value):
        user.__armor = value

    def printStats(user):
        print(f"""
    {user.name}
    ==================
    Health: {user.health}
    Chance: {user.chance}
    Damage: {user.damage}
    Armor:  {user.armor}
    """)

        print()

    def hit(user, enemy):