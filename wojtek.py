import philipp as p
import kordian as k
import solve
import sys

fname = sys.argv[1] if len(sys.argv) == 2 else "data/small.in"
problem = solve.get_problem(fname)

print(problem.num_caches)
print(len(problem.endpoints))