from functools import reduce
import math

def vector_add(v,w):
    return [i + j for (i,j) in zip(v,w)]

def vector_subtract(v,w):
    return [i - j for (i,j) in zip(v,w)]

def vectors_sum(vectors):
    return reduce(vector_add,vectors)

def scalar_multiply(v,c):
    return [c*i for i in v]

def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(vectors_sum(vectors),1/n)

def dot(v,w):
    return sum(v_i*w_i for v_i,w_i in zip(v,w))

def sum_of_squares(v):
    return dot(v,v)

def magnitude(v):
    return math.sqrt(sum_of_squares(v))

def square_distance(v,w):
    return sum_of_squares(vector_subtract(v,w))

def distance(v,w):
    return math.sqrt(square_distance(v,w))

def shape(A):
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows,num_cols

def get_row(A,i):
    return A[i]

def get_column(A,i):
    return [sub[i] for sub in A]

def make_matrix(num_rows, num_columns,entry_fn):
    return [[entry_fn(i,j) for j in range(num_columns)] for i in range(num_rows) ]

def is_diagonal(i, j):
    return 1 if i == j else 0

A = [[1,2],[3,4]]
