import pandas as pd
from statsmodels.stats.multicomp import pairwise_tukeyhsd
from statsmodels.stats.multicomp import MultiComparison
#

filename = 'PLV_degrees_surrogate_2s.xls'
sheetname = 'Sheet1'

path = "data\\Correct\\"

excel_data = pd.read_excel(path+filename, skiprows=0)
labels = pd.read_excel(path+filename, header=0)
labels = tuple(labels)
excel_data = np.matrix(excel_data)


index_data = pd.read_excel(path+filename)


index_data_nonresponse = index_data[index_data["Response"] == 1]
index_data_response = index_data[index_data["Response"] == 2]

index_data_response_MDD = index_data[index_data["Group"] == 1]
index_data_nonresponse_MDD = index_data[index_data["Group"] == 2]

index_data_nonresponse_BP = index_data[index_data["Group"] == 4]
index_data_response_BP = index_data[index_data["Group"] == 3]

def perform_post_hoc_tukey(data, factor1, factor2, factor3, factor2_idx):
    for factor2_idx in range(len(factor2_idx)):
        print(factor2, ': ', factor2_idx+1)
        mc = MultiComparison(data[data[factor2] == factor2_idx+1][factor1], index_data_response_MDD[index_data_response_MDD[factor2] == factor2_idx+1][factor3])
        result = mc.tukeyhsd()

        print(result)
        print(mc.groupsunique)
    
    
print('Group 1 -Response MDD')
print('######################################')    
perform_post_hoc_tukey(index_data_response_MDD, 'Index', 'Band', 'Condition',[1,2,3,4,5]) 
print('Group 2 -Nonesponse MDD')
print('######################################')     
perform_post_hoc_tukey(index_data_nonresponse_MDD, 'Index', 'Band', 'Condition',[1,2,3,4,5])
print('Group 3 -Response BP')
print('######################################')    
perform_post_hoc_tukey(index_data_response_BP, 'Index', 'Band', 'Condition',[1,2,3,4,5])
print('Group 4 -Nonresponse BP')
print('######################################')    
perform_post_hoc_tukey(index_data_nonresponse_BP, 'Index', 'Band', 'Condition',[1,2,3,4,5])
#mc = MultiComparison(index_data_response_MDD[index_data_response_MDD["Band"] == 1]['Index'], index_data_response_MDD[index_data_response_MDD["Band"] == 1]['Condition'])
#result = mc.tukeyhsd()
#
#print(result)
#print(mc.groupsunique)
#
#
#mc = MultiComparison(index_data_response_MDD[index_data_response_MDD["Band"] == 2]['Index'], index_data_response_MDD[index_data_response_MDD["Band"] == 2]['Condition'])
#result = mc.tukeyhsd()
#
#print(result)
#print(mc.groupsunique)
#
#
#mc = MultiComparison(index_data_response_MDD[index_data_response_MDD["Band"] == 3]['Index'], index_data_response_MDD[index_data_response_MDD["Band"] == 3]['Condition'])
#result = mc.tukeyhsd()
#
#print(result)
#print(mc.groupsunique)
#
#
#mc = MultiComparison(index_data_response_MDD[index_data_response_MDD["Band"] == 4]['Index'], index_data_response_MDD[index_data_response_MDD["Band"] == 4]['Condition'])
#result = mc.tukeyhsd()
#
#print(result)
#print(mc.groupsunique)
#
#
#mc = MultiComparison(index_data_response_MDD[index_data_response_MDD["Band"] == 5]['Index'], index_data_response_MDD[index_data_response_MDD["Band"] == 5]['Condition'])
#result = mc.tukeyhsd()
#
#print(result)
#print(mc.groupsunique)
