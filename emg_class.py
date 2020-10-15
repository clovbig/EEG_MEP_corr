"""
Author: Claudia Bigoni
Date: 08.10.2020
Date_latest_update: 09.10.2020
Description: Create structure for EMG data following .mat files
"""
import numpy as np


class SettingsGeneral:
    def __init__(self):
        self.name_examiner = []
        self.channel_muscles = []
        self.s_freq = []
        self.transmission_delay = []
        self.tms_trigger_time = []
        self.signal_flipping = []
        self.graph_window_width = []

    def add_data(self, settings, no_trials):
        self.name_examiner.append([settings['NameOfExaminer'][0][0][0]] * no_trials)
        self.channel_muscles.append([settings['ChannelMuscles'][0][0]] * no_trials)
        self.s_freq.append([settings['SamplFreq'][0][0][0][0]] * no_trials)
        self.transmission_delay.append([settings['TransmissionDelay'][0][0][0][0]] * no_trials)
        self.tms_trigger_time.append([settings['TMSTriggerTime'][0][0][0][0]] * no_trials)
        self.signal_flipping.append([settings['SignalFlippingOn'][0][0][0][0]] * no_trials)
        self.graph_window_width.append([settings['GraphWindowWidth'][0][0][0][0]] * no_trials)


class SettingsMeasurement:
    def __init__(self):
        self.dc_offset_start_time = []
        self.dc_offset_stop_time = []
        self.emg_background_Start_time = []
        self.emg_latency_sd = []
        self.emg_module_offset = []
        self.cutoff_freq_high = []
        self.cutoff_freq_low = []
        self.notch_freq = []
        self.high_pass_filt = []
        self.low_pass_filt = []
        self.notch_filt = []

    def add_data(self, settings, trials, pulse):
        self.dc_offset_start_time.append(settings['DCOffsetStartTime'][0][0][trials == pulse])
        self.dc_offset_stop_time.append(settings['DCOffsetStopTime'][0][0][trials == pulse])
        self.emg_background_Start_time.append(settings['EMGbackgroundStartTime'][0][0][trials == pulse])
        self.emg_latency_sd.append(settings['EMGLatencySDvalue'][0][0][trials == pulse])
        self.emg_module_offset.append(settings['EMGmoduleOffset'][0][0][trials == pulse])
        self.cutoff_freq_high.append(settings['cutOffFreqHigh'][0][0][trials == pulse])
        self.cutoff_freq_low.append(settings['cutOffFreqLow'][0][0][trials == pulse])
        self.notch_freq.append(settings['notchFreq'][0][0][trials == pulse])
        self.high_pass_filt.append(settings['highPassOn'][0][0][trials == pulse])
        self.low_pass_filt.append(settings['lowPassOn'][0][0][trials == pulse])
        self.notch_filt.append(settings['notchOn'][0][0][trials == pulse])


