import numpy as np
from scipy import signal
import mne
import math


def iir_bandpass_filter(input_signal, f_min, f_max, fs, order=2, rs=5, rp=5, name='butter'):
    """Bandpass an input signal between f_min and f_max
    :param input_signal: 1xn array
    :param f_min: high-pass cutoff frequency (Hz)
    :param f_max: low-pass cutoff frequency (Hz)
    :param fs: sampling frequency (Hz)
    :param order: filter order
    :param rs:
    :param rp:
    :param name: name of filter type

    :return filtered_signal"""

    filtered_signal = input_signal
    if name == 'butter':
        filtered_signal = butterworth_filter(input_signal, f_min, f_max, fs, order)
    elif name == 'cheby1':
        filtered_signal = cheby1_filter(input_signal, f_min, f_max, fs, order, rp)
    elif name == 'cheby2':
        filtered_signal = cheby2_filter(input_signal, f_min, f_max, fs, order, rs)
    elif name == 'ellip':
        filtered_signal = ellip_filter(input_signal, f_min, f_max, fs, order, rp, rs)
    elif name == 'bessel':
        filtered_signal = bessel_filter(input_signal, f_min, f_max, fs, order)
    elif name == 'peak':
        Q = order
        f_center = (f_max - f_min)/2
        filtered_signal = peak_filter(input_signal, f_center, fs, Q)
    else:
        print('No available filter selected')

    return filtered_signal


def butterworth_filter(input_signal, f_min, f_max, fs, order):
    [b, a] = signal.butter(order, np.asarray([f_min, f_max]) / (fs / 2), btype='bandpass')
    filtered_signal = np.zeros(input_signal.shape)
    for idx, epoch in enumerate(input_signal):
        for ch in range(input_signal.shape[1]):
            filtered_signal[idx, ch, :] = signal.filtfilt(b, a, epoch[ch, :], padlen=np.min([input_signal.shape[2] -
                                                                                             5, 1000]))
    return filtered_signal


def cheby1_filter(input_signal, f_min, f_max, fs, order, rp):
    [b, a] = signal.cheby1(order, rp, np.asarray([f_min, f_max]) / (fs / 2), btype='bandpass')
    filtered_signal = signal.filtfilt(b, a, input_signal, padlen=np.min([len(input_signal) - 5, 1000]))
    return filtered_signal


def cheby2_filter(input_signal, f_min, f_max, fs, order, rs):
    [b, a] = signal.cheby2(order, rs, np.asarray([f_min, f_max]) / (fs / 2), btype='bandpass')
    filtered_signal = signal.filtfilt(b, a, input_signal, padlen=np.min([len(input_signal) - 5, 1000]))
    return filtered_signal


def ellip_filter(input_signal, f_min, f_max, fs, order, rp, rs):
    [b, a] = signal.ellip(order, rp, rs, np.asarray([f_min, f_max]) / (fs / 2), btype='bandpass')
    filtered_signal = signal.filtfilt(b, a, input_signal, padlen=np.min([len(input_signal) - 5, 1000]))
    return filtered_signal


def bessel_filter(input_signal, f_min, f_max, fs, order):
    [b, a] = signal.bessel(order, np.asarray([f_min, f_max]) / (fs / 2), btype='bandpass')
    filtered_signal = signal.filtfilt(b, a, input_signal, padlen=np.min([len(input_signal) - 5, 1000]))
    return filtered_signal


def peak_filter(input_signal, fc, fs, Q):
    b, a = signal.iirpeak(fc, Q, fs)
    filtered_signal = signal.filtfilt(b, a, input_signal)
    return filtered_signal


