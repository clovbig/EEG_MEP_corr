import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


def snr(input_signal, f_band, fs, detrend=True):
    """Estimate the signal-to-noise ration (snr) for the input signal in the frequency band of interest f_band"""
    [frequency, power] = signal.welch(input_signal, fs, nperseg=2 * fs, noverlap=int(len(input_signal) / 2),
                                      detrend=detrend)
    bins_selected = np.where(np.logical_and(frequency >= 2, frequency <= 45))
    frequency = frequency[bins_selected]
    power = power[bins_selected]

    log_freq = np.log10(frequency)
    log_power = 10 * np.log10(power)

    alpha_bins = np.where(np.logical_and(frequency >= f_band[0], frequency <= f_band[1]))[0]
    alpha_log_power = log_power[alpha_bins]
    try:
        max_peak = frequency[alpha_bins[np.where(alpha_log_power == max(alpha_log_power))]]
        snr = alpha_log_power / log_power
    except ValueError:
        max_peak = 0
        snr = 0

    # # fit log power (as Zrenner et al., 2020)
    # lower_alpha_bins = np.where(frequency < f_band[0])
    # higher_alpha_bins = np.where(frequency > f_band[1])
    #
    # idx_freq = [lower_alpha_bins, higher_alpha_bins]
    # log_freq_roi = [np.ones(1, len(idx_freq)), log_freq(idx_freq)]
    # log_power_roi = [log_power[lower_alpha_bins], log_power[higher_alpha_bins]]
    #
    # fit = np.asarray(log_freq_roi) / np.asarray(log_power_roi).T
    # slope = fit[2]
    # intercept = fit[1]
    # fit_1f = slope * np.log10(frequency) + intercept
    # power_corrected = log_power - fit_1f
    #
    # # find alpha peak
    # [pks, locs] = signal.find_peaks(power_corrected, threshold=0.5)
    # locs_alpha = np.intersect1d(locs, alpha_bins)
    # peak_SNR = power_corrected[locs_alpha]
    # noise_level = np.mean(power_corrected[lower_alpha_bins])
    # spect = frequency
    #
    # # select the maximum alpha_peak
    # [_, idx_max] = max(peak_SNR)
    # peak_frequency = spect(locs_alpha[idx_max])
    # peak_SNR = peak_SNR(idx_max)
    return snr, max_peak


def instantaneous_phases(input_signal):
    """Compute phase for each sample in input signal using Hilbert Function. Phases are wrapped between -pi and pi"""
    analytic_signal = signal.hilbert(input_signal)
    instantaneous_phase = (np.angle(analytic_signal))
    phases_wrap = np.remainder(instantaneous_phase, 2 * np.pi)
    mask = np.abs(phases_wrap) > np.pi
    phases_wrap[mask] -= 2 * np.pi * np.sign(phases_wrap[mask])

    return phases_wrap


def fft(input_signal, fs, plot=False):
    """Compute spectrum of input_signal sampled with fs frequency using fft. Eventually plot full
    spectrum."""
    y = np.fft.fft(input_signal, n=fs)
    freq = np.fft.fftfreq(fs, d=1 / fs)
    idx_frequency = freq[:round(len(y) / 2)]
    signal_fft = 2.0 / len(y) * np.abs(y[0:len(y) // 2])
    if plot:
        plt.plot(idx_frequency, signal_fft)
    return idx_frequency, signal_fft


def compute_psd(spectrum, frequencies, f_min, f_max):
    """Given the spectrum of a signal, return the power in a frequency band [f_min, f_max]"""
    power = np.sum(spectrum[np.where(np.logical_and(frequencies >= f_min, frequencies <= f_max))])

    return power

