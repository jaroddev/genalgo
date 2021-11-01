from abc import abstractmethod
from random import sample

from genetic import Chromosome


class Mutation:

    @abstractmethod
    def mutate(self, chromosome: Chromosome):
        """ Mutate the given chromosome"""
        pass


class Flip(Mutation):

    def __init__(self, n: int) -> None:
        self.n = n

    def mutate(self, chromosome: Chromosome):
        
        # Check that their is at least n value to flip
        size = len(chromosome.alleles)
        if self.n > size:
            raise ValueError(f"{self.n} flip are too many flips for a chromosome of size of {size}")

        # Get n locuses to flip
        locuses = sample(
            range(size - 1),
            k = self.n
        )

        # Flip all the alleles coresponding to the chosen locuses
        for locus in locuses:
            chromosome.alleles[locus] = Flip.__flip(chromosome.alleles[locus])

    @staticmethod
    def __flip(allele: int):
        if allele is 1:
            return 0
        
        return 1


class FlipNotAllowedError(ValueError):
    """ is raised if Flip factory cannot crate a flip mutation"""


class FlipFactory:
    """ Make sure only allowed Flip can be created"""
    ALLOWED_FLIP = [1,3,5]

    @staticmethod
    def create_flip_mutation(n: int) -> Flip:
        if n in FlipFactory.ALLOWED_FLIP:
            return Flip(n)
        else:
            raise FlipNotAllowedError(f"{n} flip are not allowed, pick from {FlipFactory.ALLOWED_FLIP}")