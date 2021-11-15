from random import randint, random
from genetic import Chromosome, GA

from mutations import FlipFactory, Mutation


class OneMax(GA):

    def __init__(self, fixed_size: int = 1, chromosome_size:int = 8) -> None:
        super().__init__(fixed_size=fixed_size)
        self.chromosome_size = chromosome_size
        self.mutator: Mutation = FlipFactory.create_flip_mutation(1)

    @property
    def should_be_stopped(self) -> bool :      
        MAX_CYCLE = 200
        MAX_CYCLE_WITHOUT_IMPROVEMENT = 30
        goal_matched = lambda fitness : fitness == self.chromosome_size

        if MAX_CYCLE > self.cycle:
            return True

        if self.cycle - self.last_update > MAX_CYCLE_WITHOUT_IMPROVEMENT:
            return True

        for chromosome in self.population:
            if chromosome.fitness is not None and goal_matched(chromosome.fitness):
                return True

        return False

    def __generate_random_chromosome(self):
        alleles = []
        for _ in range(self.chromosome_size):
            number = randint(0,1)
            alleles.append(number)

        return Chromosome(alleles)

    def random_sub_population(self):
        """ Generate a list of size number of value of either 0 or 1"""
        for _ in self.fixed_size:
            chromosome = self.__generate_random_chromosome()
            self.population.append(chromosome)

    def mutate(self):
        mutation_probability: float
        
        # Only mutate if cycled based mutation probability occurs
        # Probability is mutation is high in the early cycle
        HIGH_MUTATION_PHASE = 75
        HIGH_MUTATION_PHASE_PROBABILITY = 0.75
        LOW_MUTATION_PHASE_PROBABILITY = 0.30

        # calculate mutation probability using cycle number
        if HIGH_MUTATION_PHASE > self.cycle:
            mutation_probability = HIGH_MUTATION_PHASE_PROBABILITY
        else:
            mutation_probability = LOW_MUTATION_PHASE_PROBABILITY

        probability_proportional_to_fitness = lambda fitness: (1 / fitness + 1) * mutation_probability > random()

        # get a random number and compare it to mutation probability 
        for chromosome in self.population:
            if probability_proportional_to_fitness(chromosome.fitness):
                self.mutator.mutate(chromosome)

    def crossover(self):
        """Do a uniform crosover."""
        # If probability is met then do a crossover

        # select best parent

        # do a crossover

        # clean parent
    
    def fit(self):
        """ Count the number of 1 """
        
        for chromosome in self.population:
            if chromosome.fitness is None:
                number_of_one = [number for number in self.chromosome if number is 1]
                chromosome.fitness = len(number_of_one)

    def survival(self):
        # calculate probability of survival using         
        pass