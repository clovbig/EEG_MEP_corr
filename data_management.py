"""
Author: Claudia Bigoni
Date: 08.10.2020
Date_latest_update: 09.10.2020
Description: Divide trials into single pulse or double pulse for both EEG and EMG
"""
import os
import mne
from scipy.io import loadmat
import pickle

from emg_class import EMG


errors_found = []
data_dir = 'C:\\Users\\bigoni\\Data\\TMS-EEG'
subjects = [i for i in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, i))]
for sub_id in subjects:
    print(f'Subject {sub_id}')
    t_points_eeg = [i for i in os.listdir(os.path.join(data_dir, sub_id, 'EEG')) if os.path.isdir(os.path.join(
        data_dir, sub_id, 'EEG', i))]
    t_points_emg = [i for i in os.listdir(os.path.join(data_dir, sub_id, 'EEG')) if os.path.isdir(os.path.join(
        data_dir, sub_id, 'EMG', i))]
    t_points = set(t_points_eeg + t_points_emg)
    for idx_tpoint, tpoint in enumerate(t_points):
        print(f'T point {tpoint}')
        sub_emg_data_sp = EMG(sub_id, 'SP')
        sub_emg_data_dp = EMG(sub_id, 'DP')
        for idx_seq, seq in enumerate(['A1', 'B1', 'A2', 'B2', 'A3', 'B3']):
            print(f'sequence {seq}')
            try:
                seq_epochs_emg = loadmat(
                    os.path.join(data_dir, sub_id, 'EMG', tpoint, 'Cleaned Data',
                                 f'TiMeS_{sub_id}_{tpoint}_{seq}_GUI_Results.mat'))
                trial_pulses = seq_epochs_emg['States']
                sub_emg_data_sp.add_trials(seq_epochs_emg, trial_pulses, idx_seq)
                sub_emg_data_sp.add_info_trials(seq_epochs_emg['SettingsGeneral'], len(trial_pulses[trial_pulses == 1]))
                sub_emg_data_dp.add_trials(seq_epochs_emg, trial_pulses, idx_seq)
                sub_emg_data_dp.add_info_trials(seq_epochs_emg['SettingsGeneral'], len(trial_pulses[trial_pulses == 2]))
            except FileNotFoundError:
                errors_found.append(f'EMG - {sub_id}-{tpoint}-{seq}')
            # for idx_t, t in enumerate(trial_pulses):
            #     print(f'trial n. {idx_t}')
            #     if t == 1:
            #         sub_emg_data_sp.add_trial(seq_epochs_emg, idx_tpoint, idx_t)
            #     elif t == 2:
            #         sub_emg_data_dp.add_trial(seq_epochs_emg, idx_tpoint, idx_t)
        f_name = os.path.join(data_dir, sub_id, 'EMG', tpoint, 'EMG_data_SP.pkl')
        p_file = open(f_name, 'wb')
        pickle.dump(sub_emg_data_sp, p_file)
        p_file.close()
        f_name = os.path.join(data_dir, sub_id, 'EMG', tpoint, 'EMG_data_DP.pkl')
        p_file = open(f_name, 'wb')
        pickle.dump(sub_emg_data_dp, p_file)
        p_file.close()

    f_name = os.path.join(data_dir, sub_id, 'EMG', 'not_found_files')
    p_file = open(f_name, 'w')
    for item in errors_found:
        p_file.write(item)
    p_file.close()
    # sub_eeg_data = []
    # for pulse in ['SP', 'DP']:
    #     for b in blocks:
    #         block_eeg_epochs = mne.io.read_epochs_eeglab(os.path.join(data_dir, sub_id, 'EEG', b, f'{pulse}_{sub_id}'
    #                                                               f'_{b}_ROI.set'))
    #         data_epochs_eeg = block_eeg_epochs.get_data()     # trials x channels x samples

