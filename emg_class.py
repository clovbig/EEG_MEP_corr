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

    def add_data(self, settings):
        self.name_examiner.append(settings['NameOfExaminer'][0][0][0])
        self.channel_muscles.append(settings['ChannelMuscles'][0][0])
        self.s_freq.append(settings['SamplFreq'][0][0][0][0])
        self.transmission_delay.append(settings['TransmissionDelay'][0][0][0][0])
        self.tms_trigger_time.append(settings['TMSTriggerTime'][0][0][0][0])
        self.signal_flipping.append(settings['SignalFlippingOn'][0][0][0][0])
        self.graph_window_width.append(settings['GraphWindowWidth'][0][0][0][0])


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

    def add_data(self, settings):
        self.dc_offset_start_time.append(settings['DCOffsetStartTime'][0][0][0][0])
        self.dc_offset_stop_time.append(settings['DCOffsetStopTime'][0][0][0][0])
        self.emg_background_Start_time.append(settings['EMGbackgroundStartTime'][0][0][0][0])
        self.emg_latency_sd.append(settings['EMGLatencySDvalue'][0][0][0][0])
        self.emg_module_offset.append(settings['EMGmoduleOffset'][0][0][0][0])
        self.cutoff_freq_high.append(settings['cutOffFreqHigh'][0][0][0][0])
        self.cutoff_freq_low.append(settings['cutOffFreqLow'][0][0][0][0])
        self.notch_freq.append(settings['notchFreq'][0][0][0][0])
        self.high_pass_filt.append(settings['highPassOn'][0][0][0][0])
        self.low_pass_filt.append(settings['lowPassOn'][0][0][0][0])
        self.notch_filt.append(settings['notchOn'][0][0][0][0])


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

    def add_data(self, settings):
        self.baseline_warning.append(settings['BaselineWarningOn'][0][0][0][0])
        self.baseline_bef_tms_warning.append(settings['BaselineBefTMSWarningOn'][0][0][0][0])
        self.mep_noise_check.append(settings['MEPNoiseCheckOn'][0][0][0][0])
        self.emg_noise_check_after_mep.append(settings['EMGNoiseCheckAfterMEP'][0][0][0][0])
        self.mep_vpp_check.append(settings['MEPVppCheckOn'][0][0][0][0])
        self.baseline_threshold.append(settings['BaselineThreshold'][0][0][0][0])
        self.baseline_correction_start.append(settings['baselineCorrectionStart'][0][0][0][0])
        self.baseline_correction_stop.append(settings['baselineCorrectionStop'][0][0][0][0])
        self.baseline_bef_tms_threshold.append(settings['BaselineBefTMSthreshold'][0][0][0][0])
        self.baseline_bef_tms_start.append(settings['BaselineBefTMSstart'][0][0][0][0])
        self.baseline_bef_tms_stop.append(settings['BaselineBefTMSstop'][0][0][0][0])
        self.mep_noise_threshold.append(settings['MEPnoiseThreshold'][0][0][0][0])
        self.mep_noise_checktime_offset_start.append(settings['MEPnoiseCheckTimeOffsetStart'][0][0][0][0])
        self.mep_noise_checktime_offset_stop.append(settings['MEPnoiseCheckTimeOffsetStop'][0][0][0][0])
        self.emg_after_mep_noise_threshold.append(settings['EMGafterMEPnoisethreshold'][0][0][0][0])
        self.emg_after_mep_noise_time_offset_start.append(settings['EMGNoiseAferMEPtimeOffsetStart'][0][0][0][0])
        self.emg_after_mep_noise_time_offset_stop.append(settings['EMGNoiseAferMEPtimeOffsetStop'][0][0][0][0])
        self.mep_pp_threshold.append(settings['MEPVppThreshold'][0][0][0][0])
        self.mep_checktime_offset_start.append(settings['MEPcheckTimeOffsetStart'][0][0])
        self.mep_checktime_offset_stop.append(settings['MEPchecktTimeOffsetStop'][0][0])
        self.important_ch_for_reject.append(settings['ImportantChForReject'][0][0][0][0])
        self.std_baseline_value.append(settings['stdBaselineValue'][0][0])
        self.threshold_type.append(settings['ThresholdType'][0][0][0])
        self.mep_threshold_per_trial_multipl.append(settings['MEPVppThresholdPerTrialMultipl'][0][0])
        self.mep_noise_threshold_per_trial_multipl.append(settings['MEPnoisethresholdPerTrialMultipl'][0][0])
        self.emg_after_mep_noise_threshold_per_trial_multipl.append(
            settings['EMGafterMEPnoisethresholdPerTrialMultipl'][0][0])
        self.baseline_bef_tms_threshold_per_trial_multipl.append(settings['BaselineBefTMSthresholdPerTrialMultipl'][0][0])
        self.baseline_threshold_per_trial_multipl.append(settings['BaselineThresholdPerTrialMultipl'][0][0])


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

    def add_data(self, res):
        self.discard_criteria.append(res['discardCriteria'][0][0][0][0])
        self.channels_for_rejection.append(res['channelsForRejection'][0][0][0][0])
        self.rej_results_per_ch_chosen_criteria.append(res['rejectionResultsPerChannelChosenCriteria'][0][0])
        self.rej_results_per_ch_all_criteria.append(res['rejectionResultsPerChannelAllCriteria'][0][0])
        self.rej_final_auto.append(res['rejectFinalAuto'][0][0][0][0])
        self.rej_final_manual.append(res['rejectFinalManual'][0][0][0][0])
        self.C1_baseline_value.append(res['C1_baseline_values'][0][0])
        self.C1_baseline_decision.append(res['C1_baseline_decision'][0][0])
        self.C2_baseline_bef_tms_value.append(res['C2_baselineBefTMS_values'][0][0])
        self.C2_baseline_bef_tms_decision.append(res['C2_baselineBefTMS_decision'][0][0])
        self.C3_mep_amp_value.append(res['C3_MEPamp_values'][0][0])
        self.C3_mep_amp_decision.append(res['C3_MEPamp_decision'][0][0])
        self.C4_noise_bef_mep_value.append(res['C4_noiseBefMEP_values'][0][0])
        self.C4_noise_bef_mep_decision.append(res['C4_noiseBefMEP_decision'][0][0])
        self.C5_noise_after_mep_value.append(res['C5_noiseAfterMEP_values'][0][0])
        self.C5_noise_after_mep_decision.append(res['C5_noiseAfterMEP_decision'][0][0])


