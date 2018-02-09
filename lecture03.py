#Merging Data Frames
import pandas as pd
import numpy as np

df[df['column name'].map(len) < 2] # apply len function to each member of column ["column name"]

df = pd.DataFrame([{'Name': 'Chris', 'Item Purchased': 'Sponge', 'Cost': 22.50},
                   {'Name': 'Kevyn', 'Item Purchased': 'Kitty Litter', 'Cost': 2.50},
                   {'Name': 'Filip', 'Item Purchased': 'Spoon', 'Cost': 5.00}],
                  index=['Store 1', 'Store 1', 'Store 2'])
df["Date"]=["December 1", "November 1", "Mid-May"]
df["Delivered"]= True
df["Feedback"] = ["Positive", "None", "Negative"]
df
adf = df.reset_index()
adf["Date"]= pd.Series({0: "December1", 2: "Janauary 1"})
# the missing value for .iloc[1] is NaN

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])


student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])

pd.merge(staff_df, student_df, how = "left", left_on = "Name", right_on="Name")

staff_df = staff_df.set_index("Name")
student_df = student_df.set_index("Name")
pd.merge(staff_df, student_df, how = "outer", left_index=True, right_index=True)
# using the right and left indices as join columns
pd.merge(staff_df, student_df, how = "inner", left_index=True, right_index=True)

pd.merge(staff_df, student_df, how = "left", left_index=True, right_index=True)

pd.merge(staff_df, student_df, how = "right", left_index=True, right_index=True)
# when merging data, if conflict columns exists(same column name), will append that column _x for left dataset, and _y for right dataset

invoices = pd.DataFrame([{'Name': 'Kelly', 'ProductId': 111, 'Quantity': 10},
                         {'Name': 'Sally', 'ProductId': 222, 'Quantity': 5},
                         {'Name': 'James', 'ProductId': 111, 'Quantity': 6}])


products = pd.DataFrame([{'ProductId': 111, 'ProductName': 'product1', 'Price': 1.2},
                           {'ProductId': 222, 'ProductName': 'product2', 'Price': 2.3},
                           {'ProductId': 333, 'ProductName': 'product3', 'Price': 0.8}])
products = products.set_index("ProductId")
answer = pd.merge(invoices, products, how="left", left_on = "ProductId", right_index=True)
# here  use a column from left, and a index from right to join

# if multiple columns as join columns
staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])
staff_df
student_df
pd.merge(staff_df, student_df, how='inner', left_on=['First Name','Last Name'], right_on=['First Name','Last Name'])


### Pandas Idioms

#method chaining
#Cahiin INdexing:
df.loc["Washtenaw"]["Total Population"]  # generally bad, pandas could return a copy of a view depending on numpy
# and when you see a ][ you should think carefully about what you are doing
# HOWEVER, method on a object return a reference of that object
df.drop(df[df['Quantity'] == 0].index).rename(columns={'Weight': 'Weight (oz.)'})

#df = pd.read_csv("census.csv")
census_df = pd.read_csv('C:\_research\coursera_pythonds\census.csv')
df = df.copy(census_df)
(df.where(df["SUMLEV"] == 50)
    .dropna()
.set_index(["STNAME", "CTYNAME"])
.rename(columns = {"ESTIMATESBASE2010": 'Year2010"'}) )
#same effect as following:
df = df[df['SUMLEV']==50]
df.set_index(['STNAME','CTYNAME'], inplace=True)
df.rename(columns={'ESTIMATESBASE2010': 'Estimates Base 2010'})
df.head()


#pandas has function applymap for every cell, apply for every row

sub_cols = ["POPESTIMATE2010","POPESTIMATE2011","POPESTIMATE2012","POPESTIMATE2013","POPESTIMATE2014","POPESTIMATE2015" ]
def min_max(row):
    data = row[sub_cols]
    return pd.Series({"min": np.min(data), "max": np.max(data)})

df.apply(min_max, axis = 1)

def min_max_append(row):
    data = row[sub_cols]
    row["max"] = np.max(data)
    row["min"] = np.min(data)
    return row

df.apply(min_max_append, axis = 1)
df.head()

df.apply(lambda x: np.max(x[sub_cols]), axis =1)

