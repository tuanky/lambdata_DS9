"""UTility functions for working with data"""
import pandas as pd 
import numpy as np 
import sklearn
from sklearn.model_selection import train_test_split
from scipy.stats import chi2
from scipy.stats import chi2_contingency


def split_data(df):
    '''
    The dataframe(df) is split into 20% test and 80% train. 
    The train data set is then further split into 25% validation
    and 75% train dataset. 
    '''

    train, test = train_test_split(df, test_size=0.20, random_state=42)

    train, val = train_test_split(train, test_size=0.25, random_state=42)

    return train, test, val

def conf(col1, col2):
    '''
    takes two categorical features and return chi-squared contingency table
    '''

    col1 = col1
    col2 = col2
    df_col1, df_col2 = df[col1], df[col2]
    cats1, cats2 = categories(df_col1), categories(df_col2)

    def aux(is_cat1):
        return [sum(is_cat1 & (df_col2 == cat2))
                for cat2 in cats2]

    result = [aux(df_col1 == cat1)
              for cat1 in cats1]

    return scs.chi2_contingency(result)