def spatial_filter(epoched_signal, fname, ch_list):     # from Avancer scripts..
    # FIXME: what is the montage?
    # epoched_signal: trials x channels x samples
    num_ch = epoched_signal.shape[1]
    for idx, epoch in enumerate(epoched_signal):
        for ch in range(num_ch):
            if fname == 'car':
                spatialfilter = np.ones([num_ch, num_ch]) / num_ch
                epoched_signal[idx, ch, :] = epoch - np.dot(spatialfilter, epoch)
            elif fname == 'small_laplacian':
                fact = 0.03
                interlec_dist = interelect_distance(ch_list, montage='CACS-64_REF')
                interlec_dist[interlec_dist > fact] = 0
                interlec_dist[interlec_dist != 0] = 1 / interlec_dist[interlec_dist != 0]
                row_sum = interlec_dist.sum(axis=1)
                spatialfilter = interlec_dist / row_sum[:, np.newaxis]
                epoched_signal[idx, ch, :] = epoch - np.dot(spatialfilter, epoch)
            elif fname == 'large_laplacian':
                interlec_dist = interelect_distance(ch_list, montage='CACS-64_REF')
                interlec_dist_inv = 1 / (interlec_dist + np.eye(num_ch)) - np.eye(num_ch)
                row_sum = interlec_dist_inv.sum(axis=1)
                spatialfilter = interlec_dist_inv / row_sum[:, np.newaxis]

                epoched_signal[idx, ch, :] = epoch - np.dot(spatialfilter, epoch)
            elif fname == 'gaussian_radial_diff':
                epsilon = 1 / 2
                interlec_dist = interelect_distance(ch_list, montage='CACS-64_REF', unit='auto')
                row_sum = interlec_dist.sum(axis=1)
                interlec_dist_norm = interlec_dist / row_sum[:, np.newaxis]
                radial_diff = np.exp((-1) * np.square(epsilon * interlec_dist_norm))
                radial_diff = radial_diff - np.eye(num_ch)
                row_sum = radial_diff.sum(axis=1)
                spatialfilter = radial_diff / row_sum[:, np.newaxis]
                epoched_signal[idx, ch, :] = epoch - np.dot(spatialfilter, epoch)
            else:
                epoched_signal[idx, ch, :] = epoch

    return epoched_signal


