# IMPORT EVERYTHING
import pandas as pd
import math
import numpy as np
import urllib
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns


# THIS PART IS CLEANING THE DATA
def clean_df(healthcare):
    '''
    Args:
        none
    Returns:
        none
    '''
    # changing ever_married and gender to binary values
    le = preprocessing.LabelEncoder()
    healthcare['ever_married'] = le.fit_transform(healthcare['ever_married'])
    healthcare['gender'] = le.fit_transform(healthcare['gender']) # Male = 1, Female = 0
    
    # split employed to (0 = children and never_worked, 1 = govt_job, private, self-employed)
    healthcare = healthcare.rename(columns = {"work_type" : "is_employed"})
    healthcare["is_employed"] = healthcare["is_employed"].map({
      "children": 0,
      "Never_worked": 0,
      "Govt_jov": 1,
      "Private": 1,
      "Self-employed": 1
    })
    
    # rename residence_type to is_Rural
    healthcare = healthcare.rename(columns = {"Residence_type" : "is_Rural"})
    healthcare["is_Rural"] = healthcare["is_Rural"].map({
        "Urban": 0,
        "Rural": 1
    })
    
    # rename smoking_status to has_smoked, remove all "Unknown"
    healthcare = healthcare.rename(columns = {"smoking_status" : "has_smoked"})
    healthcare["has_smoked"] = healthcare["has_smoked"].map({
      "formerly smoked": 1,
      "smokes": 1,
      "never smoked": 0,
    })
    
    # drop
    healthcare = healthcare.drop(['id'], axis = 1) # drops id bc not helpful
    healthcare = healthcare.dropna().reset_index(drop = True) # drops NaN values
    healthcare = healthcare[healthcare['gender'] != 'Other'] # drops 'Other' in gender
    
    return healthcare


# THIS PART IS CLEANING THE DATA FOR LOGREG
def clean_df_2(healthcare):
    '''
    Args:
        none
    Returns:
        none
    '''
    # convert age to categorical 
    # (Children-0 to 17,Young Adult-18 to 30, Adult-31 to 45, Old Adult-46-65, Senior-66 to 99)
    # category = pd.cut(healthcare.age,bins=[0,30,45,65,99],labels=['Young People','Middle-Age','Old Adult','Senior'])
    category = pd.cut(healthcare.age,bins=[0,60,99],labels=['Not Senior','Senior'])
    healthcare.insert(2,'Is_Old', category)
    healthcare["Is_Old"] = healthcare["Is_Old"].map({
      'Not Senior': 0,
      'Senior': 1,
    })
    
    category2 = pd.cut(healthcare.bmi,bins=[0,30,100],labels=['Not Overweight','Overweight'])
    healthcare.insert(2,'Is_Overweight', category2)
    healthcare['Is_Overweight'] = healthcare['Is_Overweight'].map({
      'Not Overweight': 0,
      'Overweight': 1,
    })
    
    category3 = pd.cut(healthcare.avg_glucose_level, bins=[0,150,300], labels=['Normal','High'])
    healthcare.insert(2,'Has_High_Glucose', category3)
    healthcare.drop(['avg_glucose_level'], axis = 1)
    healthcare['Has_High_Glucose'] = healthcare['Has_High_Glucose'].map({
      'Normal': 0,
      'High': 1,
    })
    
    healthcare = healthcare.drop(['age'], axis = 1)
    healthcare = healthcare.drop(['avg_glucose_level'], axis = 1)
    healthcare = healthcare.drop(['bmi'], axis = 1)
    
    return healthcare


# CUSTOM CLASS
class healthcare():
    '''
    does stuff to dataset
    '''
    
    def __init__(self):
        '''
        Args:
            none
        Returns:
            none
         '''
         pass
        
        
    # THIS PART IS CREATING THE HISTOGRAMS (FIGURE 1)
    # explain this
    def histogram():
        '''
        Args:
            none
        Returns:
            none
        '''
        features = ["age", "avg_glucose_level", "bmi"]
        fig, ax = plt.subplots(1,len(features), figsize = (16, 8))

        for i in range(len(features)):
            ax[i].hist(healthcare[stroke_true][features[i]], alpha = 0.6, density = True)
            ax[i].hist(healthcare[stroke_false][features[i]], alpha = 0.6, density = True)
            ax[i].set(xlabel = features[i], ylabel = "case")
            ax[i].legend(("Stroke", "No Stroke"))
        
        
    # THIS PART IS CREATING THE BARGRAPHS (FIGURE 3)
    # explain this
    def bargraph(self):
        '''
        Args:
            none
        Returns:
            none
        '''
        fig,axes = plt.subplots(7,2,figsize = (12, 36))

        sns.countplot(ax=axes[0,0], data=healthcare[stroke_true], x='gender')
        sns.countplot(ax=axes[0,1], data=healthcare[stroke_false], x='gender')
        sns.countplot(ax=axes[1,0], data=healthcare[stroke_true], x='hypertension')
        sns.countplot(ax=axes[1,1], data=healthcare[stroke_false], x='hypertension')
        sns.countplot(ax=axes[2,0], data=healthcare[stroke_true], x='heart_disease')
        sns.countplot(ax=axes[2,1], data=healthcare[stroke_false], x='heart_disease')
        sns.countplot(ax=axes[3,0], data=healthcare[stroke_true], x='ever_married')
        sns.countplot(ax=axes[3,1], data=healthcare[stroke_false], x='ever_married')
        sns.countplot(ax=axes[4,0], data=healthcare[stroke_true], x='is_employed')
        sns.countplot(ax=axes[4,1], data=healthcare[stroke_false], x='is_employed')
        sns.countplot(ax=axes[5,0], data=healthcare[stroke_true], x='is_Rural')
        sns.countplot(ax=axes[5,1], data=healthcare[stroke_false], x='is_Rural')
        sns.countplot(ax=axes[6,0], data=healthcare[stroke_true], x='has_smoked')
        sns.countplot(ax=axes[6,1], data=healthcare[stroke_false], x='has_smoked')

        plt.show()
        
        
    # THIS PART IS FINDING THE COEFFICENTS AND COEFFICIENT GRAPH (FIGURE 3)
    # explain this
    def logreg(self, col, coef):
        '''
        Args:
            col: none
            coef: none
        Returns:
            none
        '''
        plt.figure(figsize=(9,7))
        plt.barh(column_names, array_coef[:], 0.3)
        plt.title("regression model")
        plt.axvline(x=0, color='gray')
        plt.xlabel("coefficient values")
        plt.subplots_adjust(left=0.3)

        plt.show()
  

# MACHINE LEARNING COMPONENT (OPTIONAL)
