import unittest
from chromosomes import Chromosome

class ChromosomeTest(unittest.TestCase):

    def test_chromosome_size(self):
        eight_zero_chromosome = [0,0,0,0 ,0,0,0,0]
        chromosome = Chromosome(eight_zero_chromosome)
        
        print(chromosome)

        self.assertEqual(
            len(chromosome.alleles),
            8
        )


if __name__ == "__main__":
    unittest.main()