from self_py_fun.Quiz3Fun import *
import numpy as np

# You can use this .py script to perform debugging task.
sample_arr_1 = np.array([1,2,3,4,5])

def compute_D_partial(input_signal):
    signal_diff_one = np.diff(input_signal)  # Fix 1
    D_val = np.sum(np.sqrt(1 + signal_diff_one**2))  # Fix 2
    return D_val
d_1 = compute_D_partial(sample_arr_1)
# The correct d_1 should be 5.66.
