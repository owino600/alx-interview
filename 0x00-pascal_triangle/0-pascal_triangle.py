#!/usr/bin/python3
def pascal_triangle(n):
    """
    Generates Pascal's triangle up to height n.
    Returns a list of lists representing the triangle.
    """
    if n <= 0:
        return []  # Return an empty list for n <= 0

    triangle = []  # Initialize an empty list to store the triangle rows
    row = []  # Initialize an empty list for the current row
    prev_row = []  # Initialize an empty list for the previous row

    for i in range(0, n + 1):
        # Calculate the values for the current row
        row = [
            (prev_row[j - 1] + prev_row[j]) if j > 0 and j < i - 1 and i > 2 else 1
            for j in range(0, i)
        ]

        prev_row = row  # Update the previous row
        triangle.append(row)  # Add the current row to the triangle

    return triangle[1:]  # Exclude the first row with a single '1'