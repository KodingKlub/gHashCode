class EndpointDescription:
    def __init__(self, id, dc_latency, num_cache_connections, cache_connections):
        self.id = id
        self.dc_latency = dc_latency
        self.num_cache_connections = num_cache_connections
        self.cache_connections = cache_connections
        self.requests = []
