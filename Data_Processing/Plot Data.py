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
        self.data_read.plot(x='timestamp', y='S1', legend=False, figsize=(20, 6), label='Sensor 1')
        self.data_read.plot(x='timestamp', y='S2', legend=False, figsize=(20, 6), label='Sensor 2')
        self.data_read.plot(x='timestamp', y='S3', legend=False, figsize=(20, 6), label='Sensor 3')
        self.data_read.plot(x='timestamp', y='S4', legend=False, figsize=(20, 6), label='Sensor 4')

        return self  # Return Instance so that it can be linearly written in code.

    def plot_coherence(self, sensor_1: str, sensor_2: str):
        # Get Colums as Series.
        s1 = self.data_read[sensor_1]  # each row is a list
        s2 = self.data_read[sensor_2]  # each row is a list

        plt.cohere(s1, s2, 256)  # FIXME change 256 to display points.

        plt.tight_layout()

        return self   # Return Instance so that it can be linearly written in code.


pdata = Plot_Data()
pdata.read_file(pdata.set_file('Data/Random_dummy_data_v2.csv'))
# pdata.plt_time().show_plot('Sensor Plots')
pdata.plot_coherence('S1', 'S2').show_plot('Coherence')
