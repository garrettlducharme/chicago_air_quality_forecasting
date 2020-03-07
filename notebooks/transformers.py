import numpy as np

def log_trans(y):
    y = np.array(y)
    return np.log10(y + 1)

def inv_log_trans(y):
    y = np.array(y)
    return 10**y - 1