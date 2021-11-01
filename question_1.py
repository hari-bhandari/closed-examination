def create_triangle(n):
    """
    creates a triangle

    Args:
        n (int): size or height of triangle.

    Returns:
        str: The triangle
    """
    if n < 0:
        return None
    completed_string = ''
    for i in range(1, n + 1):
        completed_string += ('x' * i) + (n - i) * '-' + '\n'
    return completed_string


print(create_triangle(-1))
