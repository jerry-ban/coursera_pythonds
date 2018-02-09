#pandas
#text books
#Python for Data Analysis  , by West McKimney, O'Reilly
#Learning the Pandas Library, by Matt Harrison

#planetpython.org
#stackoverflow.com
#http://dataskeptic.com/

import pandas as pd
#pd.Series?
animals = ['Tiger', 'Bear', 'Goose']
pd.Series(animals)

birds = ['swan', 'hawk', None]
pd.Series(birds)
#None here converted to None

numbers = [11,22,None]
pd.Series(numbers)
#None here converted to NaN( float)
# NaN is similar to None, bu numeric value

np.nan == None  # False
np.nan == np.nan  # False

np.isnan(np.nan) # True

#indexing will ignore those no-matching keys
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports, index=['Golf', 'Sumo', 'Hockey'])
s

#Query Series
sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}
s = pd.Series(sports)
s
#iloc and loc are attributes
s.iloc[3]
s[3]
s.loc["Golf"]
s["Golf"]

# if initialized with integer indexing,
sports = {99: 'Bhutan',
          100: 'Scotland',
          101: 'Japan',
          102: 'South Korea'}
s = pd.Series(sports)
s[99]  # good

s = pd.Series([66,55,44,33])
s.iloc[0]

#working with data
#utilizing numpy's vectorization feature
import numpy as np
total = np.sum(s)
total

s=pd.Series(np.random.randint(0,1000,10000))
s.head()
len(s)

import timeit
def test_time1():
    summary =   0
    for item in s:
        summary+=item
timeit.timeit("test_time1", number = 100000, setup="from __main__ import test_time1")

def test_time2():
    np.sum(s)

timeit.timeit("test_time2", number = 100000, setup="from __main__ import test_time2")

###Related feature in Pandas and NumPy is called broadcasting. With broadcasting, you can apply an operation to every value in the series, changing the series.

s+=2
#compared with:
for label, value in s.iteritems():
    s.set_value(label, value+2)

original_sports = pd.Series({'Archery': 'Bhutan',
                             'Golf': 'Scotland',
                             'Sumo': 'Japan',
                             'Taekwondo': 'South Korea'})
cricket_loving_countries = pd.Series(['Australia',
                                      'Barbados',
                                      'Pakistan',
                                      'England'],
                                   index=['Cricket',
                                          'Cricket',
                                          'Cricket',
                                          'Cricket'])
# the following is like qurey, return new dataset
all_countries = original_sports.append(cricket_loving_countries)
original_sports  # no change to the origianl series
all_countries

###Data Frame
#if .loc is not existing, it will create ones
df.iloc[2] # the 3rd data row
df["animals"] # the animals column
df.iloc[1]["animals"]
df.loc["Store 1","animals"]
#.loc(), .iloc() are index
# Axis 0 is the rows, Axis 1 is columns

purchase_1 = pd.Series({'Name': 'Chris', 'Item Purchased': 'Dog Food', 'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',  'Item Purchased': 'Bird Seed',  'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.T
# chain operations tend to create a copy of data, instead of a view of data
df["Store 2"]["Cost"] = pd.Series([7,7])  #try to assign value to a copy,
df.loc["Store 2","Cost"] = 6 # update the df value

#.loc support slicing
df.loc[:,["Name","Cost"]]

# delete data
df.drop("Store 1") # create a copy which dropped the "store 1"
df.drop("Store 1", inplace=True ) # this modify the original dataset
# axes = 0 means to drop row, =1 means to drop column
del df["Name"] # delete column from original data

# new col:
df["Location"]= None

# Dataframe Indexing and Loading
costs = df['Cost']
costs += 2
#df is updated by above action
df = pd.read_csv("olympics.csv")
df.head()
df = pd.read_csv("olympics.csv", index_col =0, skiprows = 1)
df.columns # columns names