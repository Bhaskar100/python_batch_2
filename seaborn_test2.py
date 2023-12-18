import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

valor_ano = pd.DataFrame({'level_1':[1900, 2014, 2015, 2016, 2017, 2018],
                         'total':[0.0, 154.4, 490.9, 628.4,715.2,601.5]})

valor_ano.drop(0, axis=0, inplace=True)

valor_plot = sns.barplot(
    data= valor_ano,
    x= 'level_1',
    y= 'total')

plt.show()