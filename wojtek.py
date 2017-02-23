import numpy as np
import philipp as p
import kordian as k
import anna as a
import parser
import sys

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) == 2 else "data/small.in"
    problem = parser.get_problem(fname)

    for r in problem.requests:
        print(r.endpoint_id)
