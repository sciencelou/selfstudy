# Author: Lukas Elflein <lukaselflein@gmail.com>
#
"""
Generate prime and non-prime numbers in hex for labeling of blinded
Experiments.
Prime property can be used to remove blindness if label lists get lost.
Make sure to assign primes conistently to e.g. control group.
The process also assumes that you are unable to memorize hex numbers.
If this would remove blindness, choose another person to apply the labels.
"""
import numpy
import sympy

# This makes sure that your random numbers stay the same if you rerun the script
numpy.random.seed(123)


def random_numbers(range_min=2, range_max=10, num_labels=1):
    '''
    Return random numbers in given range, n prime and non-prime odd numbers.
    >>> int(random_numbers(7, 9, 1)[1])
    7
    >>> int(random_numbers(7, 9, 1)[0])
    9
    '''
    # Make even starting point odd
    if not range_min % 2:
        range_min += 1

    # Generate Primes
    prime_generator = sympy.sieve.primerange(range_min, range_max)
    primes_in_range = numpy.fromiter(prime_generator, dtype=numpy.uint32,
                                     count=-1)

    # Generate all numbers in range
    numbers_in_range = numpy.arange(range_min, range_max + 1, 2,
                                    dtype=numpy.uint32)

    # Filter Primes out
    non_primes = numbers_in_range[numpy.invert(numpy.in1d(numbers_in_range,
                                                          primes_in_range))]

    if not non_primes.size:
        return None

    chosen_primes = numpy.random.choice(non_primes, num_labels)
    chosen_non_primes = numpy.random.choice(primes_in_range, num_labels)

    return(chosen_primes, chosen_non_primes)


if __name__ == '__main__':

    # Minimum and maximum number used as label
    RANGE_MIN, RANGE_MAX = 2**17, 2**18
    # How many labels do you need?
    NUMBER_LABELS = 10

    # Get random numbers
    LABELS = random_numbers(RANGE_MIN, RANGE_MAX, NUMBER_LABELS)
    # Convert output
    LABEL_ARRAY = numpy.asarray(LABELS).T

    # Write everything to a csv table
    HEADER = 'prime=theanine+caffeine, non-prime=caffeine'
    FILE_NAME = 'hex_labels.csv'
    numpy.savetxt(FILE_NAME, LABEL_ARRAY, delimiter=',',
                  fmt='%x', header=HEADER)
    print(HEADER)
    print(LABEL_ARRAY)
