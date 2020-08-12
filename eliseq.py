# 2x - 3y = 6
# x - y - 8z + 3 = 0
# 6 = 2x - 3y + 4z

# 2x - 3y + 0z = 6
# 1x - 1y - 8z = -3
# 2x - 3y + 4z = 6

import copy

def eliseq(_A, _b):
    A = copy.deepcopy(_A)
    b = copy.deepcopy(_b)
    # assume square
    m = len(A)
    for row in A:
        assert m == len(row)
    assert m == len(b)

    # multiply a row by x and add it to another row
    def row_multiply_and_add(src, target, factor):
        for i in range(m):
            A[target][i] += A[src][i] * factor
        b[target] += b[src] * factor

    # divide a row by x
    def row_multiply_in_place(row, factor):
        for i in range(m):
            A[row][i] *= factor
        b[row] *= factor

    for i in range(m):  # each pivot
        pivot = A[i][i]
        assert pivot != 0
        if pivot != 1:
            # make the pivot 1 by normalizing all the other terms
            row_multiply_in_place(row=i, factor=1 / pivot)
        for j in range(m):  # each row for pivot
            # don't need to do anything on the pivoting row
            if j == i: continue
            # eliminate the variable
            row_multiply_and_add(src=i, target=j, factor=-A[j][i])
    return b

# format number n
def pn(n):
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    if n < 0:
        return f"({n})"
    return n

# Ax = b
def print_eqns(A, x, b):
    m = len(A)
    # no asserts
    for i in range(m):
        print(" + ".join(f"{pn(A[i][j])} * {pn(x[j])}" for j in range(m)), end="")
        print(f" = {b[i]}")

# A = [
#     [2, -3, 0],
#     [1, -1, -8],
#     [2, -3, 4]
# ]
#
# b = [7, -2, 8]

A = [
    [1, 2, -1, 1],
    [-1, 1, 2, -1],
    [2, -1, 2, 2],
    [1, 1, -1, 2]
]

b = [6, 3, 14, 8]

if __name__ == '__main__':
    x = eliseq(A, b)
    print_eqns(A, x, b)
