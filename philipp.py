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
    endpoint_savings = {}
    for endpoint in problem.endpoints:
        savings = np.ones((len(problem.video_sizes), problem.num_caches))
        savings *= -1

        for request in problem.get_requests_for_endpoint(endpoint.id):
            for cache in endpoint.cache_connections:
                cache_savings = endpoint.dc_latency - cache.latency
                savings[request.video_id,cache.cache_id] = request.num_requests * (cache_savings)

        endpoint_savings[endpoint] = savings


    print(endpoint_savings)