class EMG:
    def __init__(self, sub_id, pulse='SP'):
        self.sub_id = sub_id
        self.pulse = pulse
        self.trial = 0
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

    def set_emg_data(self, data):
        self.mep = data['MEPVppValues'][0][0]
        self.emg_module_values = data['EMGModuleValues'][0][0]
        self.emg_rms_values = data['EMGRmsValues'][0][0]
        self.emg_latency_values = data['EMGLatencyValues'][0][0]
        self.std_baseline_values = data['stdBaselineValue'][0][0]

    def add_emg_data(self, data):
        self.mep = np.concatenate((self.mep, data['MEPVppValues'][0][0]), axis=0)
        self.emg_module_values = np.concatenate((self.emg_module_values, data['EMGModuleValues'][0][0]), axis=0)
        self.emg_rms_values = np.concatenate((self.emg_module_values, data['EMGRmsValues'][0][0]), axis=0)
        self.emg_latency_values = np.concatenate((self.emg_module_values, data['EMGLatencyValues'][0][0]), axis=0)
        self.std_baseline_values = np.concatenate((self.emg_module_values, data['stdBaselineValue'][0][0]), axis=0)

    def add_trial(self, epochs, block_no, trial_no):
        self.settings.add_data(epochs['SettingsGeneral'])
        self.settings_measurement.add_data(epochs['SettingsMeasurement'])
        self.settings_rejection.add_data(epochs['SettingsRejection'])
        self.rej_results.add_data(epochs['RejectionResults'])

        if self.trial == 0:
            self.processed_data = epochs['AllProcessedDat']     # samples x ch x trials
            self.processed_data = epochs['AllOriginalDat']     # samples x ch x trials
            self.set_emg_data(epochs['EMGdata'])
        else:
            self.processed_data = np.concatenate((self.processed_data, epochs['AllProcessedDat']), axis=2)
            self.processed_data = np.concatenate((self.processed_data, epochs['AllOriginalDat']), axis=2)
            self.add_emg_data(epochs['EMGdata'])

        self.trial += 1
        self.trials.append(trial_no)
        self.block.append(block_no)
        self.trials_all.append(trial_no + 60*block_no)
