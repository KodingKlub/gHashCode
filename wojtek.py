import numpy as np
import philipp as p
import kordian as k
import anna as a
import parser
import sys

def print_combination(combination):
    used_caches = sorted([k for k,v in combination.items() if v[0]!=0])
    print(len(used_caches))
    for used_cache in used_caches:
        print(" ".join([str(c) for c in combination[used_cache][1]]))

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) == 2 else "data/small.in"
    problem = parser.get_problem(fname)


    combination = {0:(80,[0,2]),1:(30,[1]),2:(0,[]),5:(10,[100])}
    for k,v in combination.items():
        print(k,v)
    print()
    print()
    print_combination(combination)

