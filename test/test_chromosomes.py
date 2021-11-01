import unittest
from chromosomes import Chromosome

class ChromosomeTest(unittest.TestCase):

    def test_chromosome_size(self):
        eight_zero_chromosome = [0,0,0,0 ,0,0,0,0]
        chromosome = Chromosome(eight_zero_chromosome)
        
        self.assertEqual(
            len(chromosome.alleles),
            8
        )

    def test_default_aging(self):
        chromosome = Chromosome()

        self.assertEqual(0, chromosome.age)

    def test_increase_aging(self):
        chromosome = Chromosome()     

        chromosome.inc_age()

        self.assertEqual(1, chromosome.age)


if __name__ == "__main__":
    unittest.main()