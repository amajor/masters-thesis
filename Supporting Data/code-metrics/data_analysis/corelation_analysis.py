import csv
import pandas as pd
import numpy as np
import seaborn
import matplotlib.pyplot as plt




MASTER_PREDICTROS_BUGS_FILE = '../data/master_predictors_n_bugs.csv'

if __name__ == '__main__':
    pylint_msg_to_bugs_df = pd.read_csv(MASTER_PREDICTROS_BUGS_FILE, )
    pylint_msg_to_bugs_df.fillna(0)
    # print(pylint_msg_to_bugs_df)

    corr = pylint_msg_to_bugs_df.corr()
    # corr.style.background_gradient(cmap='coolwarm')
    #print(corr.loc[:,'n_bugs'])

    plt.figure(figsize=(10, 20))

    #to extract a dataframe into a dataframe object df[['col_name']]
    seaborn.heatmap(corr[['n_bugs']].query("n_bugs > 0.70"), linewidth=0.1, annot=True)

    #seaborn.heatmap(corr[['n_bugs']].query("n_bugs < 0.3"), linewidth=0.05, annot=True)
    seaborn.pairplot(pylint_msg_to_bugs_df[['n_bugs',  'too-many-branches', 'useless-object-inheritance', 'multiple-imports']])
    print(corr.query('n_bugs >= 0.8').head(10))
    plt.show()



