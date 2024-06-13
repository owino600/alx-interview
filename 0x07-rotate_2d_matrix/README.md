### Rotate 2D Matrix

Given an n x n 2D matrix, rotate it 90 degrees clockwise.

## Prototype

```python
def rotate_2d_matrix(matrix):
    pass
```

## Description

This function takes in a 2D matrix and rotates it 90 degrees clockwise. The rotation is done in-place, meaning the original matrix is modified directly.

## Parameters

- `matrix`: The input 2D matrix to be rotated. It is guaranteed to have 2 dimensions and will not be empty.

## Example

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotate_2d_matrix(matrix)

# After rotation, the matrix becomes:
# [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
# ]
```