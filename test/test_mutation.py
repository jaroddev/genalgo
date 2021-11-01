import unittest
from genetic import Chromosome

from mutations import FlipFactory, FlipNotAllowedError, NotEnoughAllelesError


class FlipFactoryTest(unittest.TestCase):

    def setUp(self) -> None:
        self.factory = FlipFactory()

    def test_non_allowed_flip(self):
        with self.assertRaises(FlipNotAllowedError):
            self.factory.create_flip_mutation(2)


class FlipTest(unittest.TestCase):

    def setUp(self) -> None:
        self.factory = FlipFactory()

        self.one_flip = self.factory.create_flip_mutation(1)
        self.three_flip = self.factory.create_flip_mutation(3)
        self.five_flip = self.factory.create_flip_mutation(5)

    def test_generic_flip(self):
        flips = [
            (self.one_flip, 1),
            (self.three_flip, 3),
            (self.five_flip, 5)
        ]

        for flipper, flipped_alleles in flips:
            eight_zero_chromosome = [0,0,0,0 ,0,0,0,0]
            chromosome = Chromosome(eight_zero_chromosome)
            flipper.mutate(chromosome)

            ones = [allele for allele in chromosome.alleles if allele is 1]

            with self.subTest():
                self.assertEqual(
                    len(ones),
                    flipped_alleles
                )
    
    def test_not_enough_alleles(self):
        two_zero_chromosome = [0, 0]
        chromosome = Chromosome(two_zero_chromosome)
        
        with self.assertRaises(NotEnoughAllelesError):
            self.three_flip.mutate(chromosome)



if __name__ == "__main__":
    unittest.main()