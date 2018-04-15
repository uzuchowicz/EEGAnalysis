#from openpyxl import load_workbook
import pandas as pd
import numpy as np
import scipy.stats as sstats
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker
import scipy
import pylab
filename='PSD_dataV2.xls'
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

PLV_data=pd.read_excel(path+filename)

PSD_mean_bands=PLV_data.groupby('Band')


# The normality criterion: each group compared should come from a population following the normal distribution.
k2, pvalue = sstats.normaltest(PLV_data['Index']) #KS test statistic, either D, D+ or D-.p-value : float One-tailed or two-tailed p-value.
alpha = 1e-3
print("p-value = {:g}", pvalue)

if pvalue < alpha:  # null hypothesis: x comes from a normal distribution
    print("The null hypothesis can be rejected")
else:
    print("The null hypothesis cannot be rejected")

# The variance criterion (or 'homogeneity of variances'): samples should come from populations with the same variance.


plt.hist(PLV_data['Index'])
plt.show()
PLV_data_MDD = PLV_data[PLV_data["Group"] == 1]["Index"]
PLV_data_BP = PLV_data[PLV_data["Group"] == 2]["Index"]

# statistic, pvalue = sstats.levene(PLV_data_MDD, PLV_data_BP)
#
#
# if pvalue < alpha:  # null hypothesis: x comes from a normal distribution
#     print("The null hypothesis can be rejected")
# else:
#     print("The null hypothesis cannot be rejected")


PLV_data_before = PLV_data[PLV_data["Condition"] == 1]["Index"]
PLV_data_after = PLV_data[PLV_data["Condition"] == 2]["Index"]

# for patient_idx in range(19):
#     if patient_idx == 6:
#         continue
#     t, p = sstats.ttest_rel(PLV_data_before[PLV_data_before["Subject"]==int(patient_idx+1)]["Index"], PLV_data_after[PLV_data_after["Subject"] ==int(patient_idx+1)]["Index"])
#

print('ANOVA:2 czynniki Band*Group')
f_val, p_val = sstats.f_oneway(PLV_data_MDD, PLV_data_BP)

print("One-way ANOVA P =", p_val)

sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 7}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="Band", y="Index", hue="Group", data=PLV_data)
plt.grid(True,which="both",ls="--",c='gray')
plt.show()


PLV_data_before = PLV_data[PLV_data["Condition"] == 1]
PLV_data_after = PLV_data[PLV_data["Condition"] == 2]

print('ANOVA:2 czynniki Band*Condition')
f_val, p_val = sstats.f_oneway(PLV_data_before, PLV_data_after)

print("One-way ANOVA P =", p_val)

sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 7}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="Band", y="Index", hue="Condition", data=PLV_data)
plt.grid(True,which="both",ls="--",c='gray')
plt.show()



PLV_data_nonresponse = PLV_data[PLV_data["Response"] == 1]
PLV_data_response = PLV_data[PLV_data["Response"] == 2]

print('ANOVA:2 czynniki Band*Condition')
f_val, p_val = sstats.f_oneway(PLV_data_before, PLV_data_after)

print("One-way ANOVA P =", p_val)

sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 7}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="Band", y="Index", hue="Response", data=PLV_data)
plt.grid(True,which="both",ls="--",c='gray')
plt.show()



PLV_data_before_MDD = PLV_data_MDD[PLV_data["Condition"] == 1]
PLV_data_after_MDD = PLV_data_MDD[PLV_data["Condition"] == 2]

PLV_data_before_BP = PLV_data_BP[PLV_data["Condition"] == 1]
PLV_data_after_BP = PLV_data_BP[PLV_data["Condition"] == 2]

print('ANOVA:2 czynniki Band*Condition*Group')
f_val, p_val = sstats.f_oneway(PLV_data_before_MDD, PLV_data_after_MDD)

print("One-way ANOVA P =", p_val)


print('ANOVA:2 czynniki Band*Condition')
f_val, p_val = sstats.f_oneway(PLV_data_before_BP, PLV_data_after_BP)

print("One-way ANOVA P =", p_val)


sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 7}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="Band", y="Index", hue="Condition",col="Group", data=PLV_data)
plt.show()



PLV_data_nonresponse_MDD = PLV_data_MDD[PLV_data["Response"] == 1]
PLV_data_response_MDD = PLV_data_MDD[PLV_data["Response"] == 2]

PLV_data_nonresponse_BP = PLV_data_BP[PLV_data["Response"] == 1]
PLV_data_response_BP = PLV_data_BP[PLV_data["Response"] == 2]

print('ANOVA:2 czynniki Band*Condition*Group')
f_val, p_val = sstats.f_oneway(PLV_data_nonresponse_MDD, PLV_data_response_MDD)

print("One-way ANOVA P =", p_val)


print('ANOVA:2 czynniki Band*Condition')
f_val, p_val = sstats.f_oneway(PLV_data_nonresponse_BP, PLV_data_response_BP)

print("One-way ANOVA P =", p_val)


sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 7}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="Band", y="Index", hue="Condition",col="Group", data=PLV_data)
plt.show()



PLV_data_before = PLV_data[PLV_data["Condition"] == 1]
PLV_data_after = PLV_data[PLV_data["Condition"] == 2]

print('ANOVA:2 czynniki EEG_channel*Condition')
f_val, p_val = sstats.f_oneway(PLV_data_before, PLV_data_after)

print("One-way ANOVA P =", p_val)

sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 7}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="EEG_channel", y="Index", hue="Condition", data=PLV_data)
plt.grid(True,which="both",ls="--",c='gray')
plt.show()

sns.set(style="whitegrid")
paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 7}
sns.set_context("paper", rc = paper_rc)
g = sns.factorplot(x="EEG_channel", y="Index", hue="Response", data=PLV_data)
plt.grid(True,which="both",ls="--",c='gray')
plt.show()

