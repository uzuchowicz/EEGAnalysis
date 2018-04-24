import seaborn as sns
import matplotlib.pyplot as plt
import copy
def two_way_plot(data):

    data_graph = copy.deepcopy(data)
    data_graph['Condition'] = ['AFTER' if i == 1 else 'BEFORE' for i in data_graph['Condition'] == 2]
    data_graph['Session'] = ['1th' if row['Session'] ==1 else ( '10th' if row['Session'] == 2 else '20th') for idx, row in data_graph.iterrows()]

    data_graph['Band'] = ['delta' if row['Band'] == 1 else ('theta' if row['Band'] == 2 else ('alpha' if row['Band'] == 3 else ('delta' if row['Band'] == 4 else 'gamma'))) for idx, row
                             in data_graph.iterrows()]
    # ['delta' if i == 1 else 'theta' for i in data_graph['Session'] ==2]
    # for index, row in data_graph.iterrows():
    #     if row['Session'] == 1:
    #         print(row['Session'])
    #         row['Session'] = '1th'
    #     else:
    #         row['Session'] ='10th'

    #     elif idx == 2:
    #         idx = 'theta'
    #     elif idx == 3:
    #         idx ='alpha'
    #     elif idx == 4:
    #         idx = 'beta'
    #     else:
    #         idx = 'gamma'

    # for i in data_graph['Session']:
    #     if i == 1:
    #         data_graph['Session'] = '1th'
    #     elif i == 2:
    #         data_graph['Session'] = '10th'
    #     else:
    #         data_graph['Session'] = '20th'



    sns.set(style="whitegrid")
    paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 15}
    sns.set_style("darkgrid")
    sns.set_context("paper", rc=paper_rc)
    g=sns.factorplot(x='Band', y="Index", hue='Session', data=data_graph, ci=95,capsize=.3, dodge=True)
    g.set_titles(row_template=["MDD-response","MDD-nonresponse","BP-response","BP-nonresponse"])
    g.fig.suptitle("Degree of PLV for BP-response group before and after sessions")
    plt.grid(True, which="both", ls="-", c='w', color='w')
    plt.show()

# def three_way_plot(data)
    # sns.set(style="whitegrid")
    # paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 15}
    # sns.set_style("darkgrid")
    # sns.set_context("paper", rc=paper_rc)
    # index_data_response_MDD['Condition'] = ['BEFORE' if i == 1 else 'AFTER' for i in index_data_response_MDD['Condition'] == 2]
    # g = sns.factorplot(x='Band', y="Index", hue='Condition', data=index_data_response_MDD, ci=95,capsize=.3, dodge=True)
    # plt.grid(True, which="both", ls="-", c='w', color='w')
    # plt.title('Degree of PLV for MDD-response in all bands before and after sessions', fontsize=8)
    # g.set_titles(row_template=["MDD-response","MDD-nonresponse","BP-response","BP-nonresponse"])
    # g.fig.suptitle("this is a title")
    #    # plt.grid(True, which="both", ls="-", c='w', color='w')
    # plt.show()
    #
    # sns.set(style="whitegrid")
    # paper_rc = {'lines.linewidth': 0.5, 'lines.markersize': 15}
    # sns.set_style("darkgrid")
    # sns.set_context("paper", rc=paper_rc)
    # g = sns.factorplot(x='Band', y="Index", hue='Condition', col='Session', data=index_data_response_MDD, ci=95,capsize=.3, dodge=True)
    # plt.grid(True, which="both", ls="-", c='w', color='w')
    # plt.title('Degree of PLV for MDD-response in all bands before and after sessions', fontsize=8)
    # g.set_titles(row_template=["MDD-response","MDD-nonresponse","BP-response","BP-nonresponse"])
    # g.fig.suptitle("this is a title")
    #    # plt.grid(True, which="both", ls="-", c='w', color='w')
    # plt.show()