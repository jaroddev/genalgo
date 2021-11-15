class Chromosome():

    def __init__(self, alleles: list = []) -> None:

        self.alleles: list = alleles

        self.fitness = None

        self.age = 0

    def __str__(self) -> str:
        return f"{self.alleles}\n{self.fitness}\n{self.age}"

    def inc_age(self):
        """ Marker to date the chromosome in a population"""
        self.age += 1