def sum_integers(start, end):
    """
       calculates the sum of numbers between two numbers

       Args:
           start (int): min range.
           end (int): max range.

       Returns:
           int : the sum between

       Raises:
           KeyError: Raises an exception.
       """
    if end < start or start < 0 or end < 0:
        return -1
    sum_between_numbers = ((end - start + 1) * (start + end))/2
    return int(sum_between_numbers)

