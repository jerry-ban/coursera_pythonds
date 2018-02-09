#Merging Data Frames
import pandas as pd

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
