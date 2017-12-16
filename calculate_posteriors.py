import numpy as np
import pymc3 as pm
import pandas as pd
import pickle
import os

# Read data
raw = pd.read_csv('./data.csv')
# Rename columns
raw.columns = ('t', 'label', 'stable', 'narrow', 'motivated', 'happy', 'unhappy', 'calm', 'worry', 'caffeine', 'sugar')


def is_prime(hex_array):
    int_array = [int(x, 16) for x in hex_array]
    bool_array = [all(x % i for i in range(2, x)) for x in int_array]
    return np.array(bool_array)


# Treatment data are labeled with prime numbers
treatment_data = raw.loc[is_prime(raw['label'])]
# Control data are labeled with odd non-prime numbers
control_data = raw.loc[np.invert(is_prime(raw['label']))]


def calculate_posterior(control_data, treatment_data, draws=2000, njobs=1):
    with pm.Model() as model:
        # Uniform Priors
        control_mean = pm.Uniform('control_mean', 1, 5)
        control_sd = pm.Uniform('control_sd', 0.1, 10)
        treatment_mean = pm.Uniform('treatment_mean', 1, 5)
        treatment_sd = pm.Uniform('treatment_sd', 0.1, 10)

        effect_mean = pm.Deterministic('effect_mean',
                                       treatment_mean - control_mean)

        # Define likelihood
        observed_control = pm.Normal(name='observed_control',
                                      mu=control_mean,
                                      sd=control_sd,
                                      observed=control_data)

        observed_treament = pm.Normal(name='observed_treatment',
                                      mu=treatment_mean,
                                      sd=treatment_sd,
                                      observed=treatment_data)
        print('Likelihood specified')

        trace = pm.sample(draws=draws, njobs=njobs)
    return (model, trace)


def mkdir(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


storage_folder_name = 'pymc3_files/'
mkdir(storage_folder_name)

for cog_property in ['stable', 'narrow', 'motivated', 'happy', 'unhappy', 'calm', 'worry']:
    # Run the model
    model, trace = calculate_posterior(treatment_data[cog_property], control_data[cog_property], draws=20000)

    # Pick a folder to put the traces into, e.g. pymc3_files/stable/
    folder_name = storage_folder_name + cog_property + '/'
    mkdir(folder_name)
    with open(folder_name + '/data.pickle', 'wb') as pickle_file:
        pickle.dump({'model': model, 'trace': trace}, pickle_file,
                    pickle.HIGHEST_PROTOCOL)
