<<<<<<< Updated upstream
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
=======
class Character(object):
    def __init__(user, name = "Player",
               Health = 100,
               Chance = 25,
               Damage = 15,
               armor = 3):
        super().__init__()
        user.name = name
        user.Health = Health
        user.Chance = Chance
        user.Damage = Damage
        user.armor = armor

    @property
    def name(user):
        return user.__name

    @name.setter
    def name(user, value):
        user.__name = value

    @property
    def Health(user):
        return user.__Health

    @Health.setter
    def Health(value):
        user.__Health = value

    @property
    def Chance(user):
        return user.__Chance

    @Chance.setter
    def Chance(user, value):
        user.__Chance = value

    @property
    def Damage(user):
        return user.__Damage

    @Damage.setter
    def Damage(user, value):
        user.__Damage = value

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
    Health: {user.Health}
    Chance: {user.Chance}
    Damage: {user.Damage}
    Armor:  {user.armor} """)

        print()

    def hit(user, dummy):
>>>>>>> Stashed changes
