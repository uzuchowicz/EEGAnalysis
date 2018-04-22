import scipy.stats as sstats
import seaborn as sns
import matplotlib.pyplot as plt
# from statsmodels.stats.multicomp import pairwise_tukeyhsd
# from statsmodels.stats.multicomp import MultiComparison
#
# mc = MultiComparison(data['Score'], data['Archer'])
# result = mc.tukeyhsd()

# print(result)
# print(mc.groupsunique)


def two_factors_anova(index_data, factor1, factor2):

    print('ANOVA:2 czynniki', factor1, '*', factor2)
    print('_________________________________________________')

    for name_group in index_data.groupby(factor1):
        samples = [condition[1] for condition in name_group[1].groupby(factor2)['Index']]
        f_val, p_val = sstats.f_oneway(*samples)
        print(factor1, ': {} | F value : {:.3f} | p value : {:.3f}|'.format(name_group[0], f_val, p_val))

    f_val, p_val = sstats.f_oneway(index_data[index_data[factor2] == 1]["Index"], index_data[index_data[factor2] == 2]["Index"])
    print("All bands one-way ANOVA P =", p_val)
    print("\n")

    sns.set(style="whitegrid")
    paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 15}
    sns.set_style("darkgrid")
    sns.set_context("paper", rc=paper_rc)
    g = sns.factorplot(x=factor1, y="Index", hue=factor2, data=index_data, ci=95, capsize=.3, dodge=True, title='Degree of PLV for MDD and BP gorup in EEG bands')
    #sns.plt.set_title('Density of PLV for MDD and BP gorup in EEG bands')
    plt.grid(True, which="both", ls="-", c='w', color='w')
    plt.title('Degree of PLV for MDD and BP gorup in EEG bands', fontsize=8)
    plt.show()

def three_factors_anova(index_data, factor1, factor2, factor3):

    print('ANOVA:2 czynniki', factor1, '*', factor2,'*', factor3)
    print('_________________________________________________')

    for name_group in index_data.groupby(factor2):

        print(factor2, ':{}'.format(name_group[0]))
        group_index_data = index_data[index_data[factor2] == name_group[0]]
        #print('source_group0',source_group[0])

        for source_group in group_index_data.groupby(factor1):
            samples = [condition[1] for condition in source_group[1].groupby(factor3)['Index']]
            f_val, p_val = sstats.f_oneway(*samples)
            print(factor1, ': {} | F value : {:.3f} | p value : {:.3f}|'.format(source_group[0], f_val, p_val))

    f_val, p_val = sstats.f_oneway(index_data[index_data[factor2] == 1]["Index"], index_data[index_data[factor2] == 2]["Index"])
    print("All bands one-way ANOVA P =", p_val)
    print("\n")

    sns.set(style="whitegrid")
    paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 15}
    sns.set_style("darkgrid")
    sns.set_context("paper", rc=paper_rc)
    sns.factorplot(x=factor1, y="Index", hue=factor3, col=factor2, data=index_data, ci=95,capsize=.3, dodge=True)
   # plt.grid(True, which="both", ls="-", c='w', color='w')
    plt.show()