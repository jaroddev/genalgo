from random import randrange

# function sig created

# generation d'une populations (sous ensemble de solution )
# selection des parents
# Génération des enfants (offsprings)
# comparateur de solutions, enfants et parents

# TODO/WIP

# insertion des enfants dans la population si meilleurs ??
# selon les conditions, retraits de certaines solutions de la population

# Verification de la condition darret de levolution


def main():
    # generate the solution ??

    # size for the byte slice 
    n = 8

    # initialize the array, 0 item
    slice = [0] * n


def generate_population(size):
    """
        @param size: size of the population at the beggining
        @return slices: array of byte arrays that are possible solutions 
    """

def parent_selection(slices, parent_number):
    """
        return an array of parent solution, we will use them to generate child solutions
        @return parents: return a slice that contains parent_number parents
    """

def generate_offsprings(generator, offspring_number):
    """
        @param size: size of the population at the beggining
        @return slices: array of byte arrays that are possible solutions 
    """

def best_offsprings(slices):
    """
        This function contains the logic to sort the offsprings array
        @param slices: array of offspings byte arrays
    """

class FlipGenerator:
    """
        A generator class that exposes the logic of flip
        through a generator interface
    """

    DEFAULT_FLIP_NUMBER = 1

    def __init__(self, flip_number = 0) -> None:
        # Might be temporary
        flip_allowed_values = {
            1,
            3,
            5
        }

        # Assing default value
        self.flip_number = FlipGenerator.DEFAULT_FLIP_NUMBER
        
        # Override default value if the valeue is allowed
        if flip_number in flip_allowed_values:
            self.flip_number = flip_number
                
    def generate(self, parent):
        print(f"chosen parent is: {parent}")
        print(f"generating a new offspring, {self.flip_number} flip method")

        child = FlipGenerator.flip(parent, )

        print(f"generated child is: {child}")

    @staticmethod
    def flip(slice, n):
        """
            A mutation method for the onemax problem
            @param slice: a byte array (0 or 1)
            @param n: number of flip
        """

        # mutation probability ??

        for i in n:
            target = randrange(len(slice) - 1)

            # should we check something here 
            slice[target] = 1

        return slice


# def generate_offsprings():
    # generate the offspring by using the given the parents 


# def print_solution():
    

# def 