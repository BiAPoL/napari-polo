from __future__ import print_function, division

from skimage.io import imread, imsave
from tifffile import TiffFile

import os
import numpy as np

###---------------------------------------------------------


def load_orientation_files(fpath, str_filter, file_type):
    
    '''...
    
    Parameters:
    -----------
    
    fpath:
    
    str_filter:
    
    file_type:
    
    
    Returns:
    --------
    
    filt_files:
    
    filt_names:
    
    '''
    
    files = os.listdir(fpath)
    filt_files = []
    filt_names = []
    
    for i in files:
        if str_filter in i:
            if file_type == '.tif':
                filt_files.append(imread(os.path.join(fpath,i)))
            elif file_type == '.npy':
                filt_files.append(np.load(os.path.join(fpath,i)))
            filt_names.append(i)
        else:
            continue
    
    return filt_files, filt_names

###---------------------------------------------------------

def load_retardance_files(fpath, str_filter, ceiling_filter = 'Retardance Ceiling (nm)'):
    
    '''...
    
    Parameters:
    -----------
    
    fpath:
    
    str_filter:
    
    ceiling_filter: default = 'Retardance Ceiling (nm)'
    
    Returns:
    --------
    
    filt_files:
    
    file_ceilings:
    
    filt_names:
    
    '''
    
    files = os.listdir(fpath)
    
    filt_files = []
    filt_ceilings = []
    filt_names = []
    
    for i in files:
        
        if str_filter in i:
            with TiffFile(os.path.join(fpath, i)) as tif:
                arr = tif.asarray()
                imagej_metadata = tif.imagej_metadata 
            #test_metadata = list(imagej_metadata.values())[-1].split(',')
            test_metadata = str(imagej_metadata).split(',')
            
            counter = 0
            for j in test_metadata:
                if ceiling_filter in j:
                    break
                counter += 1
            ceiling = int(test_metadata[counter].split(':')[-1])
            
            filt_files.append(arr)
            filt_ceilings.append(ceiling)
            filt_names.append(i)
        else:
            continue
    
    return filt_files, filt_ceilings, filt_names

###---------------------------------------------------------

def prepro_orientation(files, process_type = 'float'):
    
    '''...
    
    Parameters:
    -----------
    
    files:
    
    process_type: default = 'float'
    
    
    Returns:
    --------
    
    prepro_files:
    
    '''
    
    prepro_files = [0] * len(files)
    counter = 0
    for i in files:
        if process_type == 'float':
            prepro_files[counter] = np.around(i/100, decimals = 3).astype(float)
            counter += 1
        elif process_type == 'int':
            prepro_files[counter] = (i/100).astype(i.dtype)
            counter += 1
        else:
            print('unknown process type')
        
    return prepro_files

###---------------------------------------------------------

def prepro_retardance(files, ceilings, process_type = 'float', floor = 0):
    
    '''...
    
    Parameters:
    -----------
    
    files:
    
    ceilings:
    
    process_type: default = 'float'
    
    floor: default = 0
    
    
    Returns:
    --------
    
    prepro_files:
    
    '''
    
    prepro_files = [0] * len(files)
    for i in range(len(files)):
        i_arr = files[i]
        i_ceil = ceilings[i]
        if process_type == 'float':
            prepro_files[i] = np.around(i_arr/i_ceil, decimals = 3).astype(float)
        elif process_type == 'int':
            prepro_files[i] = (i_arr/i_ceil).astype(i.dtype)
    
    return prepro_files

###---------------------------------------------------------

def check_pixel_balance(expanded_arr, n_checks):
    
    '''something is wrong with this function. n_checks = expanded_arr.shape[0]...
    
    Parameters:
    -----------
    
    expanded_arr:
    
    n_checks:
    
    
    Returns:
    --------
    
    px_cts:
    
    '''
    
    px_cts = np.empty(n_checks, dtype = int)
    
    for i in range(n_checks):
        px_cts[i] = np.sum(expanded_arr[i,...].astype(bool).astype(np.uint8))
    
    return px_cts