def interelect_distance(ch_list, path, montage='standard_1020', unit='auto'):
    """
    interelect_distance - Calculates inter-electrode codistances (linear distance).

    the montage is normalized to a sphere of radius equal to the average brain size (0.085 metres)

    :return:
    """
    elec = mne.channels.read_montage(montage, ch_list, unit=unit)

    new_pos = np.zeros(elec.pos.shape)

    for i, elem in enumerate(ch_list):
        new_pos[i] = elec.pos[elec.ch_names.index(elem)]

    locs = new_pos
    x = locs[:, 0]
    y = locs[:, 1]
    z = locs[:, 2]

    numelectrodes = len(x)

    cosdist = np.zeros((numelectrodes, numelectrodes))

    for i in range(numelectrodes):
        for j in range(i + 1, numelectrodes):

            cosdist[i, j] = np.sqrt(((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2)) / 2

    cosdist = cosdist + cosdist.T

    return cosdist


def surface_laplacian(data, ch_list, leg_order, m, smoothing, montage='standard_1020', path=[]):
    """
    This function attempts to compute the surface laplacian transform to an mne Epochs object. The
    algorithm follows the formulations of Perrin et al. (1989) and it consists for the most part in a
    nearly-literal translation of Mike X Cohen's 'Analyzing neural time series data' corresponding MATLAB
    code (2014).

    INPUTS are:
        - ch_list: channel num
        - leg_order: maximum order of the Legendre polynomial
        - m: smothness parameter for G and H
        - smoothing: smothness parameter for the diagonal of G
        - montage: montage to reconstruct the transformed Epochs object (same as in raw data import)

    OUTPUTS are:
        - before: unaffected reconstruction of the original Epochs object
        - after: surface laplacian transform of the original Epochs object

    References:
        - Perrin, F., Pernier, J., Bertrand, O. & Echallier, J.F. (1989). Spherical splines for scalp
          potential and current density mapping. Electroencephalography and clinical Neurophysiology, 72,
          184-187.
        - Cohen, M.X. (2014). Surface Laplacian In Analyzing neural time series data: theory and practice
          (pp. 275-290). London, England: The MIT Press.
    """

    # get electrodes positions
    elec = mne.channels.read_montage(montage, ch_list, path=path, unit='auto')

    new_pos = np.zeros(elec.pos.shape)

    for i, elem in enumerate(ch_list):
        new_pos[i] = elec.pos[elec.ch_names.index(elem)]

    locs = new_pos

    x = locs[:, 0]
    y = locs[:, 1]
    z = locs[:, 2]

    numelectrodes = len(x)
    orig_data_size = np.squeeze(data.shape)

    # normalize cartesian coordenates to sphere unit
    def cart2sph(x, y, z):
        hxy = np.hypot(x, y)
        r = np.hypot(hxy, z)
        el = np.arctan2(z, hxy)
        az = np.arctan2(y, x)
        return az, el, r

    junk1, junk2, spherical_radii = cart2sph(x, y, z)
    maxrad = np.max(spherical_radii)
    x = x / maxrad
    y = y / maxrad
    z = z / maxrad

    # compute cousine distance between all pairs of electrodes
    cosdist = np.zeros((numelectrodes, numelectrodes))
    for i in range(numelectrodes):
        for j in range(i + 1, numelectrodes):
            cosdist[i, j] = 1 - (((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2 + (z[i] - z[j]) ** 2) / 2)

    cosdist = cosdist + cosdist.T + np.identity(numelectrodes)

    # get legendre polynomials
    legpoly = np.zeros((leg_order, numelectrodes, numelectrodes))
    for ni in range(leg_order):
        for i in range(numelectrodes):
            for j in range(i + 1, numelectrodes):
                # temp = special.lpn(8,cosdist[0,1])[0][8]
                legpoly[ni, i, j] = special.lpn(ni + 1, cosdist[i, j])[0][ni + 1]

    legpoly = legpoly + np.transpose(legpoly, (0, 2, 1))

    for i in range(leg_order):
        legpoly[i, :, :] = legpoly[i, :, :] + np.identity(numelectrodes)

    # compute G and H matrixes
    twoN1 = np.multiply(2, range(1, leg_order + 1)) + 1
    gdenom = np.power(np.multiply(range(1, leg_order + 1), range(2, leg_order + 2)), m, dtype=float)
    hdenom = np.power(np.multiply(range(1, leg_order + 1), range(2, leg_order + 2)), m - 1, dtype=float)

    G = np.zeros((numelectrodes, numelectrodes))
    H = np.zeros((numelectrodes, numelectrodes))

    for i in range(numelectrodes):
        for j in range(i, numelectrodes):

            g = 0
            h = 0

            for ni in range(leg_order):
                g = g + (twoN1[ni] * legpoly[ni, i, j]) / gdenom[ni]
                h = h - (twoN1[ni] * legpoly[ni, i, j]) / hdenom[ni]

            G[i, j] = g / (4 * math.pi)
            H[i, j] = -h / (4 * math.pi)

    G = G + G.T
    H = H + H.T

    G = G - np.identity(numelectrodes) * G[1, 1] / 2
    H = H - np.identity(numelectrodes) * H[1, 1] / 2

    # compute C matrix
    Gs = G + np.identity(numelectrodes) * smoothing
    GsinvS = np.sum(np.linalg.inv(Gs), 0)
    dataGs = np.dot(data.T, np.linalg.inv(Gs))
    C = dataGs - np.dot(np.atleast_2d(np.sum(dataGs, 1) / np.sum(GsinvS)).T, np.atleast_2d(GsinvS))

    # apply transform
    surf_lap = np.reshape(np.transpose(np.dot(C, np.transpose(H))), orig_data_size)


    return surf_lap
