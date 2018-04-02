#from openpyxl import load_workbook
import pandas as pd
import numpy as np

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
print(PSD_data.shape)
print(PSD_data['Subject'])
PSD_mean_bands=PSD_data.groupby('Band')
print(PSD_mean_bands)