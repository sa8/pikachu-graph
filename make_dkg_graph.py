import pickle
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as st

files = ["Signing","DKG"]
def plot_diff_in_means(data: pd.DataFrame, col1: str, col2: str, f: str):
    """
    given data, plots difference in means with confidence intervals across groups
    col1: categorical data with groups
    col2: continuous data for the means
    """
    n = data.groupby(col1)[col2].count()
    # n contains a pd.Series with sample size for each category

    cat = list(data.groupby(col1, as_index=False)[col2].count()[col1])
    # cat has names of the categories, like 'category 1', 'category 2'

    mean = data.groupby(col1)[col2].agg('mean')
    # the average value of col2 across the categories

    std = data.groupby(col1)[col2].agg(np.std)
    se = std / np.sqrt(n)
    # standard deviation and standard error

    lower = st.t.interval(alpha = 0.95, df=n-1, loc = mean, scale = se)[0]
    upper = st.t.interval(alpha = 0.95, df =n-1, loc = mean, scale = se)[1]
    # calculates the upper and lower bounds using scipy

    for upper, mean, lower, y in zip(upper, mean, lower, cat):
        #plt.plot((lower, mean, upper), (y, y, y), 'b.-')
        plt.plot( (y, y, y), (lower, mean, upper),'b.-')
        # for 'b.-': 'b' means 'blue', '.' means dot, '-' means solid line
    plt.xlabel("Number of participants",fontsize=20)
    plt.ylabel("Seconds",fontsize=20)
    plt.xticks(np.arange(3, 23, 2.0))
    #plt.yticks(
        # range(len(n)), 
        # list(data.groupby(col1, as_index = False)[col2].count()[col1])
        # )
    #plt.show()
    plt.xticks(fontsize= 15)
    plt.yticks(fontsize= 15)
    plt.tight_layout()
    plt.savefig(f+'.pdf')
    plt.close()


for file in files:
   Data = pickle.load( open( "/Users/sazouvi/PL_Work/CLB2/make-graph/pickles/"+file+".p", "rb" ) )
   cat = []
   rating = []
   print(cat,rating)
   for key, value in Data.items():
      if len(value)>0:
         cat += [key] * len(value)
         rating += value


   dat_dict = dict()
   dat_dict['cat'] = cat
   dat_dict['rating'] = rating
   test_dat = pd.DataFrame(dat_dict)
   plot_diff_in_means(data = test_dat, col1 = 'cat', col2 = 'rating',f = file)