class SettingsRejection:
    def __init__(self):
        self.baseline_warning = []
        self.baseline_bef_tms_warning = []
        self.mep_noise_check = []
        self.emg_noise_check_after_mep = []
        self.mep_vpp_check = []
        self.baseline_threshold = []
        self.baseline_correction_start = []
        self.baseline_correction_stop = []
        self.baseline_bef_tms_threshold = []
        self.baseline_bef_tms_start = []
        self.baseline_bef_tms_stop = []
        self.mep_noise_threshold = []
        self.mep_noise_checktime_offset_start = []
        self.mep_noise_checktime_offset_stop = []
        self.emg_after_mep_noise_threshold = []
        self.emg_after_mep_noise_time_offset_start = []
        self.emg_after_mep_noise_time_offset_stop = []
        self.mep_pp_threshold = []
        self.mep_checktime_offset_start = []
        self.mep_checktime_offset_stop = []
        self.important_ch_for_reject = []
        self.std_baseline_value = []
        self.threshold_type = []
        self.mep_threshold_per_trial_multipl = []
        self.mep_noise_threshold_per_trial_multipl = []
        self.emg_after_mep_noise_threshold_per_trial_multipl = []
        self.baseline_bef_tms_threshold_per_trial_multipl = []
        self.baseline_threshold_per_trial_multipl = []

    def add_data(self, settings, trials, pulse):
        if len(trials) == len(settings['BaselineWarningOn'][0][0]):
            self.baseline_warning = np.concatenate(
                (self.baseline_warning, settings['BaselineWarningOn'][0][0][trials == pulse]))
            self.baseline_bef_tms_warning = np.concatenate(
                (self.baseline_bef_tms_warning, settings['BaselineBefTMSWarningOn'][0][0][trials == pulse]))
            self.mep_noise_check = np.concatenate(
                (self.mep_noise_check, settings['MEPNoiseCheckOn'][0][0][trials == pulse]))
            self.emg_noise_check_after_mep = np.concatenate(
                (self.emg_noise_check_after_mep, settings['EMGNoiseCheckAfterMEP'][0][0][trials == pulse]))
            self.mep_vpp_check = np.concatenate(
                (self.mep_vpp_check, settings['MEPVppCheckOn'][0][0][trials == pulse]))
            self.baseline_threshold = np.concatenate(
                (self.baseline_threshold, settings['BaselineThreshold'][0][0][trials == pulse]))
            self.baseline_correction_start = np.concatenate(
                (self.baseline_correction_start, settings['baselineCorrectionStart'][0][0][trials == pulse]))
            self.baseline_correction_stop = np.concatenate(
                (self.baseline_correction_stop, settings['baselineCorrectionStop'][0][0][trials == pulse]))
            self.baseline_bef_tms_threshold = np.concatenate(
                (self.baseline_bef_tms_threshold, settings['BaselineBefTMSthreshold'][0][0][trials == pulse]))
            self.baseline_bef_tms_start = np.concatenate(
                (self.baseline_bef_tms_start, settings['BaselineBefTMSstart'][0][0][trials == pulse]))
            self.baseline_bef_tms_stop = np.concatenate(
                (self.baseline_bef_tms_stop, settings['BaselineBefTMSstop'][0][0][trials == pulse]))
            self.mep_noise_threshold = np.concatenate(
                (self.mep_noise_threshold, settings['MEPnoiseThreshold'][0][0][trials == pulse]))
            self.mep_noise_checktime_offset_start = np.concatenate(
                (self.mep_noise_checktime_offset_start, settings['MEPnoiseCheckTimeOffsetStart'][0][0][trials == pulse]))
            self.mep_noise_checktime_offset_stop = np.concatenate(
                (self.mep_noise_checktime_offset_stop, settings['MEPnoiseCheckTimeOffsetStop'][0][0][trials == pulse]))
            self.emg_after_mep_noise_threshold = np.concatenate(
                (self.emg_after_mep_noise_threshold, settings['EMGafterMEPnoisethreshold'][0][0][trials == pulse]))
            self.emg_after_mep_noise_time_offset_start = np.concatenate(
                (self.emg_after_mep_noise_time_offset_start,
                 settings['EMGNoiseAferMEPtimeOffsetStart'][0][0][trials == pulse]))
            self.emg_after_mep_noise_time_offset_stop = np.concatenate(
                (self.emg_after_mep_noise_time_offset_stop,
                 settings['EMGNoiseAferMEPtimeOffsetStop'][0][0][trials == pulse]))
            self.mep_pp_threshold = np.concatenate(
                (self.mep_pp_threshold, settings['MEPVppThreshold'][0][0][trials == pulse]))
            self.mep_checktime_offset_start.append(settings['MEPcheckTimeOffsetStart'][0][0])
            self.mep_checktime_offset_stop.append(settings['MEPchecktTimeOffsetStop'][0][0])
            self.important_ch_for_reject = np.concatenate(
                (self.important_ch_for_reject, settings['ImportantChForReject'][0][0][trials == pulse]))
            self.std_baseline_value.append(settings['stdBaselineValue'][0][0])
            self.threshold_type.append([settings['ThresholdType'][0][0][0]]*len(trials[trials == pulse]))
            self.mep_threshold_per_trial_multipl.append(settings['MEPVppThresholdPerTrialMultipl'][0][0])
            self.mep_noise_threshold_per_trial_multipl.append(settings['MEPnoisethresholdPerTrialMultipl'][0][0])
            self.emg_after_mep_noise_threshold_per_trial_multipl.append(settings[
                'EMGafterMEPnoisethresholdPerTrialMultipl'][0][0])
            self.baseline_bef_tms_threshold_per_trial_multipl.append(
                settings['BaselineBefTMSthresholdPerTrialMultipl'][0][0])
            self.baseline_threshold_per_trial_multipl.append(settings['BaselineThresholdPerTrialMultipl'][0][0])
        else:
            print('Difference in trials length')
            pass
            # FIXME do sotming and send error

    def set_data(self, settings, trials, pulse):
        if len(trials) == len(settings['BaselineWarningOn'][0][0]):
            self.baseline_warning = settings['BaselineWarningOn'][0][0][trials == pulse]
            self.baseline_bef_tms_warning = settings['BaselineBefTMSWarningOn'][0][0][trials == pulse]
            self.mep_noise_check = settings['MEPNoiseCheckOn'][0][0][trials == pulse]
            self.emg_noise_check_after_mep = settings['EMGNoiseCheckAfterMEP'][0][0][trials == pulse]
            self.mep_vpp_check = settings['MEPVppCheckOn'][0][0][trials == pulse]
            self.baseline_threshold = settings['BaselineThreshold'][0][0][trials == pulse]
            self.baseline_correction_start = settings['baselineCorrectionStart'][0][0][trials == pulse]
            self.baseline_correction_stop = settings['baselineCorrectionStop'][0][0][trials == pulse]
            self.baseline_bef_tms_threshold = settings['BaselineBefTMSthreshold'][0][0][trials == pulse]
            self.baseline_bef_tms_start = settings['BaselineBefTMSstart'][0][0][trials == pulse]
            self.baseline_bef_tms_stop = settings['BaselineBefTMSstop'][0][0][trials == pulse]
            self.mep_noise_threshold = settings['MEPnoiseThreshold'][0][0][trials == pulse]
            self.mep_noise_checktime_offset_start = settings['MEPnoiseCheckTimeOffsetStart'][0][0][trials == pulse]
            self.mep_noise_checktime_offset_stop = settings['MEPnoiseCheckTimeOffsetStop'][0][0][trials == pulse]
            self.emg_after_mep_noise_threshold = settings['EMGafterMEPnoisethreshold'][0][0][trials == pulse]
            self.emg_after_mep_noise_time_offset_start = settings['EMGNoiseAferMEPtimeOffsetStart'][0][0][trials == pulse]
            self.emg_after_mep_noise_time_offset_stop = settings['EMGNoiseAferMEPtimeOffsetStop'][0][0][trials == pulse]
            self.mep_pp_threshold = settings['MEPVppThreshold'][0][0][trials == pulse]
            self.mep_checktime_offset_start = list(settings['MEPcheckTimeOffsetStart'][0][0])
            self.mep_checktime_offset_stop = list(settings['MEPchecktTimeOffsetStop'][0][0])
            self.important_ch_for_reject = settings['ImportantChForReject'][0][0][trials == pulse]
            self.std_baseline_value = list(settings['stdBaselineValue'][0][0])
            self.threshold_type.append([settings['ThresholdType'][0][0][0]]*len(trials[trials == pulse]))
            self.mep_threshold_per_trial_multipl = list(settings['MEPVppThresholdPerTrialMultipl'][0][0])
            self.mep_noise_threshold_per_trial_multipl = list(settings['MEPnoisethresholdPerTrialMultipl'][0][0])
            self.emg_after_mep_noise_threshold_per_trial_multipl = list(
                settings['EMGafterMEPnoisethresholdPerTrialMultipl'][0][0])
            self.baseline_bef_tms_threshold_per_trial_multipl = list(
                settings['BaselineBefTMSthresholdPerTrialMultipl'][0][0])
            self.baseline_threshold_per_trial_multipl = list(settings['BaselineThresholdPerTrialMultipl'][0][0])
        else:
            print('Difference in trials length')
            pass
            # FIXME do sotming and send error


