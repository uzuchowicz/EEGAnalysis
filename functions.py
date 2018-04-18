import scipy.stats as sstats
import seaborn as sns
import matplotlib.pyplot as plt


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
    sns.factorplot(x=factor1, y="Index", hue=factor2, data=index_data, ci='sd', dodge=True)
    plt.grid(True, which="both", ls="-", c='w', color='w')
    plt.show()

def three_factors_anova(index_data, factor1, factor2, factor3):

    print('ANOVA:2 czynniki', factor1, '*', factor2,'*', factor3)
    print('_________________________________________________')

    for source_group in index_data.groupby(factor1):
        print(factor1, ':{}'.format(source_group[0]))
        for name_group in source_group.groupby(factor2):
            samples = [condition[1] for condition in source_group[1].groupby(factor3)['Index']]
            f_val, p_val = sstats.f_oneway(*samples)
            print(factor1, ': {} | F value : {:.3f} | p value : {:.3f}|'.format(name_group[0], f_val, p_val))

    f_val, p_val = sstats.f_oneway(index_data[index_data[factor2] == 1]["Index"], index_data[index_data[factor2] == 2]["Index"])
    print("All bands one-way ANOVA P =", p_val)
    print("\n")

    sns.set(style="whitegrid")
    paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 15}
    sns.set_style("darkgrid")
    sns.set_context("paper", rc=paper_rc)
    sns.factorplot(x=factor1, y="Index", hue=factor2, col=factor3, data=index_data, ci='sd', dodge=True)
    plt.grid(True, which="both", ls="-", c='w', color='w')
    plt.show()