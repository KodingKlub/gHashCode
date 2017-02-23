import wojtek as w
import kordian as k
import solve
import sys

fname = sys.argv[1] if len(sys.argv) == 2 else "data/small.in"
problem = solve.get_problem(fname)