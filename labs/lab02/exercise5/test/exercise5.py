def is_valid_triangle(a, b, c):
    """Check if three sides can form a valid triangle.

    A triangle is valid if the sum of any two sides is greater than the third side.

    Args:
        a (float): Length of side a.
        b (float): Length of side b.
        c (float): Length of side c.
    Returns:
        bool: True if the sides form a valid triangle, False otherwise. 
    """
def is_valid_triangle(a, b, c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        return True
    else:
        return False

print(is_valid_triangle(3, 4, 5))