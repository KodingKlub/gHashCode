import numpy as np
import wojtek as w
import kordian as k
import anna as a
import parser
import sys

def merge_combination(combination1, combination2, problem):
    merged_combination = combination1

    for cache_id, cached_videos in combination1.items():
        video_information1 = cached_videos
        capacity1 = video_information1[0]
        videos1 = video_information1[1]

        video_information2 = combination2[cache_id]
        capacity2 = video_information2[0]
        videos2 = video_information2[1]

        if len(videos2) > 0:
            missing_videos = videos2.difference(videos1)
        else:
            missing_videos = []

        missing_video_sum = 0
        for video in missing_videos:
            missing_video_sum += problem.video_sizes[video]

        if (capacity1 + missing_video_sum) > problem.cache_size:
            return False

        if len(videos1) > 0:
            merged_videos = videos1.union(videos2)
        else:
            merged_videos = videos2

        merged_tuple = (capacity1 + missing_video_sum, merged_videos)
        merged_combination[cache_id] = merged_tuple

    return merged_combination

def savings(problem):
    endpoints_example = len(problem.endpoints)
    endpoint_savings = {}
    endpoint_combinations = {}

    for endpoint in problem.endpoints:  
        savings = np.ones((len(problem.video_sizes), problem.num_caches))
        savings *= -1

        for request in problem.get_requests_for_endpoint(endpoint.id):
            for cache in endpoint.cache_connections:
                cache_savings = endpoint.dc_latency - cache.latency
                savings[request.video_id,cache.cache_id] = request.num_requests * (cache_savings)

        endpoint_savings[endpoint] = savings

    return endpoint_savings

def merge_combination_data(combinations, problem):
    success = False
    N = 0
    X = np.zeros(len(problem.endpoints))

    while not success:

        combination1 = combinations[N][int(X[N])]
        combination2 = combinations[N+1][int(X[N+1])]

        merged_combination = merge_combination(
            combination1,
            combination2,
            problem
        )

        if merged_combination:
            N = N + 1
        else:

            if len(combinations[N+1]) > X[N+1] + 1:
                X[N+1] += 1
            else:
                X[N+1] = 0

                if len(combinations[N]) > X[N] + 1:
                    X[N] += 1
                else:
                    if N > 0:
                        N -= 1
                    else:
                        break

        if N + 1 == len(problem.endpoints):
            success = True

        print(N, len(problem.endpoints), X, merged_combination)

    print(success)

if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) == 2 else "data/small.in"
    problem = parser.get_problem(fname)

    print(savings(problem))

    combinations = {
        0: [
            {1: (50, {0}), 2: (30,{3})},
            {1: (50, {0}), 2: (30,{3})},
        ],
        1: [
            {1: (80,  {2}), 2: (80,{1,3})},
            {1: (80,  {2}), 2: (80,{1,3})},
        ]
    }

    merge_combination_data(combinations, problem)
