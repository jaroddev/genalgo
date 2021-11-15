
from abc import abstractmethod


class BaseGeneticAlgorithm:
    
    
    @abstractmethod
    def create_initial_population():
        """ Create a population of random chromosomes (solutions)"""

    def __mutate(self):
        pass

    def new_cycle(self):
        """ Increase the age of each chromosome in the population"""
        self.cycle+=1

        for chromosome in self.population:
            chromosome.inc_age()

    def run(self):
        self.create_initial_population()

        while (not self.should_be_stopped):
            self.fit()
            self.__update_best_chromosome()

            # if crossover probability is met
            self.parameters.crossover_strategy.crossover(self.population)

            # if mutation probability is met for the chromosome 
            self.__mutate()

            
            # next cycle
            self.new_cycle()