class ResultsRejection:
    def __init__(self):
        self.discard_criteria = []
        self.channels_for_rejection = []
        self.rej_results_per_ch_chosen_criteria = []
        self.rej_results_per_ch_all_criteria = []
        self.rej_final_auto = []
        self.rej_final_manual = []
        self.C1_baseline_value = []
        self.C1_baseline_decision = []
        self.C2_baseline_bef_tms_value = []
        self.C2_baseline_bef_tms_decision = []
        self.C3_mep_amp_value = []
        self.C3_mep_amp_decision = []
        self.C4_noise_bef_mep_value = []
        self.C4_noise_bef_mep_decision = []
        self.C5_noise_after_mep_value = []
        self.C5_noise_after_mep_decision = []

    def set_data(self, res, trials, pulse):
        self.discard_criteria = (res['discardCriteria'][0][0][trials[trials == pulse]])
        self.channels_for_rejection = (res['channelsForRejection'][0][0][trials[trials == pulse]])
        self.rej_results_per_ch_chosen_criteria = res['rejectionResultsPerChannelChosenCriteria'][0][0][
                                                  trials[trials == pulse], :]
        self.rej_results_per_ch_all_criteria = (
            res['rejectionResultsPerChannelAllCriteria'][0][0][trials[trials == pulse], :])
        self.rej_final_auto = (res['rejectFinalAuto'][0][0][trials[trials == pulse]])
        self.rej_final_manual = (res['rejectFinalManual'][0][0][trials[trials == pulse]])
        self.C1_baseline_value = (res['C1_baseline_values'][0][0][trials[trials == pulse], :])
        self.C1_baseline_decision = (res['C1_baseline_decision'][0][0][trials[trials == pulse], :])
        self.C2_baseline_bef_tms_value = (res['C2_baselineBefTMS_values'][0][0][trials[trials == pulse], :])
        self.C2_baseline_bef_tms_decision = (res['C2_baselineBefTMS_decision'][0][0][trials[trials == pulse], :])
        self.C3_mep_amp_value = (res['C3_MEPamp_values'][0][0][trials[trials == pulse], :])
        self.C3_mep_amp_decision = (res['C3_MEPamp_decision'][0][0][trials[trials == pulse], :])
        self.C4_noise_bef_mep_value = (res['C4_noiseBefMEP_values'][0][0][trials[trials == pulse], :])
        self.C4_noise_bef_mep_decision = (res['C4_noiseBefMEP_decision'][0][0][trials[trials == pulse], :])
        self.C5_noise_after_mep_value = (res['C5_noiseAfterMEP_values'][0][0][trials[trials == pulse], :])
        self.C5_noise_after_mep_decision = (res['C5_noiseAfterMEP_decision'][0][0][trials[trials == pulse], :])

    def add_data(self, res, trials, pulse):
        self.discard_criteria = np.concatenate((self.discard_criteria, res['discardCriteria'][0][0][trials[
            trials == pulse]]))
        self.channels_for_rejection = np.concatenate((self.channels_for_rejection,
                                                      res['channelsForRejection'][0][0][trials[trials == pulse]]))
        self.rej_results_per_ch_chosen_criteria = np.concatenate((self.rej_results_per_ch_chosen_criteria,
            res['rejectionResultsPerChannelChosenCriteria'][0][0][trials[trials == pulse], :]))
        self.rej_results_per_ch_all_criteria = np.concatenate((self.rej_results_per_ch_all_criteria,
            res['rejectionResultsPerChannelAllCriteria'][0][0][trials[trials == pulse], :]))
        self.rej_final_auto = np.concatenate(
            (self.rej_final_auto, res['rejectFinalAuto'][0][0][trials[trials == pulse]]))
        self.rej_final_manual = np.concatenate(
            (self.rej_final_manual, res['rejectFinalManual'][0][0][trials[trials == pulse]]))
        self.C1_baseline_value = np.concatenate(
            (self.C1_baseline_value, res['C1_baseline_values'][0][0][trials[trials == pulse], :]))
        self.C1_baseline_decision = np.concatenate(
            (self.C1_baseline_decision, res['C1_baseline_decision'][0][0][trials[trials == pulse], :]))
        self.C2_baseline_bef_tms_value = np.concatenate(
            (self.C2_baseline_bef_tms_value, res['C2_baselineBefTMS_values'][0][0][trials[trials == pulse], :]))
        self.C2_baseline_bef_tms_decision = np.concatenate(
            (self.C2_baseline_bef_tms_decision, res['C2_baselineBefTMS_decision'][0][0][trials[trials == pulse], :]))
        self.C3_mep_amp_value  = np.concatenate(
            (self.C3_mep_amp_value, res['C3_MEPamp_values'][0][0][trials[trials == pulse], :]))
        self.C3_mep_amp_decision = np.concatenate(
            (self.C3_mep_amp_decision, res['C3_MEPamp_decision'][0][0][trials[trials == pulse], :]))
        self.C4_noise_bef_mep_value = np.concatenate(
            (self.C4_noise_bef_mep_value, res['C4_noiseBefMEP_values'][0][0][trials[trials == pulse], :]))
        self.C4_noise_bef_mep_decision = np.concatenate(
            (self.C4_noise_bef_mep_decision, res['C4_noiseBefMEP_decision'][0][0][trials[trials == pulse], :]))
        self.C5_noise_after_mep_value = np.concatenate(
            (self.C5_noise_after_mep_value, res['C5_noiseAfterMEP_values'][0][0][trials[trials == pulse], :]))
        self.C5_noise_after_mep_decision = np.concatenate(
            (self.C5_noise_after_mep_decision, res['C5_noiseAfterMEP_decision'][0][0][trials[trials == pulse], :]))


