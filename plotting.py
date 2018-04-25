import seaborn as sns
import matplotlib.pyplot as plt
import copy
def two_way_plot(data, factor1, factor2):

    data_graph = copy.deepcopy(data)
    data_graph['Condition'] = ['BEFORE' if i == 1 else 'AFTER' for i in data_graph['Condition'] == 2]
    data_graph['Session'] = ['1th' if row['Session'] ==1 else ( '10th' if row['Session'] == 2 else '20th') for idx, row in data_graph.iterrows()]
    data_graph['Group'] = ['MDD-response' if row['Group'] == 1 else ('MDD-nonresponse' if row['Group'] == 2 else ('BP-response' if row['Group'] == 3 else 'BP-nonresponse')) for idx, row
                             in data_graph.iterrows()]
    data_graph['Band'] = ['delta' if row['Band'] == 1 else ('theta' if row['Band'] == 2 else ('alpha' if row['Band'] == 3 else ('beta' if row['Band'] == 4 else 'gamma'))) for idx, row
                             in data_graph.iterrows()]

    sns.set(style="whitegrid")
    paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 15}
    sns.set_style("darkgrid")
    sns.set_context("paper", rc=paper_rc)
    g=sns.factorplot(x=factor1, y="Index", hue=factor2, data=data_graph, ci=95,capsize=.3, dodge=True)
    g.set_titles(row_template=["MDD-response","MDD-nonresponse","BP-response","BP-nonresponse"])
    g.fig.suptitle("Degree of PLV for BP-response group before and after sessions")
    plt.grid(True, which="both", ls="-", c='w', color='w')
    plt.show()


def three_way_plot(data, factor1, factor2, factor3):

    data_graph = copy.deepcopy(data)
    data_graph['Condition'] = ['AFTER' if i == 1 else 'BEFORE' for i in data_graph['Condition'] == 2]
    data_graph['Session'] = ['1th' if row['Session'] ==1 else ( '10th' if row['Session'] == 2 else '20th') for idx, row in data_graph.iterrows()]
    data_graph['Group'] = ['MDD-response' if row['Group'] == 1 else (
    'MDD-nonresponse' if row['Group'] == 2 else ('BP-response' if row['Group'] == 3 else 'BP-nonresponse')) for idx, row
                           in data_graph.iterrows()]

    data_graph['Band'] = ['delta' if row['Band'] == 1 else ('theta' if row['Band'] == 2 else ('alpha' if row['Band'] == 3 else ('beta' if row['Band'] == 4 else 'gamma'))) for idx, row
                             in data_graph.iterrows()]

    sns.set(style="whitegrid")
    paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 15}
    sns.set_style("darkgrid")
    sns.set_context("paper", rc=paper_rc)
    g=sns.factorplot(x=factor1, y='Index', hue=factor2, col=factor3, data=data_graph, ci=95,capsize=.3, dodge=True)
    g.set_titles(row_template=["MDD-response","MDD-nonresponse","BP-response","BP-nonresponse"])
    g.fig.suptitle("Degree of PLV for BP-response group before and after sessions")
    #plt.grid(True, which="both", ls="-", c='w', color='w')
    plt.show()