#from openpyxl import load_workbook
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy
import plotly
#from stats import probplot
from pandas.tools import plotting
import matplotlib
import plotly.plotly as py
plotly.tools.set_credentials_file(username='uzuchowicz', api_key='mkt4BEiLw1kbLYLP5BEf')
from plotly.tools import FigureFactory as FF
import scipy.stats as sstats
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker
import scipy
import pylab
import functions as fct

filename = 'PSD_data_from_HERMES_data_v0.xls'
sheetname = 'Sheet1'

path = "data\\"

# Read excel data
# excel_data = pd.ExcelFile(path+filename)
# data = excel_data.parse(sheetname).head(0)
# labels=tuple(data.head(0))
# power_spectrum_data=np.matrix(excel_data.parse(sheetname, skiprows =1))

excel_data = pd.read_excel(path+filename, skiprows=0)
labels = pd.read_excel(path+filename, header=0)
labels = tuple(labels)
excel_data = np.matrix(excel_data)


index_data = pd.read_excel(path+filename)
index_mean_bands = index_data.groupby('Band')
index_mean_response = index_data.groupby('Response')

#index_mean_bands.boxplot(column=['Index'])
#index_mean_response.boxplot(column=['Index'])

# Scatter matrices for different columns
# plotting.scatter_matrix(PSD_data[['Response', 'Group', 'Band']])
# plt.show()

###################################################################################################################################################################
# # testing normality
# The normality criterion: each group compared should come from a population following the normal distribution.
#First method
ks_results = scipy.stats.kstest(index_data['Index'], cdf='norm')

matrix_ks = [
    ['', 'DF', 'Test Statistic', 'p-value'],
    ['Sample Data', len(index_data) - 1, ks_results[0], ks_results[1]]
]

ks_table = FF.create_table(matrix_ks, index=True)
#py.plot(ks_table, filename='ks-table')

# Second method
k2, pvalue = sstats.normaltest(index_data['Index']) #KS test statistic, either D, D+ or D-.p-value : float One-tailed or two-tailed p-value.
alpha = 1e-3
print("p-value = {:g}", pvalue)

if pvalue < alpha:  # null hypothesis: x comes from a normal distribution
    print("The null hypothesis can be rejected")
else:
    print("The null hypothesis cannot be rejected")

# for patient_idx in range(19):
#     if patient_idx == 6:
#         continue
#     t, p = sstats.ttest_rel(PLV_data_before[PLV_data_before["Subject"]==int(patient_idx+1)]["Index"], PLV_data_after[PLV_data_after["Subject"] ==int(patient_idx+1)]["Index"])
#

######################################################################################################################################################################
# The variance criterion (or 'homogeneity of variances'): samples should come from populations with the same variance.

#
# plt.hist(PLV_data['Index'])
# plt.show()


# statistic, pvalue = sstats.levene(PLV_data_MDD, PLV_data_BP)
#
#
# if pvalue < alpha:  # null hypothesis: x comes from a normal distribution
#     print("The null hypothesis can be rejected")
# else:
#     print("The null hypothesis cannot be rejected")



######################################################################################################################################################################
# plot = probplot(PSD_data['Index'], dist='norm', plot=pylab)
# pylab.show()

#####################################################################################################################################################################

index_mean_bands = index_data.groupby('Band')

index_data_MDD = index_data[index_data["Group"] == 1]
index_data_BP = index_data[index_data["Group"] == 2]

index_data_before = index_data[index_data["Condition"] == 1]
index_data_after = index_data[index_data["Condition"] == 2]

index_data_nonresponse = index_data[index_data["Response"] == 1]
index_data_response = index_data[index_data["Response"] == 2]

index_data_nonresponse_MDD = index_data_MDD[index_data["Response"] == 1]
index_data_response_MDD = index_data_MDD[index_data["Response"] == 2]

index_data_nonresponse_BP = index_data_BP[index_data["Response"] == 1]
index_data_response_BP = index_data_BP[index_data["Response"] == 2]

############################################################################################################################################
fct.two_factors_anova(index_data, 'Band', 'Group')
fct.two_factors_anova(index_data, 'Band', 'Response')
fct.two_factors_anova(index_data, 'Band', 'Condition')
fct.three_factors_anova(index_data, 'Band', 'Group', 'Condition')
fct.two_factors_anova(index_data_MDD, 'Band', 'Condition')
fct.two_factors_anova(index_data_BP, 'Band', 'Condition')
fct.three_factors_anova(index_data, 'EEG_channel', 'Group', 'Condition')
fct.two_factors_anova(index_data_MDD, 'EEG_channel', 'Condition')
fct.two_factors_anova(index_data_BP, 'EEG_channel', 'Condition')





###########################################################



##############################################################################################################
###############################CONDITION######################################################################

#  Czy aktywność EEG zmienia się pod wpływem stymulacji (CONDITION) w poszczególnych grupach pacjentów (GROUP) i
# czy zmiana ta zależy od pasma częstotliwości (BAND) i od topografii (CHANNEL) lub od obu tych zmiennych jednocześnie (BAND x CHANNEL) ?
# wykonać 3-czynnikową analizę ANOVA dla każdej z czterech grup osobno dla zmiennych CONDITION, BAND i CHANNEL (sporządzić wykresy dla:
#  CONDITION, CONDITION x BAND, CONDITION x CHANNEL, CONDITION x BAND x CHANNEL).



##############################################################################################################

# Scatter matrices for different columns
#plotting.scatter_matrix(PSD_data[['Response', 'Group', 'Band']])




