# Import the relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch 

# Import the relevant data sets
train = pd.read_csv("train.csv")
train.set_index("id") # Set the ID column as the index
print(train.shape)
test = pd.read_csv("test.csv")
test.set_index("id") # Set the ID column as the index
print(test.shape)
cpc_titles = pd.read_csv("title_info.csv")
print(cpc_titles.shape)

# Preliminary exploration
# print(train.head())
# print(train.tail())
# print(cpc_titles.head())

cpc_copy = cpc_titles.copy() # Create a copy of the cpc_titles file
cpc_titles = cpc_titles.rename(columns={"code": "context"}) # Rename the "code" column to be more in line with our requirements

context = train['context'].unique() # Create a numpy array to store the distinct context identifiers
print(context.shape)

# print(context)

anchor = train['anchor'].unique() # Create a numpy array to store the distinct anchors
print(type(anchor))

target = train['target'].unique() # Create a numpy array to store the distinct targets
#print(target.shape)

train_merged = pd.merge(train, cpc_titles[["context","title"]], on="context", how="left") # Merge the training set and cpc_titles for further analysis
train_merged.set_index("id") # Set the "id" column as the index
#print(train_merged.index)
#print(train_merged.head())
#print(train_merged.shape)
#print(type(train_merged))

anchor_matrix = np.asmatrix(anchor) # Convert the anchor array into a n-D matrix; where n = number of unique anchors 
# print("matrix shape")
# print(anchor_matrix.shape)
# print("matrix")
# print(anchor_matrix)

df = pd.DataFrame(anchor_matrix) # Convert the matrix to dataframe
print("matrix to dataframe shape")
print(df.shape)
print("matrix to dataframe structure")
print(df)
df.columns = df.iloc[0] # This ensures that the rows values are considered for column names; here we only have one row
print("after converting rows to column headers")
df = df.drop([0]) # We drop the row prior to the merge; this will create an empty dataframe
print(df)


train_merged = pd.concat([train_merged,df], axis=1) # Concat the new columns to the training dataset
print(train_merged.shape)
print(train_merged.head())


temp = train_merged.copy() # Make a copy of the training set
temp = temp.drop(columns=["anchor","context","score","title"]) # Remove the irrelevant columns for experimentation
print(temp.head())

from re import search

x = 1.0
y = 0.0

for r in temp[target]:
    for c in temp[anchor]:
        if search(target,anchor):
                1.0
        else:
                0.0 

# from re import search
# import sklearn as sk
# from sklearn.preprocessing import OneHotEncoder
# onehotencoder = OneHotEncoder()

# categorical_cols = temp[anchor]
# transformed_data = onehotencoder.fit_transform(temp[categorical_cols])
# #print(transformed_data.shape)

# encoded_data = pd.DataFrame(transformed_data, index=temp.index)

# concatenated_data = pd.concat([temp, encoded_data], axis=1)
# print(concatenated_data.head)






########################################## EXPERIMENTS #################################################################

## To ensure PyTorch has been installed correctly

# Test case
#torch.cuda.is_available()
#x = torch.rand(5,3)
# print(x)

# print("untransposed anchor")
# print(anchor.shape)

## This will not work as we want the anchors in columns rather than rows plus this is a 1-D vector; 
## taking a transpose of this will simply yield the same vector back.
# anchor_t = anchor.transpose()
# print(type(anchor_t))
# print("transposed anchor")
# print(anchor_t.shape)

#print(list(df))

## The below lines are useless as they'll swap the rows and columns. We don't need it for our project.
# df_t = df.T
# print("after transpose shape")
# print(df_t.shape)
# print("after transpose structure")
# print(df_t)

#df.drop(df.index[0]) ## Unnecessary line of code

#train_merged = pd.concat([train_merged,pd.DataFrame(anchor_matrix)], axis=1) # Add the matrix as new columns to the training dataset

## The trials below are for one hot encoding iteratively
# d = temp.target.apply(pd.Series).unstack()

# for row_val, col_val in enumerate(temp.columns):
#     temp.loc[temp['target']]

# full = temp[target]
# sub = list[]

## 1-hot encoding attempts
# from re import search
# import sklearn as sk
# from sklearn.preprocessing import OneHotEncoder
# onehotencoder = OneHotEncoder()

# categorical_cols = temp[anchor]
# transformed_data = onehotencoder.fit_transform(temp[categorical_cols])
# #print(transformed_data.shape)

# encoded_data = pd.DataFrame(transformed_data, index=temp.index)

# concatenated_data = pd.concat([temp, encoded_data], axis=1)
# print(concatenated_data.head)

