from random import random

from scipy.stats import binom, uniform
import random

import argparse


with open("rf.txt", "r")as f:
    RG = f.read()
GACT = {0: 'G', 1: 'A', 2: 'C', 3: 'T'}
L = len(RG)


class Read:
    pos = 0
    line = []

    def __init__(self, line, pos):
        self.pos = pos
        self.line = line


def get_rand_ind(left: int, right: int, count: int) -> list:
    res_indexes = set()
    while len(res_indexes) < count:
        new_index = random.randrange(left, right)
        if new_index not in res_indexes:
            res_indexes.add(new_index)
    return list(res_indexes)


def read_with_error(true_sym):
    rand_sym = random.randrange(0, 4)
    while rand_sym == true_sym:
        rand_sym = random.randrange(0, 4)
    return (GACT[rand_sym])


def generate_read(l, s, err):
    res = list(s)
    k = binom.rvs(l, err)
    print("k=", k)
    err_lst = get_rand_ind(0, l, k)
    print("err_lst=", *err_lst)
    for pos in err_lst:
        res_pos = res[pos]
        res[pos] = read_with_error(list('GACT').index(res_pos))
    print(res)
    return (Read(line=res, pos=p))


def argparser():
   parser = argparse.ArgumentParser()
   # задаем минимальную дину рида (default=10)
   parser.add_argument('-m', default=10, type=int, help='MIN read\'s length')
   # задаем максимальную длину рида (default=10)
   parser.add_argument('-M', default=10, type=int, help='MAX read\'s length')
   # задаем error rate (default=0.05)
   parser.add_argument('-e', default=0.05, type=float, help='error rate')
   # задаем кол-во ридов (default=5)
   parser.add_argument('-n', default=5, type=int, help='number of reads')
   args = parser.parse_args()
   return(args.m, args.M, args.e, args.n)

reads = []
m, M, error, N = argparser()
print(argparser())
for i in range(N):
    l = m + binom.rvs(M-m, 0.5)
    print("l =",l)
    p = random.randint(0, L-l)
    reads.append(generate_read(l, RG[p:p+l], error))