# Group by
df = census_df.copy()
df=df[df["SUMLEV"]==50]
from datetime import datetime
call_time_start = datetime.now()
for state in df['STNAME'].unique():
    avg = np.average(census_df.where(df['STNAME']==state).dropna()['CENSUS2010POP'])
call_time_end = datetime.now()
time_delta = call_time_end - call_time_start
str(time_delta.total_seconds())

call_time_start = datetime.now()
for group, frame in df.groupby('STNAME'):
    avg = np.average(frame['CENSUS2010POP'])
call_time_end = datetime.now()
time_delta = call_time_end - call_time_start
str(time_delta.total_seconds())


df = df.set_index("STNAME")
def grp_index_fun(item):
    print(item)
    if item[0] <"M":
        return 0
    if item[0] < "Q":
        return 1
    return 2

### passing a function as a group key will call the function once per index value
### with the return values being used as the group names
call_time_start = datetime.now()
for group, frame in df.groupby(fun):
     print('Total: ' + str(len(frame)) + ' rows in group ' + str(group) + ' for processing.')
call_time_end = datetime.now()
time_delta = call_time_end - call_time_start
str(time_delta.total_seconds())

#call the function on column values.
def grp_col_fun(df, ind, col):
     col_value = df[col].loc[ind]
     return "region: " + str(col_value)
df = df.reset_index()
call_time_start = datetime.now()
df_result = df.groupby(lambda idx: grp_col_fun(df, idx, 'REGION'))[["POPESTIMATE2010", "POPESTIMATE2011"]].sum()
call_time_end = datetime.now()
time_delta = call_time_end - call_time_start
str(time_delta.total_seconds())

df_result.head(5)
### split, then apply
df = census_df.copy()
df1 = df.groupby("STNAME").agg({"CENSUS2010POP": np.average})

def fun(grp, col1, col2):
    return (grp[col1]*grp[col2]).sum()
    #return sum(grp[col1]*grp[col2]))
df.groupby("Category").apply(fun, "Quantity", "Weight (oz.)")

### dataframe groupby , and data series group by
df = census_df.copy()
df=df[df["SUMLEV"]==50]
df1 =df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
for gy, gp in df1:
    print("{} {} {}".format(gp.shape, gy, gp.iloc[0]))

print(type(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']))
print(type(df.groupby(level=0)['POPESTIMATE2010']))

### for series, can do more than 1 aggregation
# if df has index, then can use index level to groupby
(df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average, 'sum': np.sum}))

# if data frame groupby, will create hierarchical column labels
(df.set_index('STNAME').groupby(level=0).agg({"POPESTIMATE2010": [np.average, np.sum], "POPESTIMATE2011": np.sum}))
(df.set_index('STNAME').groupby(level=0).agg({"POPESTIMATE2010": ["sum", "mean"], "POPESTIMATE2011": np.sum}))

# the confusion come in when we change the labels of the dictionary passed to aggregate,
# to correspond to the labels in our group data frame. In this case, pandas recognizes
# that they're the same and maps the functions directly to columns instead of creating
# a hierarchically labeled column.
df.reset_index()
(df.set_index('STNAME').groupby(level=0).agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))

#### Scales
# Ratio scale    units are equally spaced; mathematical operations of +-*/ are all valid; like hight and weight
# Interval scale: units are equally spaced, but there is no true zero, like temperature
# Ordinal scale: the order of the units is important, but not evenly spaced; letter grades such as A+, A
# Nominal scale: categories of data, but the categories have no order with respect to one another; eg: teams of a sport

#change 1st column label to "Grades"
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns = {0: "Grades"}, inplace=True)

df['Grade s'].astype('category').head()
grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                             ordered=True)
grades.head()
# sometimes for a category variable value, use a column True/False will be useful, especially in feature extraction

# Pandas has built-in function called getdummies to convert values of a signle column into multiple columns of 0&1
# that step is reducing a value which is on the interval or ratio scale, like a number grade,
# into one that is categorical like a letter grade. good to view frequency, like hist

#pandas has function: cut, which takes in argument which is some real like structure of a column or a data frame or a series.
# It also takes a number of bins to be used and all bins are kept at equal spacing.
df=census_df.copy()
df = df[df['SUMLEV']==50]
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
pd.cut(df['avg'],3)
pd.cut(df['avg'],3, labes = ["Small", "Medium", "Large"])?