import pandas as pd
import numpy as np
from scipy.stats import ttest_ind


states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

ut_file = r"C:\_research\coursera_pythonds\university_towns.txt"
gdp_file = r"C:\_research\coursera_pythonds\gdplev.xls"
zillow_file = r"C:\_research\coursera_pythonds\City_Zhvi_AllHomes.csv"

get_recession_start1()
get_recession_end1()
get_recession_bottom1()
convert_housing_data_to_quarters1()


def run_ttest1():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values,
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence.

    Return the tuple (different, p, better)
    where

    different=True if the t-test is True at a p<0.01 (we reject the null hypothesis),
    different=False if otherwise (we cannot reject the null hypothesis).

    The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    data = convert_housing_data_to_quarters1().copy()
    data = data.loc[:,'2008q3':'2009q2']
    data = data.reset_index()
    def price_ratio(row):
        return (row['2008q3'] - row['2009q2'])/row['2008q3']

    data['up&down'] = data.apply(price_ratio,axis=1)
    #uni data

    uni_town = get_list_of_university_towns1()['RegionName']
    uni_town = set(uni_town)

    def is_uni_town(row):
        #check if the town is a university towns or not.
        if row['RegionName'] in uni_town:
            return 1
        else:
            return 0
    data['is_uni'] = data.apply(is_uni_town,axis=1)


    not_uni = data[data['is_uni']==0].loc[:,'up&down'].dropna()
    is_uni  = data[data['is_uni']==1].loc[:,'up&down'].dropna()
    def better():
        if not_uni.mean() < is_uni.mean():
            return 'non-university town'
        else:
            return 'university town'
    p_val = list(ttest_ind(not_uni, is_uni))[1]
    result = (True,p_val,better())
    return result


run_ttest1()

data = convert_housing_data_to_quarters1().copy()
data = data.loc[:,'2008q3':'2009q2']
data = data.reset_index()
def price_ratio(row):
    return (row['2008q3'] - row['2009q2'])/row['2008q3']

data['up&down'] = data.apply(price_ratio,axis=1)
#uni data

uni_town = get_list_of_university_towns1()['RegionName']
uni_town = set(uni_town)

def is_uni_town(row):
    #check if the town is a university towns or not.
    if row['RegionName'] in uni_town:
        return 1
    else:
        return 0
data['is_uni'] = data.apply(is_uni_town,axis=1)


not_uni = data[data['is_uni']==0].loc[:,'up&down'].dropna()
is_uni  = data[data['is_uni']==1].loc[:,'up&down'].dropna()
def better():
    if not_uni.mean() < is_uni.mean():
        return 'non-university town'
    else:
        return 'university town'
ttest_ind(not_uni, is_uni)
p_val = list(ttest_ind(not_uni, is_uni))[1]
result = (True,p_val,better())
return result