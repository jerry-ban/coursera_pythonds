__author__ = 'jerry.ban'

df.rename(columns = {oldColName: newColName}, inplace = True )

###Query Data Frame

# boolean masking is the heart of query dataframe
# boolean mask is an array (1 or 2 dimension) where each of the values in the array are True/False
# the array overlaid on top of the data that we are querying and the data cell aligned with True value
# will be admitted into our final result.


df["Gold"]> 0  # boolean array returned, and indexed
only_gold = df.where(df["Gold"] > 0)
only_gold["Gold"].count()
df["Gold"].count()

only_gold = only_gold.dropna()

only_gold = df[df["Gold"] > 0]

## pay attention to the ()
len( df[ (df["Gold"] > 0) | (df["Gold.1"] > 0) ])
len( df[ (df["Gold"] > 0) & (df["Gold.1"] > 0) ])

df["Name"][df["Cost"]>3.0]
df[df["Cost"]>3.0]["Name"]


### Indexing data frame

#set index will lose the old index, so need to keep the old index info if necessary
df["country"] = df.index
df = df.set_index("Gold")
df = df.reset_index() # the index column will be the 1st data column, and add a numbered index column without name
# if original df has only numbered index column, then reset_index will create a 1st data column named as "index", and recreate a numbered index column
df["Country"].unique()
df = df.set_index(["State", "County"])
# in combined(multi column) index, each column is called a Level, and outermost column is  level 0
df.loc["Michigan", "Washtenaw County"]
df.loc[ [("Michigan", "Washtenaw County"),("Michigan", "Wayne County") ] ]

# add extra column to existing index
df = df.set_index([df.index, "Name"])
df.index.names = ["Location", "Name"]


# add a new row to a multi-indexed data frame
new_series = pd.Series(data={"Cost": 3.0, "Item Purchased": "Kitty FOod"}, name=("Store 2", "Kevyn") )
df.append(new_series)

### missing values
df = pd.read_csv("log.txt")
df.fillna?

df = df.set_index('time')
df = df.sort_index()

df.fillna( method = None)
# method



import pandas as pd
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], index=['Store 1', 'Store 1', 'Store 2'])
df.head()