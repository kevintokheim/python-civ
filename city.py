class City:
    def __init__(self, name, population, id):
        self.name = name
        self.population = population
        self.id = id

    def get_name(self):
        return self.name

    def get_population(self):
        return self.population

    def add_to_population(self):
        self.population += 1
        return self.population

    def get_id(self):
        return self.id
