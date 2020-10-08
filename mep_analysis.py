"""
Author: Claudia Bigoni
Date: 06.10.2020
Description: MEP preprocessing following Hussain et al. Cerebral Cortex 2019
"""
import numpy as np
from scipy import stats
import signal_analysis as sig
# 1. peak-to-peak = max - min voltage deflection 20-40ms after TMS pulse
# 2. Artifact removal:
#   a. baseline EMG: -25 -5ms prestimulus
#   b. if more than half samples overs 75th percentile+3*interquartile range remove trial
#   c. if MEP low correlation with average MEP (r<40) -> artifact (avg MEP elicited by single pulse)
# 3. Normalize peak-to-peak to mean MEP for each subject and ln-transform


def divide_in_epochs(input_signal, fs, t_time=1, t_min=-0.025, t_max=-0.05):
    """Divide the input_signal in epochs according to a trigger. They will be between tmin and tmax. Trigger is at 1s
    :param input_signal: samples x channel x trial
    :param fs: sampling frequency (Hz)
    :param t_time: time of trigger
    :param t_min: starting time (related to trigger_t)
    :param t_max: ending time (related to trigger_t)
    """
    samp_t_min = int((t_time + t_min)*fs)
    samp_t_max = int((t_time + t_max) * fs)
    epochs = input_signal['AllOriginalDat'][samp_t_min:samp_t_max, :, :]
    # other option is to use input_signal['AllProcessedDat']

    return epochs


def remove_artifacts_corr(epoched_signal, thr=0.4):
    """Remove trials where MEP has lower correlation with average MEP"""
    mean_mep = np.mean(epoched_signal, axis=1)
    remove_idx = []
    for idx, epoch in enumerate(epoched_signal.T):
        corr_val = np.corrcoef(epoch, mean_mep)[0, 1]
        if corr_val <= thr:
            remove_idx.append(idx)
    keep_idx = np.setdiff1d(range(0, epoched_signal.shape[1]), remove_idx)
    clean_epochs = epoched_signal[:, keep_idx]

    return clean_epochs, remove_idx


def remove_artifacts_power(epoched_signal):
    # epoched_signal = samples x trials
    remove_idx = []
    for idx, epoch in enumerate(epoched_signal.T):
        perc75 = np.percentile(epoch, 75)
        iqr = stats.iqr(epoch)
        upper_limit = perc75 + 3*iqr
        samples_above_limit = epoch[epoch > upper_limit]
        if len(samples_above_limit) > len(epoch)/2:
            remove_idx.append(idx)
    keep_idx = np.setdiff1d(range(0, epoched_signal.shape[1]), remove_idx)
    clean_epochs = epoched_signal[:, keep_idx]
    return clean_epochs, remove_idx


def normalize_peak_to_peak_mep(epoched_signal, ptp):
    """Normalize peak_to_peak amplitudes to the mean MEP amplitude and ln transform it"""
    # FIXME: for each epoch? or general?
    ptp = (ptp-np.mean(epoched_signal, axis=1))/np.mean(epoched_signal, axis=1)
    ptp_ln = np.log(ptp)

    return ptp_ln


def compute_peak_to_peak_amp(epoched_signal):
    """For each epoch compute the maximum deflection of voltage, i.e. maxV-minV"""
    min_v = np.min(epoched_signal, axis=1)
    max_v = np.max(epoched_signal, axis=1)
    peak_to_peak = max_v - min_v

    return peak_to_peak
