from abc import abstractmethod
from random import randint
from typing import Callable

from chromosomes import Chromosome

class Mutation:

    @abstractmethod
    def mutate(self, chromosome: Chromosome):
        """Mutate the given chromosome."""


class MutationStrategy:
    """Strategy pattern wrapping around mutation base class.

    Attributes:
        mutation_probability:   Function taking a number in [0, 1] 
        and returns if the chromosome should mutate
    """

    def __init__(
        self,
        mutation_probability: Callable[[float], bool],
    ) -> None:
    
        self.mutation_probability = mutation_probability

    def mutate(self, population: List[Chromosome], mutation: Mutation):
        """ Mutate a whole population"""
        for _, chromosome in range(population):
            if self.mutation_probability(randint(0, 1)):
                mutation.mutate(chromosome)