import pandas as pd 
import numpy as np 


train = pd.read_csv('/Users/danielwu/Documents/Kaggle/Titantic/Titantic_competition/train.csv')
test = pd.read_csv('/Users/danielwu/Documents/Kaggle/Titantic/Titantic_competition/test.csv')
gender_submission = pd.read_csv('/Users/danielwu/Documents/Kaggle/Titantic/Titantic_competition/gender_submission.csv')

train.head() #shows the first 5 rows from train.csv 
test.head() #shows the first 5 rows from test.csv

#Descriptive statistics of object data types for train:
train.shape
train.describe(include=['0'])

#Descriptive statistics of object data types for test:
test.shape
test.describe(include=['0'])

#All info of both databases 
train.info()
test.info()

#Check duplicate 
train.isnull()
test.isnull()
train.isnull().sum()
test.isnull().sum()