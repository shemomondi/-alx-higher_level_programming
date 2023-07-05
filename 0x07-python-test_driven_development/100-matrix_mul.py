#!/usr/bin/python3
"""Defines a matrix multiplication function."""

def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices.

    Args:
        m_a (list of lists): The first matrix.
        m_b (list of lists): The second matrix.

    Returns:
        list of lists: The resulting matrix after multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or a list of lists.
                   If one element of the matrix is not an integer or float.
                   If m_a or m_b is not a rectangle.
        ValueError: If m_a or m_b is empty or they can't be multiplied.

    """

    # Validate m_a and m_b are lists
    if type(m_a) is not list or type(m_b) is not list:
        raise TypeError("m_a must be a list" if type(m_a) is not list else "m_b must be a list")

    # Validate m_a and m_b are lists of lists
    if any(type(row) is not list for row in m_a) or any(type(row) is not list for row in m_b):
        raise TypeError("m_a must be a list of lists" if type(m_a[0]) is list else "m_b must be a list of lists")

    # Validate m_a and m_b are not empty
    if len(m_a) == 0 or len(m_a[0]) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or len(m_b[0]) == 0:
        raise ValueError("m_b can't be empty")

    # Validate m_a and m_b contain only integers or floats
    if any(not isinstance(element, (int, float)) for row in m_a for element in row):
        raise TypeError("m_a should contain only integers or floats")
    if any(not isinstance(element, (int, float)) for row in m_b for element in row):
        raise TypeError("m_b should contain only integers or floats")

    # Validate m_a and m_b are rectangles
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")

    # Validate m_a and m_b can be multiplied
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for i in range(len(m_a)):
        row = []
        for j in range(len(m_b[0])):
            element = 0
            for k in range(len(m_b)):
                element += m_a[i][k] * m_b[k][j]
            row.append(element)
        result.append(row)

    return result
