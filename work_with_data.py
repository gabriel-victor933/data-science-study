import math
from collections import Counter
import matplotlib.pyplot as plt
import random
from probabilidade import inverse_normal_cdf
from vectors import shape, make_matrix, get_column
from statistic import correlation, mean, standart_deviantion

random.seed(0)

def bucketize(point, bucket_size):
    return bucket_size*math.floor(point/bucket_size)

def make_histogram(points,bucket_size):
    return Counter(bucketize(point,bucket_size) for point in points)

def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()

def random_normal():
    return inverse_normal_cdf(random.random())

def correlation_matrix(data):

    _,num_columns = shape(data)

    def matrix_entry(i,j):
        return correlation(get_column(data,i),get_column(data,j))
    
    return make_matrix(num_columns, num_columns, matrix_entry)



bmi = [
    [63,160,150],
    [67,170.2,160],
    [70,177.8,171]
]

def scale(data):
    
    num_rows,nums_columns = shape(data)

    means = [mean(get_column(data,j)) for j in range(nums_columns)]
    stdevs = [standart_deviantion(get_column(data,j)) for j in range(nums_columns)]

    return means,stdevs


def rescale(data_matrix):
    means, stdevs = scale(data_matrix)

    def rescaled(i, j):
        if stdevs[j] > 0:
            return (data_matrix[i][j] - means[j]) / stdevs[j]
        else:
            return data_matrix[i][j]
        
    num_rows, num_cols = shape(data_matrix)
    return make_matrix(num_rows, num_cols, rescaled)


print(rescale(bmi))