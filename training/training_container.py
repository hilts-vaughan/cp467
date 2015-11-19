__author__ = 'Vaughan Hilts <setsuna>'
# Represent a very basic data structure for holding training data for various characters. Given a request for a
# specific character, it returns the indexed data for this


class TrainingCluster:

    HISTOGRAM = "histogram"
    CENTROIDS = "centroids"

    def __init__(self):
        self.vectors = {}

    # This will overwrite any old data that might have existed there
    def add_vector(self, cluster_key, vector):
        self.vectors['cluster_key'] = vector

class TrainingContainer:

    def __init__(self):
        self.training_lookup = {}

    def add_cluster_for_key(self, key, cluster):
        # We should create an array for lookup if the key is not available yet
        if key not in self.training_lookup:
            self.training_lookup[key] = []

        # Append the cluster of data here
        self.training_lookup[key].append(cluster)

    # Allows us to fetch entire clusters from the cache
    def get_clusters_for_key(self, key):
        return self.training_lookup[key]
