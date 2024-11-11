from collections import Counter
from matplotlib import pyplot as plt
import random
from vectors import sum_of_squares, dot
import math

num_friends = [random.randrange(0,100) for _ in range(204)]

minutes_per_day = [(num_friends - random.randrange(1 - num_friends, 20))*(30 - random.randrange(-10,10)) for num_friends in num_friends]
minutes_per_day2 = [random.randrange(120,1000) for num_friends in num_friends]

friends_counter = Counter(num_friends)

def mean(x):
    return sum(x)/len(x)

def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n//2

    if n % 2 == 1:
        return sorted_v[midpoint]
    else:
        lo = midpoint -1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi])/2  

def quantile(x, p):
    p_index = int(p*len(x))
    return sorted(x)[p_index]

def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x for x,count in counts.items() if count == max_count]

def data_range(x):
    return max(x) - min(x)

def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]

def variance(x):
    n = len(x)
    deviantions = de_mean(x)
    return sum_of_squares(deviantions)/(n-1)

def standart_deviantion(x):
    return math.sqrt(variance(x))

def covariance(x,y):
    n = len(x)
    return dot(de_mean(x),de_mean(y))/(n-1)

def correlation(x,y):
    stdet_x = standart_deviantion(x)
    stdet_y = standart_deviantion(y)

    if stdet_x > 0 and stdet_y > 0:
        return covariance(x,y)/stdet_y/stdet_x
    else:
        return 0
    

print(correlation(num_friends,minutes_per_day))
print(correlation(num_friends,minutes_per_day2))