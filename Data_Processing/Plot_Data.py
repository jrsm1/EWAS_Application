import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Testing
log = 1

# TODO Make Plots Pretty.
class Plot_Data():
    # TODO get sampling frequency from file.
    def __init__(self, filename):
        self.data_read = pd.read_csv(filename, header=90)
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

    # TODO Use a sensor List parameter to get column titles from file.
    def plt_time(self, sensor: str):
        """
        Plots raw data with respect to timestamp from file.
        """
        # TODO Read only the sensor column --> Optimization
        self.data_read.plot(x='Timestamp', y=sensor, legend=False, label=sensor)

        # Setup Plot Parameters.
        plt.title('RAW DATA')
        plt.legend()
        plt.show()

        return self  # Return Instance so that it can be linearly written in code.

    def plot_fft(self, sensor: str, sampling_rate):
        """
        Plot Fourier Transform using Numpy .fft algorithm.

        :param sensor : The sensor name which should be the name of the column which contains desired sensor information.
        :param sampling_rate : The

        :return Return Instance so that it can be linearly written in code.
        """
        #  Get Sensor columns values in a Series.
        fourier = np.fft.fft(self.data_read[sensor])

        # Calculate Sample spacing (inverse of the sampling rate).
        freq = np.fft.fftfreq(fourier.size, d=(1 / sampling_rate))

        plt.plot(freq, fourier.real ** 2 + fourier.imag ** 2)
        plt.ylabel('FFT')

        return self  # Return Instance so that it can be linearly written in code.

    # TODO finish with values from paper.
    def plot_CSD(self, sensor_1: str, sensor_2: str, sampling_freq):
        """
        Plots Cross Power Spectrum

        :param sensor_1: The value of the column name from the loaded files where the desired information is. [SENSOR 1 NAME]
        :param sensor_2: The value of the column name from the loaded files where the desired information is. [SENSOR 2 NAME]
        :param sampling_freq: The signal sampling frequency.

        :return: Instance so that it can be linearly written in code.
        """
        plt.csd(self.data_read[sensor_1], self.data_read[sensor_2], Fs=sampling_freq)

        return self  # Return Instance so that it can be linearly written in code.

    # TODO finish with values from paper.
    def plot_PSD(self, sensor: str, sampling_freq):
        """
        Plots Auto Power Spectrum

        :param sensor: The value of the column name from the loaded files where the desired information is. [SENSOR NAME]
        :param sampling_freq: The signal sampling frequency.

        :return: Instance so that it can be linearly written in code.
        """
        plt.psd(self.data_read[sensor], Fs=sampling_freq)

        return self  # Return Instance so that it can be linearly written in code.

    def plot_Phase(self, sensor: str, sampling_freq):
        """
        Plots Phase Spectrum of a single sensor.

        :param sensor: The value of the column name from the loaded files where the desired information is. [SENSOR NAME]
        :param sampling_freq: The signal sampling frequency.

        :return Return Instance so that it can be linearly written in code.
        """
        # sampling_freq = 1 / 0.1

        plt.phase_spectrum(x=self.data_read[sensor], Fs=sampling_freq)

        return self  # Return Instance so that it can be linearly written in code.

    def plot_coherence(self, sensor_1: str, sensor_2: str, sampling_freq):
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

        plt.cohere(s1, s2, sampling_freq)  # FIXME change 256 to display points.

        return self  # Return Instance so that it can be linearly written in code.

    # TODO change and implement with param title as List of Titles for more than one plot situation.
    # TODO call within each plot method to simplify code.
    @staticmethod
    def show_plot(title: str):
        """
        Creates necessary Qt Windows with interactive plots.
        Use with a plot method return to setup plots.

        :param title: Plot title.
        """
        plt.title(title)
        plt.legend()
        plt.show()


    # def get_sampling_frequency():
    #     df =


# TESTING.
# pdata = Plot_Data('Testing.csv')
# pdata.plt_time().show_plot('Sensor Plots')
# pdata.plot_coherence('S1', 'S2', 1000).show_plot('Coherence')
# pdata.plot_fft('S1', 1).show_plot('Fast Fourier Transform')
# pdata.plot_Phase('S1', 1).show_plot('Phase Spectrum')
# pdata.plot_CSD('S1', 'S2', 1000).show_plot('CSD Plot')  # FIXME leyenda.
# pdata.plot_PSD('S1', 1000).show_plot('PSD Plot')

# pdata.plt_time().plot_fft('S1').plot_PSD('S1', 1000).plot_CSD('S1', 'S2', 1000).plot_Phase('S1', 1000).plot_coherence('S1', 'S2').show_plot('All Plots')  # FIXME DOES NOT WORK.
