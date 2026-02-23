#!/usr/bin/env python3
"""Initialize K-means centroids"""

import numpy as np


def initialize(X, k):
    """
    Initializes cluster centroids for K-means

    X: numpy.ndarray of shape (n, d)
    k: positive integer (number of clusters)

    Returns: numpy.ndarray of shape (k, d) or None
    """
    if (not isinstance(X, np.ndarray) or len(X.shape) != 2 or
            not isinstance(k, int) or k <= 0):
        return None

    n, d = X.shape

    min_vals = np.min(X, axis=0)
    max_vals = np.max(X, axis=0)

return np.random.uniform(min_vals, max_vals, (k, d))
