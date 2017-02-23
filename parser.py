import wojtek as w
import philipp as p
import kordian as k
import endpoint
import req_description
import cache_connection

class Problem:
    def __init__(self, video_sizes, endpoints, requests, num_caches, cache_size):
        self.video_sizes = video_sizes
        self.endpoints = endpoints
        self.requests = requests
        self.num_caches = num_caches
        self.cache_size = cache_size
        self.req_per_endpoint = {}
        for i in range(len(endpoints)):
            self.req_per_endpoint[i] = [];

        for req in requests:
            self.req_per_endpoint[req.endpoint_id].append(req)

    def get_requests_for_endpoint(self, endpoint_id):
        return self.req_per_endpoint[endpoint_id]

def get_problem(fname):
    with open(fname) as f:
        content = f.readlines()

    content = [x.strip() for x in content]
    f = content[0].split(" ")
    V = int(f[0])
    E = int(f[1])
    R = int(f[2])
    C = int(f[3])
    X = int(f[4])

    videos = [int(vid) for vid in content[1].split(" ")]
    endpoints = []

    ct = 2
    for e in range(E):
        line = [int(s) for s in content[ct].split(" ")]
        latency = line[0]
        num_cache_conns = line[1]
        cache_conns = []
        ct += 1
        for ii in range(num_cache_conns):
            sp = [int(s) for s in content[ct].split(" ")]
            ct += 1
            cache_conn = cache_connection.CacheConnection(sp[0],sp[1])
            cache_conns.append(cache_conn)

        endp = endpoint.EndpointDescription(e, latency, num_cache_conns, cache_conns)
        endpoints.append(endp)

    requests = []
    for i in range(R):
        line = [int(s) for s in content[ct].split(" ")]
        ep_id = line[1]
        vid_id = line[0]
        num_req = line[2]
        requests.append(req_description.RequestDescription(vid_id, ep_id, num_req))
        ct += 1

    problem = Problem(videos, endpoints, requests, C, X)
    return problem