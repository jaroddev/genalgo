from abc import abstractmethod, abstractproperty
from typing import Callable

from genetic.chromosomes import Chromosome

class GAParameters:

    def __init__(
        self, 
        mutation_strategy: MutationStrategy,
        mutation_probability: Callable[[float], bool],
        crossover_strategy: ,

    ) -> None:

        self.mutation_strategy = mutation_strategy

        self.crossover_strategy = crossover_strategy

        self.mutation_strategy = mutation_strategy


class GA():
    """ Template for building generic genetic algorithm based solution"""

    def __init__(
        self,
        parameters: GAParameters
    ) -> None:

        """ Initialize the algorithm parameters

            Args:
                max_size -> max numbers of retained solutions
                chromosome -> A class with many method important for handling a chromosome
        """

        self.population: list[Chromosome] = []
      
        self.parameters = parameters

        # cycle
        self.cycle = 1

        # Last cycle the best was updated
        self.last_update = 1
        self.best_chromosome = None

    def __str__(self) -> str:
        cycle = f"Cycle number: {self.cycle}"
        fixed_position = f"Fixed size: {self.fixed_size}"
        current_position_label = "Current population:"

        population_string = ""
        
        for chromosome in self.population:
            population_string = f"{population_string}<--------------------------------->\n{chromosome.__str__}\n"
        
        return f"{cycle}\n{fixed_position}\n{current_position_label}\n{population_string}"

    @abstractproperty
    def should_be_stopped(self) -> bool :
        """ Decide if the algorithm should be stopped or not"""
          
    @abstractmethod
    def random_sub_population(self):
        """ Create a population of random chromosomes (solutions)"""

    @abstractmethod
    def crossover(self):
        pass

    @abstractmethod
    def fit(self):
        """ Give each solution a score so that they can be compared to each other"""

    @abstractmethod
    def survival(self):
        """ Introduce a survival mechanism to get rid of some chromosome
        
            Also serve as a way to make the population a fixed size
        """

    def __mutate(self):
        """ Mutate a whole population"""

        for _, chromosome in range(self.population):
            if self.parameters.mutation_probability(randint(0, 1)):
               self.parameters.mutation.mutate(chromosome)

    def __update_best_chromosome(self):
        # If it is the first time the function is called then the first chromosome is the best           
        if self.best_chromosome is None:
            self.best_chromosome = self.population[0]
            self.last_update = self.cycle

        for chromosome in self.population:
            if self.best_chromosome is not chromosome and chromosome.fitness > self.best_chromosome.fitness:
                self.best_chromosome = chromosome
                self.last_update = self.cycle

    def new_cycle(self):
        """ Increase the age of each chromosome in the population"""
        self.cycle+=1

        for chromosome in self.population:
            chromosome.inc_age()

    def run(self):
        self.random_sub_population()
        self.fit()
        self.__update_best_chromosome()

        while (not self.should_be_stopped):
            # if mutation probability is met for the chromosome 
            self.__mutate()
            self.parameters.mutation_strategy.mutate(self.population)

            # if crossover probability is met
            self.self.parameters.crossover_strategy.crossover()
            
            # prepare for survival
            self.fit()
            self.survival()

            # next cycle
            self.new_cycle()
            self.__update_best_chromosome()