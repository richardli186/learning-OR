def average(numbers):
    """
    Finds the average of a list of numbers

    Inputs:
        - numbers: a list of numbers

    Returns the average of the list
    """
    return sum(numbers) / len(numbers)

#print(average([1,4,5,2,3]))

def pairs(dictionary):
    """
    Prints the key value pairs of a dictionary

    Inputs:
        - dictionary: a dictionary

    Returns nothing
    """
    for key, value in dictionary.items():
        print(f'{key}' + ':' + f'{value}')

#pairs({4:5, 'twri':'34sdfj'})

def evens(lst):
    """
    List comprehension that filters a list to only even numbers

    Inputs:
        - lst: a list of real integers

    Returns a list of only the even numbers in the original list
    """
    return [num for num in lst if num % 2 == 0]

#print(evens([0,1,2,3,4,5,6,6,7]))

