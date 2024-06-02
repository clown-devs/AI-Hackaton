import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import keras

from sklearn.preprocessing import StandardScaler

def find_anomaly_interval(time):    
    time_answer = []
    i = 0
    time = list(time)
    while i < len(time) - 1:
        j = i
        i_start = i
        while (time[j+1] - time[j]) == 1 and j < len(time) - 2:
            j += 1
            i += 1
        time_answer.append((time[i_start], time[j]))
        i += 1
            
    return time_answer

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
    
    signal_in_channel = np.array(signal_in_channel).reshape(-1, 1)
    
    signal_in_channel = pd.DataFrame({'timestamp': np.arange(len(signal_in_channel)), 'value': signal_in_channel.reshape(-1)})
    
    signal_with_mean_transform = window_average(signal_in_channel['value'], 200, 200)
    print("WINDOW:",signal_with_mean_transform)
    ### OK! WITH Kakich local
    
    signal_with_mean_transform['value'] = scaler.fit_transform(signal_with_mean_transform[['value']])
    seq_size = 30

    signal_croped_in_windows, _ = to_seq(
        signal_with_mean_transform[['value']], 
        signal_with_mean_transform['value'], 
        seq_size=30
    )
    print("CROP:",signal_croped_in_windows)
    
    reconstructed_model = keras.models.load_model(path_to_model)

    #print("CROP:",signal_croped_in_windows)
    output = reconstructed_model(signal_croped_in_windows)
    max_trainMAE = 0.5  #or Define 90% value of max as threshold.

    testMAE = np.mean(np.abs(output - signal_croped_in_windows), axis=1)
    #print("testMAE:", testMAE)
    
    test = signal_with_mean_transform
    #print("TEST:", test)
    target = 'Fp1-M2'
    #Capture all details in a DataFrame for easy plotting
    anomaly_df = pd.DataFrame(test[30:])
    anomaly_df['testMAE'] = testMAE
    anomaly_df['max_trainMAE'] = max_trainMAE
    anomaly_df['anomaly'] = anomaly_df['testMAE'] > anomaly_df['max_trainMAE']
    anomaly_df[target] = test['value']
    anomaly_df['time'] = anomaly_df.index
    
    anomalies = anomaly_df.loc[anomaly_df['anomaly'] == True]
    
    anomaly_intervals = find_anomaly_interval(anomalies['time'])
 
    return anomaly_intervals