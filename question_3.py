def sum_integers(start, end):
    if end < start or start < 0 or end < 0:
        return -1
    sum_between_numbers = ((end - start + 1) * (start + end))/2
    return int(sum_between_numbers)

