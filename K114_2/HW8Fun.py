import numpy as np
import os
import matplotlib.pyplot as plt

def produce_trun_mean_cov(input_signal, input_type, E_val):
    length = input_signal.shape[1] // E_val
    tar = input_signal[input_type == 1]
    ntar = input_signal[input_type == -1]
    tar_mean = np.zeros((E_val, length))
    ntar_mean = np.zeros((E_val, length))
    tar_cov = np.zeros((E_val, length, length))
    ntar_cov = np.zeros((E_val, length, length))
    all_cov = np.zeros((E_val, length, length))
    for e in range(E_val):
        s = e * length
        e_ = (e + 1) * length
        tar_mean[e] = np.mean(tar[:, s:e_], axis=0)
        ntar_mean[e] = np.mean(ntar[:, s:e_], axis=0)
        tar_cov[e] = np.cov(tar[:, s:e_], rowvar=False)
        ntar_cov[e] = np.cov(ntar[:, s:e_], rowvar=False)
        all_cov[e] = np.cov(input_signal[:, s:e_], rowvar=False)
    return [tar_mean, ntar_mean, tar_cov, ntar_cov, all_cov]

def plot_trunc_mean(tar_mean, ntar_mean, time_index, labels, save_dir):
    plt.figure(figsize=(12, 8))
    for i in range(tar_mean.shape[0]):
        plt.plot(time_index, tar_mean[i], label=f'{labels[i]} (Target)')
        plt.plot(time_index, ntar_mean[i], label=f'{labels[i]} (Non-Target)', linestyle='--')
    plt.xlabel("Time (ms)")
    plt.ylabel("Amplitude")
    plt.title("Truncated Mean ERP Signals")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(save_dir, "Mean.png"))
    plt.close()

def plot_trunc_cov(cov_list, save_dir):
    names = ["Target", "Non-Target", "All"]
    for i, cov in enumerate(cov_list):
        avg_cov = np.mean(cov, axis=0)
        plt.imshow(avg_cov, cmap='viridis', aspect='auto')
        plt.colorbar()
        plt.title(f"Covariance - {names[i]}")
        plt.savefig(os.path.join(save_dir, f"Covariance_{names[i]}.png"))
        plt.close()