import numpy as np
import wojtek as w
import philipp as p
import anna as a
import parser
import sys
import itertools as it

def powerset(iterable):
    s = list(iterable)
    return list(it.chain.from_iterable(it.combinations(s, r) for r in range(1,len(s)+1)))

def get_combinations_dict(problem):
	endpoint_combinations = {}

	for endpoint in problem.endpoints:
		requests = problem.get_requests_for_endpoint(endpoint.id)
		videos = [1,2,3,4]
		videos = list(map(lambda x: x.video_id, requests))
		# video_sizes = problem.video_sizes
		caches = endpoint.cache_connections
		cache_ids = list(map(lambda x: x.cache_id, caches))
		# combinations_temp = {}

		video_combinations = powerset(videos)

		all_combinations_endpoint = []

		for video_combination in video_combinations:
			combinations = w.make_sets(video_combination, cache_ids)
			all_combinations_subset = []
			for combination in combinations:
				combination_dict = {}
				valid = True
				for c in combination:
					sum_vid_sizes = 0
					for vid in c[1]:
						sum_vid_sizes += problem.video_sizes[vid]
					if sum_vid_sizes > problem.cache_size:
						valid = False
					entry = (sum_vid_sizes, set(c[1]))
					combination_dict[c[0]] = entry
				if valid:
					all_combinations_subset.append(combination_dict)
			all_combinations_endpoint += all_combinations_subset
		endpoint_combinations[endpoint] = all_combinations_endpoint
	return endpoint_combinations

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) == 2 else "data/small.in"
    problem = parser.get_problem(fname)
    
    

    print(get_combinations_dict(problem))





          # for video_id in video_ids:
                # cache_combinations = []
                # for cache_id in cache_ids:
                #     combination = {}
                #     for inner_cache_id in cache_ids:
                #         if inner_cache_id == cache_id:
                #             combination[inner_cache_id] = (problem.video_sizes[video_id],set([video_id]))
                #         else:
                #             combination[inner_cache_id] = (0,set([]))
                #     cache_combinations.append(combination)
                # combinations_temp[video_id]

