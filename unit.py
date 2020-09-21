class Unit:
    def __init__(self, hp, unit_type, city_id):
        # mp, active, current_action, turn_over, location,
        self.hp = hp
        self.unit_type = unit_type
        # self.mp = mp
        # self.active = active
        # self.current_action = current_action
        # self.turn_over = turn_over
        # self.location = location
        self.city_id = city_id

    def get_hp(self):
        return self.hp

    def get_city(self):
        print(self.city_id)
        return self.city_id

class CombatUnit(Unit):
    def __init__(self, hp, unit_type, city_id, ap):
        super().__init__(hp, unit_type, city_id)
        self.ap = ap

    def get_ap(self):
        print(self.ap)
        return self.ap

class City:
    def __init__(self, name, population, id):
        self.name = name
        self.population = population
        self.id = id
    
    def get_name(self):
        print(self.name)
        return self.name

    def get_population(self):
        print(self.population)
        return self.population
    
    def add_to_population(self):
        self.population += 1
        print(self.population)
        return self.population

    def get_id(self):
        print(self.id)
        return self.id

u = Unit("10", "Warrior", "Athens")
c = CombatUnit("10", "Warrior", "Sparta", 5)
# u.get_city()
# u.get_hp()
# c.get_ap()
a = City("Athens", 2, 1)
a.get_name()
a.get_population()
a.add_to_population()
