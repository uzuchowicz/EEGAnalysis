#from openpyxl import load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats
import plotly
#from stats import probplot
from pandas.tools import plotting
import matplotlib
import plotly.plotly as py
plotly.tools.set_credentials_file(username='uzuchowicz', api_key='mkt4BEiLw1kbLYLP5BEf')
from plotly.tools import FigureFactory as FF
filename='SpectralAnalysis.xlsx'
sheetname='PowerSpectrum_all_s1_s2'
path="data\\"

#Read excel data
# excel_data = pd.ExcelFile(path+filename)
# data = excel_data.parse(sheetname).head(0)
# labels=tuple(data.head(0))
# power_spectrum_data=np.matrix(excel_data.parse(sheetname, skiprows =1))

excel_data=pd.read_excel(path+filename, skiprows=0)
labels=pd.read_excel(path+filename, header=0)
labels=tuple(labels)
excel_data=np.matrix(excel_data)

PSD_data=pd.read_excel(path+filename)
PSD_mean_bands=PSD_data.groupby('Band')
PSD_mean_response=PSD_data.groupby('Response')
PSD_mean_bands.boxplot(column=['Index'])
PSD_mean_response.boxplot(column=['Index'])

# Scatter matrices for different columns
#plotting.scatter_matrix(PSD_data[['Response', 'Group', 'Band']])

plt.show()

#testing normality
ks_results = scipy.stats.kstest(PSD_data['Index'], cdf='norm')

matrix_ks = [
    ['', 'DF', 'Test Statistic', 'p-value'],
    ['Sample Data', len(PSD_data) - 1, ks_results[0], ks_results[1]]
]

ks_table = FF.create_table(matrix_ks, index=True)
py.plot(ks_table, filename='ks-table')



# plot = probplot(PSD_data['Index'], dist='norm', plot=pylab)
# pylab.show()