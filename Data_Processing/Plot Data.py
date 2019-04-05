import pathlib

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib


class Plot_Data():

    def __init__(self):
        # Open in New Qt5 Interactive Window
        matplotlib.use('Qt5Agg')

    def show_plot(self, title: str):
        # Faster Rendering
        matplotlib.rcParams['path.simplify'] = True
        matplotlib.rcParams['path.simplify_threshold'] = 1.0

        plt.title(title)
        plt.legend()
        plt.show()

    def set_file(self, file_path):
        self.file_path = file_path

        return r'../' + file_path

    def read_file(self, file_path):
        self.data_read = pd.read_csv(str(file_path), header=12, index_col=0)
        # , names=['Col_1', 'Col_2', ... , 'COL_n')

        print(self.data_read)

    def plt_time(self):
        # Multiple Lines in same Plot.
        fig, ax = plt.subplots()
        self.data_read.plot(x='timestamp', y='S1', ax=ax, legend=False, figsize=(20, 6), label='Sensor 1')
        self.data_read.plot(x='timestamp', y='S2', ax=ax, legend=False, figsize=(20, 6), label='Sensor 2')
        self.data_read.plot(x='timestamp', y='S3', ax=ax, legend=False, figsize=(20, 6), label='Sensor 3')
        self.data_read.plot(x='timestamp', y='S4', ax=ax, legend=False, figsize=(20, 6), label='Sensor 4')

        return self  # Return Instance so that it can be linearly written in code.

    def plot_coherence(self, sensor_1, sensor_2):
        t = np.arange(0, len(sensor_1) / 100, 0.01)  # TODO REMOVE

        fig, axs = plt.subplots(2, 1)
        # axs[0].plot(t, s1, t, s2)
        # axs[0].set_xlim(0, 2)
        # axs[0].set_xlabel('time')
        # axs[0].set_ylabel('s1 and s2')
        # axs[0].grid(True)

        cxy, f = axs[1].cohere(s1, s2, 256)
        axs[1].set_ylabel('coherence')

        fig.tight_layout()
        plt.show()


pdata = Plot_Data()
pdata.read_file(pdata.set_file('Data/Random_dummy_data_v2.csv'))
pdata.plt_time().show_plot('Sensor Plots')
