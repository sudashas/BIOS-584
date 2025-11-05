import os
import numpy as np
import scipy.io as sio
from HW8Fun import produce_trun_mean_cov, plot_trunc_mean, plot_trunc_cov

bp_low = 0.5
bp_upp = 6
electrode_num = 16
electrode_name_ls = ['F3', 'Fz', 'F4', 'T7', 'C3', 'Cz', 'C4', 'T8', 'CP3', 'CPz', 'CP4', 'P7', 'P3', 'Pz', 'P4', 'P8']
parent_dir = '/Users/suhasdas/Documents/GitHub/BIOS-584'
data_dir = os.path.join(parent_dir, 'data')
subject = 'K114'
session = '001_BCI_TRN'
time_index = np.linspace(0, 800, 25)

out_dir = os.path.join(parent_dir, 'K114_2')
mat_path = os.path.join(data_dir, f"{subject}_{session}_Truncated_Data_0.5_6.mat")
data = sio.loadmat(mat_path)
signal = data['Signal']
labels = np.squeeze(data['Type'], axis=1)

results = produce_trun_mean_cov(signal, labels, electrode_num)
tar_mean, ntar_mean, tar_cov, ntar_cov, all_cov = results

plot_trunc_mean(tar_mean, ntar_mean, time_index, electrode_name_ls, out_dir)
plot_trunc_cov([tar_cov, ntar_cov, all_cov], out_dir)