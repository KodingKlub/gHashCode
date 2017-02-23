class EndpointDescription:
    def __init__(self, id, dc_latency, num_caches, cache_latencies):
        self.id = id
        self.dc_latency = dc_latency
        self.num_caches = num_caches
        self.cache_latencies = cache_latencies
