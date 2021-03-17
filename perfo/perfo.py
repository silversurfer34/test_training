from random import randint
from timeit import repeat
from statistics import mean
from simple.sort import *

# inspired by https://realpython.com/sorting-algorithms-python/#pythons-built-in-sorting-algorithm


def time_sorting_algorithm(algorithm, array):
    # Set up the context and prepare the call to the specified
    # algorithm using the supplied array. Only import the
    # algorithm function if it's not the built-in `sorted()`.
    setup_code = f"from __main__ import {algorithm}" if algorithm != "sorted" else ""

    stmt = f"{algorithm}({array})"

    # Execute the code ten different times and return the time
    # in seconds that each execution took
    # number is the number of time stmt is called and measured
    #   number=10 will measure the time spend for 10 launches of stmt
    # repeat is the number of repetition of the measure
    #   repeat=10 will measure 10 times and return 10 results
    times = repeat(setup=setup_code, stmt=stmt, repeat=1, number=1)
    # Finally, display the name of the algorithm and the
    # minimum, max, average time it took to run
    print(
        f"Algorithm: {algorithm}. Minimum execution time: {min(times)}, Max execution time: {max(times)}, "
        f"Average execution time: {mean(times)}"
    )


ARRAY_LENGTH = 10000


if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    random_array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]
    sorted_array = [i for i in range(ARRAY_LENGTH)] #Best for bubble
    reverse_array = sorted_array[::-1] #Worst for insertion
    min_at_the_end = sorted_array[::] #Worst for bubble
    min_at_the_end.append(0)

    use_cases = {"sorted array": sorted_array, "random_array": random_array, "reverse array": reverse_array,
                 "min at the end": min_at_the_end}
    for label, array in use_cases.items():
        # Call the function using the name of the sorting algorithm
        # and the array you just created
        print(label)
        # time_sorting_algorithm(algorithm="sorted", array=array)
        time_sorting_algorithm(algorithm="bubble_sort", array=array)
        time_sorting_algorithm(algorithm="insertion_sort", array=array)
        time_sorting_algorithm(algorithm="merge_sort", array=array)
        time_sorting_algorithm(algorithm="quicksort", array=array)
        print("\n")