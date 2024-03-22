class Country():
    def __init__(self, name, population):
        self.name = name
        self.population = population
        self.deadPeople = 0
        self.infectedBy = None

    def infect(self, virus):
        self.infectedBy = virus