import numpy as np
import mne
from typing import IO
from typing import Tuple

def parse_file(file_path: str) -> Tuple[np.ndarray, str]:
    edf = mne.io.read_raw_edf(file_path)

    data = edf.get_data()[0].T # Хардкодим первый канал

    return data, edf


def save_to_csv(data: np.ndarray, edf, output_filename: str):
    header = ','.join(edf.ch_names[0])
    np.savetxt(output_filename, data, delimiter=',', header=header)