class EMG:
    def __init__(self, sub_id, pulse='SP'):
        self.sub_id = sub_id
        self.pulse = pulse
        if self.pulse == 'SP':
            self.pulse_no = 1
        elif self.pulse == 'DP':
            self.pulse_no = 2
        self.trial = 0
        self.seq = 0
        self.trials = []
        self.block = []
        self.trials_all = []
        self.ch_list = {'FDI': 0, 'ADM': 1, 'APB': 2, 'FCU': 3, 'FCR': 4, 'ECR': 5, 'ECU': 6, 'FDI2': 7}

        # Settings:
        self.settings = SettingsGeneral()
        self.settings_measurement = SettingsMeasurement()
        self.settings_rejection = SettingsRejection()
        # Rejection results:
        self.rej_results = ResultsRejection()

        # Data
        self.original_data = np.zeros((1, 8, 1))
        self.processed_data = np.zeros((1, 8, 1))
        self.rejection_results = np.zeros((1, 8, 60))

        # EMG data
        self.mep = []
        self.emg_module_values = []
        self.emg_rms_values = []
        self.emg_latency_values = []
        self.std_baseline_values = []

    def set_emg_data(self, data, trials):
        self.mep = data['MEPVppValues'][0][0][trials[trials == self.pulse_no], :]
        self.emg_module_values = data['EMGModuleValues'][0][0][trials == self.pulse_no, :]
        self.emg_rms_values = data['EMGRmsValues'][0][0][trials == self.pulse_no, :]
        self.emg_latency_values = data['EMGLatencyValues'][0][0][trials == self.pulse_no, :]
        self.std_baseline_values = data['stdBaselineValue'][0][0][trials == self.pulse_no, :]

    def add_emg_data(self, data, trials):
        self.mep = np.concatenate((self.mep, data['MEPVppValues'][0][0][trials == self.pulse_no, :]), axis=0)
        self.emg_module_values = np.concatenate(
            (self.emg_module_values, data['EMGModuleValues'][0][0][trials == self.pulse_no, :]), axis=0)
        self.emg_rms_values = np.concatenate(
            (self.emg_module_values, data['EMGRmsValues'][0][0][trials == self.pulse_no, :]), axis=0)
        self.emg_latency_values = np.concatenate(
            (self.emg_module_values, data['EMGLatencyValues'][0][0][trials == self.pulse_no, :]), axis=0)
        self.std_baseline_values = np.concatenate(
            (self.emg_module_values, data['stdBaselineValue'][0][0][trials == self.pulse_no, :]), axis=0)

    # def add_trial(self, epochs, block_no, trial_no):
    #     # self.settings.add_data(epochs['SettingsGeneral'])
    #     # self.settings_measurement.add_data(epochs['SettingsMeasurement'])
    #     # self.settings_rejection.add_data(epochs['SettingsRejection'])
    #     # self.rej_results.add_data(epochs['RejectionResults'])
    #
    #     if self.trial == 0:
    #         self.processed_data = epochs['AllProcessedDat']     # samples x ch x trials
    #         self.original_data = epochs['AllOriginalDat']     # samples x ch x trials
    #         self.set_emg_data(epochs['EMGdata'])
    #     else:
    #         self.processed_data = np.concatenate((self.processed_data, epochs['AllProcessedDat']), axis=2)
    #         self.original_data = np.concatenate((self.original_data, epochs['AllOriginalDat']), axis=2)
    #         self.add_emg_data(epochs['EMGdata'])
    #
    #     self.trial += 1
    #     self.trials.append(trial_no)
    #     self.block.append(block_no)
    #     self.trials_all.append(trial_no + 60*block_no)

    def add_trials(self, epochs_emg, trials, block_no):
        if self.seq == 0:
            self.processed_data = epochs_emg['AllProcessedDat'][:, :, trials == self.pulse_no]
            # samples x ch x  trials
            self.original_data = epochs_emg['AllOriginalDat'][:, :, [trials == self.pulse_no][0]]
            # samples x ch x trials
            self.set_emg_data(epochs_emg['EMGdata'], trials)
            self.settings_measurement.add_data(epochs_emg['SettingsMeasurement'], trials, self.pulse)
            self.settings_rejection.set_data(epochs_emg['SettingsRejection'], trials, self.pulse_no)
            self.rej_results.set_data(epochs_emg['RejectionResults'], trials, self.pulse_no)
        else:
            self.processed_data = np.concatenate(
                (self.processed_data, epochs_emg['AllProcessedDat'][:, :, trials == self.pulse_no]), axis=2)
            self.original_data = np.concatenate(
                (self.original_data, epochs_emg['AllOriginalDat'][:, :, trials == self.pulse_no]), axis=2)
            self.add_emg_data(epochs_emg['EMGdata'], trials)
            self.settings_measurement.add_data(epochs_emg['SettingsMeasurement'], trials, self.pulse)
            self.settings_rejection.add_data(epochs_emg['SettingsRejection'], trials, self.pulse_no)
            self.rej_results.add_data(epochs_emg['RejectionResults'], trials, self.pulse_no)

        self.seq += 1
        trial_no = trials == self.pulse_no
        tot_trials = np.arange(0, len(trials))
        self.trials.append(tot_trials[trial_no])
        self.block.append(block_no)
        self.trials_all.append(tot_trials[trial_no] + 60*block_no)

    def add_info_trials(self, settings_general, no_trials):
        self.settings.add_data(settings_general, no_trials)
