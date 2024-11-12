from matplotlib import pyplot as plt
import math
import random
from collections import Counter

def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
    if x < 0: return 0 
    elif x < 1: return x
    else: return 1

def normal_pdf(x,mu=0,sigma=1):
    sqrt_two_pi = math.sqrt(2*math.pi)
    return math.exp(-((x-mu)**2)/(2*sigma**2))/(sqrt_two_pi*sigma)

def normal_cdf(x, mu=0,sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2

def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
# se não for padrão, computa o padrão e redimensiona
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0
    # normal_cdf(-10) está (muito perto de) 0
    hi_z, hi_p = 10.0, 1
    # normal_cdf(10) está (muito perto de) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2 # considera o ponto do meio e o valor da
        mid_p = normal_cdf(mid_z) # função de distribuição cumulativa lá
        if mid_p < p:
        # o ponto do meio ainda está baixo, procura acima
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
        # o ponto do meio ainda está alto, procura abaixo
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

def bernoulli_trial(p):
    return 1 if random.random() < p else 0

def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))

def make_hist(p, n, num_points):
    data = [binomial(n, p) for _ in range(num_points)]# usa um gráfico de barras para exibir as amostrar binomiais atuais
    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
    [v / num_points for v in histogram.values()],
    0.8,
    color='0.75')
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    # usa um gráfico de linhas para exibir uma aproximação da normal
    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mu, sigma) - normal_cdf(i - 0.5, mu, sigma)
    for i in xs]
    plt.plot(xs,ys)
    plt.title("Distribuição Binomial vs. Aproximação Normal" )
    plt.show()


def normal_approximation_to_binomial(n, p):
    mu = p * n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


normal_probability_below = normal_cdf

def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo,mu,sigma)

def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi,mu,sigma) - normal_cdf(lo,mu,sigma)

def normal_probability_outside(lo,hi, mu=0, sigma=1):
    return 1 - normal_probability_between(hi,lo, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    tail_probability = (1 - probability) / 2
    # limite superior deveria ter tail_probability acima
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    # limite inferior deveria ter tail_probability abaixo
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound



mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
print(mu_0,sigma_0)
lo, hi = normal_two_sided_bounds(0.95,mu_0, sigma_0)
print(lo, hi)


mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability # 0.887


hi = normal_upper_bound(0.95, mu_0, sigma_0)
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability # 0.936
print(power)

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
    # se x for maior do que a média, a coroa será o que for maior do que x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
    # se x for menor do que a média, a coroa será o que for menor do que x
        return 2 * normal_probability_below(x, mu, sigma)
    
print('p-values:',two_sided_p_value(529.5, mu_0, sigma_0))