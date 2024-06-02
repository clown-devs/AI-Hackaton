import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras

from sklearn.preprocessing import StandardScaler

def window_average(numbers, window_size, step_size):
    return pd.DataFrame([np.mean(numbers[i:i+window_size]) for i in range(0, len(numbers)-window_size+1, step_size)], columns=['value'])

def to_seq(x, y, seq_size=1):
    x_values = [] 
    y_values = []
    
    for i in range(len(x) - seq_size):
        x_values.append(x.iloc[i: (i + seq_size)].values)
        y_values.append(y.iloc[i + seq_size])
        
    return np.array(x_values), np.array(y_values)


def predict_result(data, path_to_model):
    
    scaler = StandardScaler()

    channel = 0
    signal_in_channel = data
    print("SIGNAL", signal_in_channel.shape)
    signal_in_channel = np.array(signal_in_channel).reshape(-1, 1)
    scaler.fit_transform(signal_in_channel)
    
    signal_in_channel = pd.DataFrame({'timestamp': np.arange(len(signal_in_channel)), 'value': signal_in_channel.reshape(-1)})
    
    signal_with_mean_transform = window_average(signal_in_channel['value'], 200, 200)
    print(signal_with_mean_transform.shape)
    
    seq_size = 30
    signal_croped_in_windows, _ = to_seq(
        signal_with_mean_transform[['value']], 
        signal_with_mean_transform['value'], 
        seq_size=seq_size
    )

    reconstructed_model = keras.models.load_model(path_to_model)
    
    output = reconstructed_model(signal_croped_in_windows)
    return output