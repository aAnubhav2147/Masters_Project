import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import torch 

#torch.cuda.is_available()
#x = torch.rand(5,3)
# print(x)

train = pd.read_csv("train.csv")
print(train.shape)
test = pd.read_csv("test.csv")
print(test.shape)
cpc_titles = pd.read_csv("title_info.csv")
print(cpc_titles.shape)

print(train.head())
#print(train.tail())
print(cpc_titles.head())

cpc_copy = cpc_titles.copy()
cpc_titles = cpc_titles.rename(columns = {"code" : "context"})

context = train['context'].unique()
print(context.shape)

target = train['target'].unique()
print(target.shape)

train2 = pd.merge(train, cpc_titles[["context","title"]], on= "context", how = "left")
print(train2.head())

