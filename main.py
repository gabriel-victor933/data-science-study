import math

def mean(v):
    return sum(v)/len(v)

def sub_mean(v):
    x_bar = mean(v)
    return [x - x_bar for x in v]

def square_vector(v):
    return [x**2 for x in v]

def variance(v):
    squared = square_vector(sub_mean(v))
    return sum(squared)/(len(v)-1)

def deviation(v):
    return math.sqrt(variance(v))

def correlacao(x,y):
    sub_y = sub_mean(y)
    sub_x = sub_mean(x)

    stdet_x = deviation(x)
    stdet_y = deviation(y)

    return sum([x_i*y_i for x_i,y_i in zip(sub_x,sub_y)])/stdet_x/stdet_y
print(correlacao([1,2,3,4,5],[2,1,5,5,7]))