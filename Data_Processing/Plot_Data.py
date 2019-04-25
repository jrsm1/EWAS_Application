import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import GUI_Handler
import os
import sys
import time

# Testing
log = 1

# TODO AUMENTAR TAMAÑO LETRA DE LABELS EN LAS GRAFICAS.
class Plot_Data():
    def __init__(self, filename):
        """
        Loads Data from CSV File plots it's Raw_Data vs. Time | Auto-Powr Spectru, | Cross-Power Spectrum |
        Coherence | Phase Function | Fast Fourier Transform.

        Will also get from files needed parameters needed to plot.

        This Class Assumes User Application will always handle passing a valid Sensor from File.

        :param filename: File Containing Desired Data.
        """
        self.filename = filename
        try:
            self.sampling_rate = self.get_sampling_rate()
        except ValueError:
            GUI_Handler.show_error(' FATAL ERROR !!! <br> <br> File formatting Error <br> File seems to be corrupted. '
                                   ' <br>  <br> Restart Program...')

        self.data_read = pd.read_csv(self.filename, header=90)
        if log: print(self.data_read)

        # Open in New Qt5 Interactive Window
        matplotlib.use('Qt5Agg')

        # Faster Rendering
        matplotlib.rcParams['path.simplify'] = True
        matplotlib.rcParams['path.simplify_threshold'] = 1.0
        # Init Figure Parameters
        matplotlib.rcParams["figure.figsize"] = (20, 6)
        matplotlib.rcParams["figure.dpi"] = 80  # Makes Window Size in PIXELS = FIGURE_SIZE * DPI
        matplotlib.rcParams["figure.facecolor"] = '0.85'

    def plt_time(self, sensor: str):
        """
        Plots raw data with respect to timestamp from file.

        :param sensor:

        :return Plotted data in new Qt5Agg interactive Window.
        """
        # TODO Read only the sensor column --> Optimization
        self.data_read.plot(x='timestamp', y=sensor, legend=False, label=sensor)

        # Setup Plot Parameters.
        plt.title('RAW DATA')
        plt.ylabel('Voltage (V)')
        plt.legend()
        plt.show()

        return self  # Return Instance so that it can be linearly written in code.

    def plot_fft(self, sensor: str):
        """
        Plot Fourier Transform using Numpy .fft algorithm.

        :param sensor : The sensor name which should be the name of the column which contains desired sensor information.

        :return Return Instance so that it can be linearly written in code.
        """

        n = len(self.data_read[sensor])

        #  Get Sensor columns values in a Series.
        fourier = np.fft.fft(self.data_read[sensor])/n # Normalize

        # Calculate Sample spacing (inverse of the sampling rate).
        freq = np.fft.fftfreq(fourier.size, d=(1 / self.sampling_rate)/2)

        plt.plot(freq, fourier.real ** 2 + fourier.imag ** 2)

        # Setup Plot Parameters.
        plt.title('Frequency Spectrum of  ' + sensor)
        plt.ylabel('|Y(f)|')
        plt.xlabel('Frequency (Hz)')
        plt.show()

        return self  # Return Instance so that it can be linearly written in code.

    def plot_PSD(self, sensor: str):
        """
        Plots Auto Power Spectrum

        :param sensor: The value of the column name from the loaded files where the desired information is. [SENSOR NAME]
        :param sampling_freq: The signal sampling frequency.

        :return: Instance so that it can be linearly written in code.
        """

        plt.psd(self.data_read[sensor], Fs=self.sampling_rate)

        # Setup Plot Parameters.
        plt.title('Auto-Power Spectrum of ' + sensor)
        plt.show()

        return self  # Return Instance so that it can be linearly written in code.

    def plot_CSD(self, sensor_1: str, sensor_2: str):
        """
        Plots Cross Power Spectrum

        :param sensor_1: The value of the column name from the loaded files where the desired information is. [SENSOR 1 NAME]
        :param sensor_2: The value of the column name from the loaded files where the desired information is. [SENSOR 2 NAME]

        :return: Instance so that it can be linearly written in code.
        """

        plt.csd(self.data_read[sensor_1], self.data_read[sensor_2], Fs=self.sampling_rate)

        # Setup Plot Parameters.
        plt.title('Cross-Power Spectrum between  ' + sensor_1 + '  and  ' + sensor_2)
        plt.show()

        return self  # Return Instance so that it can be linearly written in code.

    def plot_Phase(self, sensor: str):
        """
        Plots Phase Function of a single sensor.

        :param sensor: The value of the column name from the loaded files where the desired information is. [SENSOR NAME]
        :param sampling_freq: The signal sampling frequency.

        :return Return Instance so that it can be linearly written in code.
        """

        plt.phase_spectrum(x=self.data_read[sensor], Fs=self.sampling_rate)

        # Setup Plot Parameters.
        plt.title('Phase Function of  ' + sensor)
        plt.show()

        return self  # Return Instance so that it can be linearly written in code.

    def plot_coherence(self, sensor_1: str, sensor_2: str):
        """
        Plot Coherence between two sensors.

        :param sensor_1: The value of the column name from the loaded files where the desired information is. [SENSOR 1 NAME]
        :param sensor_2: The value of the column name from the loaded files where the desired information is. [SENSOR 2 NAME]
        :param sampling_freq : The signal sampling frequency.

        :return Return Instance so that it can be linearly written in code.
        """

        # Get Columns as Series.
        s1 = self.data_read[sensor_1]  # each row is a list
        s2 = self.data_read[sensor_2]  # each row is a list

        plt.cohere(s1, s2, self.sampling_rate)

        # Setup Plot Parameters.
        plt.title('Coherence Function between  ' + sensor_1 + '  and  ' + sensor_2)
        plt.show()

        return self  # Return Instance so that it can be linearly written in code.

    def get_sampling_rate(self):
        """
        Gets Test Sample Frequency from File as an Integer.

        :return: Sampling Rate as Integer.
        """
        sf_string = self.data_read = pd.read_csv(self.filename, header=5, nrows=1, dtype=str).columns.tolist()[0]
        sample_freq = int(sf_string.split(' ')[0])

        return sample_freq


# TESTING.
# pdata = Plot_Data('../Data/Testing.csv')
# time = pdata.plt_time('Sensor_1')
# cohere = pdata.plot_coherence('Sensor_1', 'Sensor_2')
# fft = pdata.plot_fft('Sensor_1')
# phase = pdata.plot_Phase('Sensor_1')
# csd = pdata.plot_CSD('Sensor_1', 'Sensor_')
# psd = pdata.plot_PSD('Sensor_1')

# pdata.plt_time('Sensor_1').plot_coherence('Sensor_1', 'Sensor_2').plot_fft('Sensor_1').plot_PSD('Sensor_1').plot_CSD(
#     'Sensor_1', 'Sensor_2').plot_Phase('Sensor_1')
# pdata.plot_fft('Sensor_1')
