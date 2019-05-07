import numpy as np
from scipy.signal import argrelmin, argrelmax
# from scipy.spatial import distance


# parameter analysis utils
def find_spikes(v):
    # look for non-resting potential values
    ind = np.where(v < -10)
    v[ind] = -10
    ind = np.where(np.diff(v) < 0)
    v[ind] = -10

    # look for all slope changes
    v = (np.diff(v) > 0).astype(int)

    # get all change of slopes indices
    v_ind = np.where(np.diff(np.sign(v)))[0]

    # return last positive change of slope
    return v_ind[1::2]


def calc_features_step(U, t, dt, t_on, t_off):
    v = U.copy()
    N = v.shape[0]

    # resting potential
    rest_pot = np.mean(v[t<t_on])
    rest_pot_std = np.std(v[int(.9*t_on/dt):int(t_on/dt)])

    ind = find_spikes(v)

    spike_times = np.array(t)[ind]
    spike_times_stim = spike_times[(spike_times > t_on)  & (spike_times < t_off)]
    ind_stim1 = ind[(spike_times > t_on) & (spike_times < t_off)]
    ind_stim = ind_stim1.astype(int)

    firing_rate = 1e3*np.absolute(spike_times_stim.shape[0]/(t_off-t_on))
    time_1st_spike = spike_times_stim[spike_times_stim>t_on][0]

    ISI = np.diff(spike_times_stim).astype(float)


    sum_stats_vec = np.array([
                rest_pot,
                rest_pot_std,
                len(spike_times_stim),
                spike_times_stim,
                firing_rate,
                ISI.mean(),
                ISI.std()
                ])


    return sum_stats_vec


def calc_ramp_sum_stats(v, t, dt, t_on, t_off):
    """Calculate summary statistics of a single run with ramp current(single spike with DAP)"""
    stats = []
    stats_idx = []
#     v = v.transpose()
    N = v.shape[0]

    # resting potential
    rest_pot = np.mean(v[t<t_on])
    rest_pot_std = np.std(v[int(.9*t_on/dt):int(t_on/dt)])   # TODO: add if needed

    # RMSE
#     n = len(self.v0)
#     rmse = np.linalg.norm(v - self.v0) / np.sqrt(n)

    # more then one AP:
    multiple_AP = np.shape(np.where(v > 0))[1]

    #case without any action potential or more then one AP
    if (np.all(v <= 20)):
        AP_onsets = 999
        AP_amp = 999
        AP_width = 999
        DAP_amp = 999
        DAP_width = 999
        DAP_deflection = 999
        DAP_time = 999
        mAHP = 999
        fAHP = 999

    else:
        threshold = -30
        # hyperpolarization after DAP
        mAHP_idx = np.argmin(v)
        mAHP = v[mAHP_idx]

        # Action potential
        AP_onsets = np.where(v > threshold)[0]
        AP_start = AP_onsets[0]
        AP_end = AP_onsets[-1]
        AP_max_idx = AP_start + np.argmax(v[AP_start:AP_end])
        AP_max = v[AP_max_idx]
        AP_amp = AP_max - rest_pot

        # AP width
        AP_onsets_half_max = np.where(v > (AP_max+rest_pot)/2)[0]
        AP_width = t[AP_onsets_half_max[-1]] - t[AP_onsets_half_max[0]]

        # DAP: fAHP
        v_dap = v[AP_max_idx:]

        fAHP_idx = argrelmin(v[AP_max_idx:])[0][0] + AP_max_idx
        fAHP = v[fAHP_idx]

        # DAP amplitude
        DAP_max_idx = argrelmax(v_dap)[0][1] + AP_max_idx
        DAP_max = v[DAP_max_idx]
        DAP_amp = DAP_max - rest_pot

        DAP_deflection = DAP_amp - (fAHP - rest_pot)
        DAP_time = t[DAP_max_idx] - t[AP_max_idx]    # Time between AP and DAP maximum

        # Width of DAP: between fAHP and halfsize of fAHP after DAP max
        vnorm = v[DAP_max_idx:] - rest_pot

        if np.any((abs(vnorm) < abs(fAHP - rest_pot)/2)):
            half_max = np.where((abs(vnorm) < abs(fAHP - rest_pot)/2))[0]

            DAP_width_idx = DAP_max_idx + half_max[0]
            DAP_width = (DAP_width_idx - fAHP_idx) * dt
        else:
            DAP_width = 999


    sum_stats_vec = np.array([
                    rest_pot,
                    AP_amp,
                    AP_width,
                    fAHP,
                    DAP_amp,
                    DAP_width,
                    DAP_deflection,
                    DAP_time,
                    mAHP,
                    ])


    return sum_stats_vec
