def transpose(matrix):
    if len(matrix) < 1:
        return matrix
    else:
        return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]


def powers(number_list, first, last):
    return [[i ** j for j in range(first, last + 1)] for i in number_list]


def matmul(m1, m2):
    mat = [[[m1[i][k]*m2[k][j] for k in range(len(m1[0]))] for j in range(len(m2[0]))] for i in range(len(m1))]
    return [[sum(mat[i][j]) for j in range(len(mat[0]))] for i in range(len(mat))]


def invert(matrix):
    a, b = matrix[0]
    c, d = matrix[1]
    det = a*d - b*c
    return [[d/det, -b/det], [-c/det, a/det]]


def loadtxt(file):
    with open(file, 'r') as f:
        mat = [[float(num) for num in line.split()] for line in f]
        f.close()
    return mat
