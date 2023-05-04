from __future__ import print_function, division

import numpy as np
# from windrose import WindroseAxes
from scipy.ndimage import label, binary_opening


# ---------------------------------------------------------

def percentile_pairs(arr, step_size):
    """...

    Parameters:
    -----------

    arr: input image as a numpy.ndarray

    step_size: chosen size for binning the percentile-based distribution of arr intensity values


    Returns:
    --------

    idx_steps: equivalent to numpy.arange(0,101, step_size)

    arr_steps: the percentile equivalent of idx_steps from arr

    val_pairs: tuples of the upper and lower ends of the percentile bins from arr_steps

    """

    idx_steps = np.arange(0, 101, step_size)
    arr_steps = np.percentile(arr, idx_steps).astype(float)
    val_pairs = np.asarray([(arr_steps[i], arr_steps[i + 1]) for i in range(arr_steps.shape[0] - 1)])

    return idx_steps, arr_steps, val_pairs


# ---------------------------------------------------------

def filter_arr_vals(arr, val_pairs):
    """...

    Parameters:
    -----------

    arr: input image as a numpy.ndarray

    val_pairs: tuples of the upper and lower ends of the percentile bins from arr_steps
               (typically returned from the function 'percentile_pairs')


    Returns:
    --------

    expanded_arr: numpy array with size equivalent to the merged tuple of len(val_pairs) followed by arr.shape[0]

    """

    expanded_arr = np.empty(np.concatenate(((val_pairs.shape[0],), arr.shape)))

    for i in range(val_pairs.shape[0]):
        p = val_pairs[i, :]
        i_arr = np.copy(arr)
        i_arr[arr <= p[0]] = 0
        i_arr[arr > p[1]] = 0
        expanded_arr[i, ...] = i_arr

    return expanded_arr


# ---------------------------------------------------------

def label_expansion(expanded_arr, noise_se_size=3):
    """...

    Parameters:
    -----------

    expanded_arr: numpy array with number of dimensions of len(input_image) + 1

    noise_se_size: width of the square structuring element used to remove small noise from expanded_arr.
                   default = 3.

    Returns:
    --------

    labeled_arr: numpy array with the same size as expanded_arr containing the N_8 or N_26 connected
                 component labeling result

    obj_ct:

    """

    dims = len(expanded_arr.shape) - 1
    n_layers = expanded_arr.shape[0]

    labeled_arr = np.empty_like(expanded_arr)
    obj_ct = np.empty(n_layers, dtype=int)

    if dims == 3:
        noise_se = np.ones((noise_se_size, noise_se_size, noise_se_size), dtype=np.uint8)
        label_se = np.ones((3, 3, 3), dtype=np.uint8)

    elif dims == 2:
        noise_se = np.ones((noise_se_size, noise_se_size), dtype=np.uint8)
        label_se = np.ones((3, 3), dtype=np.uint8)

    else:
        print('problem!')

    for i in range(n_layers):
        i_arr = expanded_arr[i, ...]
        i_lab, i_ct = label(binary_opening(i_arr, structure=noise_se), structure=label_se)
        labeled_arr[i, ...] = i_lab
        obj_ct[i] = i_ct

    return labeled_arr, obj_ct


# ---------------------------------------------------------

def det_obj_sizes(labeled_arr, obj_ct, n_layers, bg_val=0):
    """...

    Parameters:
    -----------

    labeled_arr:

    obj_ct:

    n_layers: integer indicating the number of layers where object size should be quantified.
              default = labeled_arr.shape[0].

    bg_val: default = 0.

    Returns:
    --------

    sizes:

    """

    sizes = [0] * n_layers
    for i in range(n_layers):
        i_arr = labeled_arr[i, ...]

        i_sizes = np.empty((obj_ct[i] + 1), dtype=int)
        for j in range(obj_ct[i] + 1):
            if j > bg_val:
                i_sizes[j] = np.where(i_arr.flatten() == j)[0].shape[0]
            else:
                i_sizes[j] = 0

        sizes[i] = np.vstack((np.arange(obj_ct[i] + 1), i_sizes)).T

    return sizes


# ---------------------------------------------------------

def mask_adj_obj(arr, labeled_arr):
    """...

    Parameters:
    -----------

    arr:

    labeled_arr:


    Returns:
    --------

    mask:

    indexed:

    umbrella_label:

    n:

    """

    mask = np.sum(labeled_arr, axis=0).astype(bool)
    indexed = np.copy(arr)
    indexed[mask == False] = 0
    print(indexed.shape)

    dims = len(arr.shape)
    if dims == 3:
        se = np.ones((3, 3, 3))
    elif dims == 2:
        se = np.ones((3, 3))
    else:
        print('problem!')

    umbrella_label, n = label(indexed, structure=se)

    return mask, indexed, umbrella_label, n


# ---------------------------------------------------------

def orientation_angles(indexed_arr):
    """...

    Parameters:
    -----------

    indexed_arr:


    Returns:
    --------

    x:

    """

    x = indexed_arr.flatten()
    x = x[x > 0]

    return x


# ---------------------------------------------------------

def rotate_angles(angles, val):
    """...

    Parameters:
    -----------

    angles:

    val:

    Returns:
    --------

    rotated:

    """

    rotated = np.empty_like(angles)

    for i in range(angles.shape[0]):
        i_a = angles[i]
        if i_a < val:
            rotated[i] = i_a - val + 180
        else:
            rotated[i] = i_a - val

    return rotated
