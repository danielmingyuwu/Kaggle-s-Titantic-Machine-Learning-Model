import pandas as pd 
import numpy as np 


train = pd.read_csv('/Users/danielwu/Documents/Kaggle/Titantic/Titantic_competition/train.csv')
test = pd.read_csv('/Users/danielwu/Documents/Kaggle/Titantic/Titantic_competition/test.csv')
gender_submission = pd.read_csv('/Users/danielwu/Documents/Kaggle/Titantic/Titantic_competition/gender_submission.csv')

#Filter the survived passenger from the train.
survived = train[train['Survived'] == 1]
not_survived = train[train['Survived'] == 0]

#Record Survived and Non-Survived passenger. 
Survived_passenger = len(survived['Survived'])
Not_survived_passenger = len(not_survived['Survived'])


#Total num of Passenger.
total_ppl = Survived_passenger + Not_survived_passenger

#Summary of Survival.
train.Survived.value_counts()

#A good way to check if numbers are correct. 
print(total_ppl == len(train['Survived']))


#Identify the relationship between gender and Survival Rate.
male_survived = survived[survived['Sex']=='male']
male_survived_in_num = len(male_survived['Survived'])
male_survived_in_percentage_vs_gender = male_survived_in_num / 577
male_survived_in_percentage_vs_all = male_survived_in_num/total_ppl

female_survived = survived[survived['Sex']=='female']
female_survived_in_num = len(female_survived['Survived'])
female_survived_in_percentage_vs_gender = female_survived_in_num / 314
female_survived_in_percentage_vs_all = female_survived_in_num/total_ppl

#Summary of gender vs survival (Table). 
train.Sex.value_counts()

#Combine the result as a table.
gender_survival = pd.DataFrame({'male':[int(male_survived_in_num),male_survived_in_percentage_vs_all,male_survived_in_percentage_vs_gender],'female':[int(female_survived_in_num),female_survived_in_percentage_vs_all,female_survived_in_percentage_vs_gender]},index=['Num_Survival','Percentage_Survival','Rate'])



#Identify the relationship between classes and Survival (Table). 
survival_table_C1 = train.loc[(train.Survived == 1)&(train.Pclass == 1)]
survival_table_C2 = train.loc[(train.Survived == 1)&(train.Pclass == 2)]
survival_table_C3 = train.loc[(train.Survived == 1)&(train.Pclass == 3)]

#Summary of Class (Table).
Survival_Class = train.Pclass.value_counts()

#Different classes. 
First_Class_Survival = survived[survived['Pclass']==1]
Second_Class_Survival = survived[survived['Pclass']==2]
Third_Class_Survival = survived[survived['Pclass']==3]

#Survival rate and class relationship. 
First_Class_Survival_rate_vs_class1 = len(First_Class_Survival) / len(train[train['Pclass'] == 1])
Second_Class_Survival_rate_vs_class2 = len(Second_Class_Survival) / len(train[train['Pclass'] == 2])
Third_Class_Survival_rate_vs_class3 = len(Third_Class_Survival) / len(train[train['Pclass'] == 3])

First_Class_Survival_rate_vs_all = len(First_Class_Survival) / len(train.Pclass)
Second_Class_Survival_rate_vs_all = len(Second_Class_Survival) / len(train.Pclass)
Third_Class_Survival_rate_vs_all = len(Third_Class_Survival) / len(train.Pclass)

#Combine the result as as table.
class_survival = pd.DataFrame({'Class1':[int(len(First_Class_Survival)),First_Class_Survival_rate_vs_class1],'Class2':[int(len(Second_Class_Survival)),Second_Class_Survival_rate_vs_class2],'Class3':[int(len(Third_Class_Survival)),Third_Class_Survival_rate_vs_class3]},index=['Num_Survival','Percentage_Survival'])

