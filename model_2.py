from scipy.stats import binom, uniform
import random
from main import *

# фиксированная длина ридов
l = 10
N = 2
data = []
for _ in range(N):
    cube = [random.uniform(0, 1) for i in range(l)]
    p = [1/x for x in range(1, l+1)]
    res = [1 if cube[i] < p[i] else 0 for i in range(l)]
    data.append(res)