"""Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?"""


def path_count(rows, cols):
    """step down and right from position (if possible), count possible paths from next step recursively"""
    if rows == 0 or cols == 0:
        # only 1 route to end, directly down or directly right
        return 1

    # if path length from square is already calculated, no need to recalculate
    if known_path_lengths[rows - 1][cols - 1] != -1:
        return known_path_lengths[rows - 1][cols - 1]

    paths = 0

    # step right
    paths += path_count(rows, cols - 1)

    # step down
    paths += path_count(rows - 1, cols)
    
    known_path_lengths[rows - 1][cols - 1] = paths

    return paths


size = 20
known_path_lengths = [[-1] * size for i in range(size)]
print(path_count(size, size))
