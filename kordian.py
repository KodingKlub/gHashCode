import numpy as np
import wojtek as w
import philipp as p
import anna as a
import parser
import sys

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) == 2 else "data/small.in"
    problem = parser.get_problem(fname)