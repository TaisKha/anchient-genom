from scipy.stats import binom, uniform
import random
from main import *


# фиксированная длина ридов и фиксированная ошибка
l = 11
N = 2
data = []
err = 0.5

for _ in range(N):
    k = binom.rvs(l, err)
    err_lst = get_rand_ind(0, l, k)
    print(err_lst)
    res = [1 if i in err_lst else 0 for i in range(l)]
    print(res)
    data.append(res)
