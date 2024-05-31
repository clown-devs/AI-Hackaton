import numpy as np
import mne
from typing import IO
from typing import Tuple

def parse_file(file_path: str) -> Tuple[np.ndarray, str]:
    edf = mne.io.read_raw_edf(file_path)
    header = ','.join(edf.ch_names[:6]) # Хардкодим первые 6 каналов

    data = edf.get_data()[:6].T # Хардкодим первые 6 каналов

    return data, header


def save_to_csv(data: np.ndarray, header: str, output_filename: str):
    np.savetxt(output_filename, data, delimiter=',', header=header)
