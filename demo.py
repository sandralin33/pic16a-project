import pandas as pd
import math
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix


# CUSTOM CLASS
class DataPreparation():
    '''
    description
    '''
    
    def __init__(self, csv):
        '''
        Args:
            none
        Returns:
            none
        '''
        # exception handling
        
        # self
        self.csv = csv
    
        
    def clean_df(self):
        '''
        Args:
            none
        Returns:
            none
        ''' 
        
        # ADD COMMENT
        # original - changing ever_married and gender to binary values
        le = preprocessing.LabelEncoder()
        healthcare['ever_married'] = le.fit_transform(healthcare['ever_married'])
        healthcare['gender'] = le.fit_transform(healthcare['gender']) # Male = 1, Female = 0
        
        # ADD COMMENT
        # original - rename work_type to employed and split employed to (0 = children and never_worked, 1 = govt_job, private, self-employed)
        # work-related stress
        healthcare = healthcare.rename(columns = {"work_type" : "is_employed"})
        healthcare["is_employed"] = healthcare["is_employed"].map({
          "children": 0,
          "Never_worked": 0,
          "Govt_jov": 1,
          "Private": 1,
          "Self-employed": 1
        })
        
        # ADD COMMENT
        healthcare = healthcare.rename(columns = {"Residence_type" : "is_Rural"})
        healthcare["is_Rural"] = healthcare["is_Rural"].map({
            "Urban": 0,
            "Rural": 1
        })
        
        # ADD COMMENT
        # original - split smoking_status to has_smoked, remove all "Unknown", change to
        healthcare = healthcare.rename(columns = {"smoking_status" : "has_smoked"})
        healthcare["has_smoked"] = healthcare["has_smoked"].map({
          "formerly smoked": 1,
          "smokes": 1,
          "never smoked": 0,
        })
        
        # DROPPING STUFF
        healthcare = healthcare.drop(['id'], axis = 1) # ADD COMMENT
        healthcare = healthcare[healthcare['gender'] != 'Other'] # drops 'Other' in gender
        healthcare = healthcare.dropna().reset_index(drop = True) # dropping entries with NaN values
        
        return healthcare
    
        
    def clean_df_2(self):
        '''
        Args:
            none
        Returns:
            none
        '''
        
        # ORIGINAL COMMENT
        # additional cleaning for making a more accurate model for logistic regression (non-skewed by quantitative variables)
        # make sure to call clean_df first and pass healthcare from clean_df to
        # this function to further change continuous variables to categorical
        
        # ADD COMMENT
        category = pd.cut(healthcare.age,bins=[0,60,99],labels=['Not Senior','Senior'])
        healthcare.insert(2,'Is_Old', category)
        healthcare["Is_Old"] = healthcare["Is_Old"].map({
        'Not Senior': 0,
        'Senior': 1,
        })
        
        # ADD COMMENT
        category2 = pd.cut(healthcare.bmi,bins=[0,30,100],labels=['Not Overweight','Overweight'])
        healthcare.insert(2,'Is_Overweight', category2)
        healthcare['Is_Overweight'] = healthcare['Is_Overweight'].map({
        'Not Overweight': 0,
        'Overweight': 1,
        })
        
        # ADD COMMENT
        category3 = pd.cut(healthcare.avg_glucose_level, bins=[0,150,300], labels=['Normal','High'])
        healthcare.insert(2,'Has_High_Glucose', category3)
        healthcare.drop(['avg_glucose_level'], axis = 1)
        healthcare['Has_High_Glucose'] = healthcare['Has_High_Glucose'].map({
        'Normal': 0,
        'High': 1,
        })
        
        # DROP STUFF
        healthcare = healthcare.drop(['age'], axis = 1)
        healthcare = healthcare.drop(['avg_glucose_level'], axis = 1)
        healthcare = healthcare.drop(['bmi'], axis = 1)
        
        return healthcare
    
    
    # RENAME THIS FUNCTION
    def clean_df_3(self):
        '''
        Args:
            none
        Returns:
            none
        '''
        # FEEL FREE TO RENAME AND/OR FIX IT BC IDK WHAT THIS DOES
        
        # function to split data into testing and training and compute the scores for both
        y = healthcare['stroke'] # stroke outcome
        X = healthcare.drop(['stroke'], axis=1) # drop stroke so we don't cheat, X = (features) subset of healthcare
        
        # set aside 25% of samples for testing the model later on 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
   

# FUNCTION OUTSIDE OF CLASS  
def make_histogram(f):
        '''
        Args:
            f: list of features
        Returns:
            none
        '''
        # exception handling
        
        
        # ADD COMMENT
        fig, ax = plt.subplots(1, len(f), figsize = (16, 8))
        
        # ADD COMMENT
        for i in range(len(f)):
            ax[i].hist(healthcare[stroke_true][f[i]], alpha = 0.6, density = True)
            ax[i].hist(healthcare[stroke_false][f[i]], alpha = 0.6, density = True)
            ax[i].set(xlabel = f[i], ylabel = "case")
            ax[i].legend(("Stroke", "No Stroke"))
            
