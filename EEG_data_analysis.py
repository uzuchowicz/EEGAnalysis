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




filename='PSD_data_15epochs.xls'
sheetname='Sheet1'

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


index_data=pd.read_excel(path+filename)
index_mean_bands=index_data.groupby('Band')
index_mean_response=index_data.groupby('Response')
index_mean_bands.boxplot(column=['Index'])
index_mean_response.boxplot(column=['Index'])

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
index_data_MDD = index_data[index_data["Group"] == 1]["Index"]
index_data_BP = index_data[index_data["Group"] == 2]["Index"]

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

PLV_data_before = index_data[index_data["Condition"] == 1]["Index"]
PLV_data_after = index_data[index_data["Condition"] == 2]["Index"]

tips = sns.load_dataset("tips")
tips_agg = (tips.groupby(["day", "smoker"])
                .total_bill.agg([np.mean, sstats.sem])
                .reset_index())
tips_agg["low"] = tips_agg["mean"] - tips_agg["sem"]
tips_agg["high"] = tips_agg["mean"] + tips_agg["sem"]

# Define a wrapper function for plt.errorbar

def errorbar(x, y, low, high, order, color, **kws):
    xnum = [order.index(x_i) for x_i in x]
    plt.errorbar(xnum, y, (y - low, high - y), color=color)

# Draw the plot
g = sns.factorplot(x="day", y="mean", col="smoker", data=tips_agg)
order = sns.utils.categorical_order(tips_agg["day"])
g.map(errorbar, "day", "mean", "low", "high", order=order)



print('ANOVA:2 czynniki Band*Group')
f_val, p_val = sstats.f_oneway(index_data_MDD, index_data_BP)

print("One-way ANOVA P =", p_val)

sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 10}
sns.set_context("paper", rc = paper_rc)

# tips_agg = (PLV_data.groupby(["Band", "Group"])
#                 .Index.agg([np.mean, sstats.sem])
#                 .reset_index())
# tips_agg["low"] = tips_agg["mean"] - tips_agg["sem"]
# tips_agg["high"] = tips_agg["mean"] + tips_agg["sem"]

sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="Band", y="Index", hue="Response", col = "Group", data=index_data, fmt='none')
# order = sns.utils.categorical_order(tips_agg["Band"])
# g.map(errorbar, "Band", "Index", "low", "high", order=order)
plt.grid(True,which="both",ls="--",c='gray')
plt.show()

index_data_before = index_data[index_data["Condition"] == 1]
index_data_after = index_data[index_data["Condition"] == 2]

print('ANOVA:2 czynniki Band*Condition')
f_val, p_val = sstats.f_oneway(index_data_before, index_data_after)

print("One-way ANOVA P =", p_val)

sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 10}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="Band", y="Index", hue="Condition", data=index_data)
plt.grid(True,which="both",ls="--",c='gray')
plt.show()



index_data_nonresponse = index_data[index_data["Response"] == 1]
index_data_response = index_data[index_data["Response"] == 2]

print('ANOVA:2 czynniki Band*Condition')
f_val, p_val = sstats.f_oneway(PLV_data_before, PLV_data_after)

print("One-way ANOVA P =", p_val)

sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 7}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="Band", y="Index", hue="Response", data=index_data)
plt.grid(True,which="both",ls="--",c='gray')
plt.show()



PLV_data_before_MDD = index_data_MDD[index_data["Condition"] == 1]
PLV_data_after_MDD = index_data_MDD[index_data["Condition"] == 2]

PLV_data_before_BP = index_data_BP[index_data["Condition"] == 1]
PLV_data_after_BP = index_data_BP[index_data["Condition"] == 2]

print('ANOVA:2 czynniki Band*Condition*Group')
f_val, p_val = sstats.f_oneway(PLV_data_before_MDD, PLV_data_after_MDD)

print("One-way ANOVA P =", p_val)


print('ANOVA:2 czynniki Band*Condition')
f_val, p_val = sstats.f_oneway(PLV_data_before_BP, PLV_data_after_BP)

print("One-way ANOVA P =", p_val)


sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 7}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="Band", y="Index", hue="Condition",col="Group", data=index_data)
plt.show()



PLV_data_nonresponse_MDD = index_data_MDD[index_data["Response"] == 1]
PLV_data_response_MDD = index_data_MDD[index_data["Response"] == 2]

PLV_data_nonresponse_BP = index_data_BP[index_data["Response"] == 1]
PLV_data_response_BP = index_data_BP[index_data["Response"] == 2]

print('ANOVA:2 czynniki Band*Condition*Group')
f_val, p_val = sstats.f_oneway(PLV_data_nonresponse_MDD, PLV_data_response_MDD)

print("One-way ANOVA P =", p_val)


print('ANOVA:2 czynniki Band*Condition')
f_val, p_val = sstats.f_oneway(PLV_data_nonresponse_BP, PLV_data_response_BP)

print("One-way ANOVA P =", p_val)


sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 10}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="Band", y="Index", hue="Condition",col="Group", data=index_data)
plt.show()



index_data_before = index_data[index_data["Condition"] == 1]
index_data_after = index_data[index_data["Condition"] == 2]

print('ANOVA:2 czynniki EEG_channel*Condition')
f_val, p_val = sstats.f_oneway(PLV_data_before, PLV_data_after)

print("One-way ANOVA P =", p_val)

sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 7}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="EEG_channel", y="Index", hue="Condition", data=index_data)
#plt.grid(True,which="both",ls="--",c='gray')
plt.show()

sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 7}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="EEG_channel", y="Index", hue="Response", data=index_data)
plt.grid(True,which="both",ls="--",c='gray')
plt.show()

###############
index_mean_bands=index_data.groupby('Band')
index_mean_response=index_data.groupby('Response')
index_mean_bands.boxplot(column=['Index'])
index_mean_response.boxplot(column=['Index'])

# Scatter matrices for different columns
#plotting.scatter_matrix(PSD_data[['Response', 'Group', 'Band']])

plt.show()


