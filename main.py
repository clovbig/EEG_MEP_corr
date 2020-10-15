"""
Author: Claudia Bigoni
Date: 07.10.2020
Description: Check for possible correlation between EEG_phase and MEP
"""
import mne
import os
import pickle
import numpy as np
from scipy.io import loadmat
import matplotlib.pyplot as plt

import mep_analysis as ma
import signal_analysis as sig
import preprocessing as pp

emg_chs = {'FDI': 0, 'ADM': 1, 'APB': 2, 'FCU': 3, 'FCR': 4, 'ECR': 5, 'ECU': 6, 'FDI2': 7}
if __name__ == '__main__':
    # Load data
    data_dir = 'C:\\Users\\bigoni\\Data\\TMS-EEG'
    sub_id = 'WP11_002'
    t_point = 'T1'
    sequence = 'A1'
    pulse = 'SP'
    # Already epoched and cleaned EEG data (epochs between -0.2 and 0.5s where 0 is TMS pulse)
    epochs_eeg = mne.io.read_epochs_eeglab(os.path.join(data_dir, sub_id, 'EEG', t_point, f'{pulse}_{sub_id}'
                                                        f'_{t_point}_ROI.set'))   # trials x channels x samples
    fs_eeg = epochs_eeg.info['sfreq']
    data_epochs_eeg = epochs_eeg.get_data()     # trials x channels x samples
    # TODO: concatenate emg data for single pulse/double pulse like EEG data
    epochs_emg = pickle.load(open(os.path.join(data_dir, sub_id, 'EMG', t_point, f'EMG_data_{pulse}.pkl'), "rb"))
    # epochs_emg = loadmat(os.path.join(data_dir, sub_id, 'EMG', block, 'Cleaned Data', f'TiMeS_{sub_id}_{block}_'
    #                                   f'{sequence}_GUI_Results.mat'))
    # Variable definition
    fs_emg = 5000  # Hz
    f_band_emg = [2, 250]
    mu_band = [8, 13]
    beta_band = [14, 30]
    lesioned_hemisphere = 'left'
    emg_ch = 'FDI'
    eeg_ch = 'C4'
    # 1. Pre-process EMG
    meps = epochs_emg.mep[:, emg_chs[emg_ch]]
    # a. epoch for mep and remove artifacts trials
    epochs_mep = ma.divide_in_epochs(epochs_emg, fs_emg, 1, 0.02, 0.04)
    _, idx_remove_1 = ma.remove_artifacts_power(epochs_mep[:, emg_chs[emg_ch], :])
    # b. epoch for baseline emg and remove artifacts trials
    epochs_baseline_emg = ma.divide_in_epochs(epochs_emg, fs_emg, 1, -0.025, -0.005)
    _, idx_remove_2 = ma.remove_artifacts_corr(epochs_baseline_emg[:, emg_chs[emg_ch], :])
    # c. additional trials to remove according to previous pre-processing
    idx_remove_3 = epochs_emg.rej_results.C3_mep_amp_decision[:, emg_chs[emg_ch]]   # FIXME: check this...


    [emg_freq, emg_spectrum] = sig.fft(epochs_baseline_emg, fs_emg)
    emg_power = sig.compute_psd(emg_spectrum, emg_freq, f_band_emg[0], f_band_emg[1])

    # 2. Pre-process EEG
    # TODO maybe.. already preprocessed
    # a. epoch EEG in 6 sec trial with t=3s time of TMS pulse. Re-reference to average reference
    # epochs_eeg_6s = mne.Epochs(epochs_eeg, events=epochs_eeg.events, event_id=0, tmin=-3, tmax=3, baseline=None,
    #                        verbose=True)
    # b. remove artifacts and trials (eye blinks, signal drift, ...)
    # _, idx_remove_3 = eeg_artifacts_removal(epochs_eeg)

    # 3. Remove all trials containing trials in either mep, emg or eeg
    idx_remove = set([idx_remove_1, idx_remove_2, idx_remove_3])
    num_trials = len(meps)
    idx_keep = np.setdiff1d(range(0, num_trials), idx_remove)
    epochs_eeg = epochs_eeg[idx_keep, :, :]
    epochs_mep = epochs_mep[idx_keep]
    epochs_baseline_emg = epochs_mep[idx_keep]
    meps = meps[idx_keep]

    # 4. Filter EEG
    # a. space filter (Laplacian)
    # Choose the channel of interest according to the lesion site, hence the stimulation area
    if lesioned_hemisphere == 'left':
        ch = 'C4'
    elif lesioned_hemisphere == 'right':
        ch = 'C3'
    epochs_eeg = pp.spatial_filter(data_epochs_eeg, 'small_laplacian', epochs_eeg.ch_names)
    # b. frequency filter
    epochs_mu = pp.iir_bandpass_filter(data_epochs_eeg, mu_band[0], mu_band[1], fs_eeg, order=10, name='butter')
    epochs_beta = pp.iir_bandpass_filter(data_epochs_eeg, beta_band[0], beta_band[1], fs_eeg, order=10, name='butter')

    # 5. Compute PSD in EEG epochs pre stimulus
    # a. re-epoch between 2.848 and 2.998s
    epochs_power_mu = epochs_eeg
    spectrum, freq = sig.fft(epochs_power_mu, fs_eeg)
    mu_power = sig.compute_psd(spectrum, freq, mu_band[0], mu_band[1])

    epochs_power_beta = epochs_eeg
    spectrum, freq = sig.fft(epochs_power_beta, fs_eeg)
    beta_power = sig.compute_psd(spectrum, freq, beta_band[0], beta_band[1])

    # 6. Get instananeous frequency of EEG just before the TMS pulse
    # a. insta phase
    # b. define if peak, trough or nothing

    # 7. Find correlations between MEP and EEG power-phase
    pass
