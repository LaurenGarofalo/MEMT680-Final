# -*- coding: utf-8 -*-
"""
MEMT680 Final Exam
Lauren Garofalo
"""
#%% Import Statements
import os
import numpy as np
import urllib
import time
import sys

#%% Download File
# This is a tool I have provided you to help you download your file.

def download_file(url, filename):
    """
    A function that downloads the data file from a URL
    Parameters
    ----------
    url : string
        url where the file to download is located
    filename : string
        location where to save the file
    reporthook : function
        callback to display the download progress
    """
    if not os.path.isfile(filename):
        urllib.request.urlretrieve(url, filename, reporthook)
        
def reporthook(count, block_size, total_size):
    """
    A function that displays the status and speed of the download
    """

    global start_time
    if count == 0:
        start_time = time.time()
        return
    duration = time.time() - start_time
    progress_size = int(count * block_size)
    speed = int(progress_size / (1024 * duration + 0.0001))
    percent = int(count * block_size * 100 / total_size)
    sys.stdout.write("\r...%d%%, %d MB, %d KB/s, %d seconds passed" %
                     (percent, progress_size / (1024 * 1024), speed, duration))
    sys.stdout.flush()
    
name = 'Lauren'
download_file(f'https://zenodo.org/record/7339649/files/data_{name}.npz?download=1','data.npz')    

#%% Loading the Data   
with np.load('data.npz', allow_pickle=True) as data:
    training_feat = data['training_feat']   
    training_true = data['training_true']
    validation_feat = data['validation_feat']
    
#%% Preprocessing the Data    
    
   