import matplotlib.pyplot as plt
import pandas as pd


def _read_channel(filename, n):
    """
        Чтение канала из .csv файла.
        :param filename: расположение .csv файла.
        :param n: номер канала из 'Fp1-M2,C3-M2,O1-M2,Fp2-M1,C4-M1,O2-M1'.
        :return: название канала, данные
    """
    file = pd.read_csv(filename)
    header = file.columns[n-1]
    header = header[2:] if n == 1 else header
    channel = file.iloc[:, n-1].tolist()

    return header, channel


def _read_channels(filename):
    """
        Чтение всех каналов из .csv файла.
        :param filename: расположение .csv файла.
        :return: массив называний каналов, массив из массивов данных каждого канала.
    """
    file = pd.read_csv(filename)
    headers = file.columns[:6].tolist()
    headers[0] = headers[0][2:]  # Удаляем решетку
    channels = [file.iloc[:, i].tolist() for i in range(6)]
    return headers, channels


def visual(filename: str, n: int):
    """
        Рисует график выбранного канала.
        :param filename: расположение .csv файла.
        :param n: номер канала из 'Fp1-M2,C3-M2,O1-M2,Fp2-M1,C4-M1,O2-M1'.
    """
    if n > 6 or n < 1:
        raise Exception('Поддерживаются только каналы 1-6')
    header, channel = _read_channel(filename, n)
    plt.figure(figsize=(15, 10))
    plt.plot(channel, label=header)
    plt.legend()
    plt.show()


def visual_all(filename: str):
    """
        Рисует графики всех каналов.
        :param filename: расположение .csv файла.
    """
    headers, channels = _read_channels(filename)
    plt.figure(figsize=(15, 10))

    for i in range(6):
        plt.subplot(3, 2, i + 1)
        plt.plot(channels[i], label=headers[i])
        plt.legend()

    plt.show()


if __name__ == '__main__':
    visual_all('../N-1.csv')
    visual('../N-1.csv', 1)
