# import numpy as np
# import mne

# edf = mne.io.read_raw_edf('N-1.edf')
# header = ','.join(edf.ch_names)

# data = edf.get_data().T

# np.savetxt('test.csv', data, delimiter=',', header=header)

import numpy as np
import mne

edf = mne.io.read_raw_edf('N16-1.edf')
header = edf.ch_names[0]  
print(edf.info)

data = edf.get_data()[0]  
print(len(data))
data = data.reshape(-1, 1) 
#np.savetxt('test.csv', data, delimiter=',', header=header)

# import matplotlib.pyplot as plt


# plt.figure(figsize=(10, 5))
# plt.plot(data)
# plt.title('Data from the first channel')
# plt.xlabel('Time')
# plt.ylabel('Amplitude')
# plt.show()