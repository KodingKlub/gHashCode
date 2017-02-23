import numpy as np
import wojtek as w
import kordian as k
import anna as a
import parser
import sys

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) == 2 else "data/small.in"
    problem = parser.get_problem(fname)

		endpoints_example = len(problem.endpoints)
		endpoint_savings = []
		for endpoint in range(endpoint_savings):
				savings = np.zeros(len(problem.videos),len(problem.num_caches))
				for request in problem.endpoints.requests:
					for cache in problem.endpoint.caches:
						cache_saving = endpoint.datacenterlatency - cache.latency
						savings[request.video,cache.id] = request.amount * (cache_savings)
				endpoint_savings.append(savings)
