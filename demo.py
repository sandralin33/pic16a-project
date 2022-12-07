import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

class DataPreparation:
    '''
    description SANDRA
    '''
    
    def __init__(self, df):
        '''
        Args:
            none
        Returns:
            none
        '''
        self.df = df
        
        
    # SANDRA    
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
        self.df['ever_married'] = le.fit_transform(self.df['ever_married'])
        self.df['gender'] = le.fit_transform(self.df['gender']) # Male = 1, Female = 0
        
        # ADD COMMENT
        # original - rename work_type to employed and split employed to (0 = children and never_worked, 1 = govt_job, private, self-employed)
        # work-related stress
        self.df = self.df.rename(columns = {"work_type" : "is_employed"})
        self.df["is_employed"] = self.df["is_employed"].map({
            "children": 0,
            "Never_worked": 0,
            "Govt_jov": 1,
            "Private": 1,
            "Self-employed": 1
        })
        
        # ADD COMMENT
        self.df = self.df.rename(columns = {"Residence_type" : "is_Rural"})
        self.df["is_Rural"] = self.df["is_Rural"].map({
            "Urban": 0,
            "Rural": 1
        })
        
        # ADD COMMENT
        # original - split smoking_status to has_smoked, remove all "Unknown", change to
        self.df = self.df.rename(columns = {"smoking_status" : "has_smoked"})
        self.df["has_smoked"] = self.df["has_smoked"].map({
            "formerly smoked": 1,
            "smokes": 1,
            "never smoked": 0,
        })
        
        # DROPPING STUFF
        self.df = self.df.drop(['id'], axis = 1) # ADD COMMENT
        self.df = self.df[self.df['gender'] != 'Other'] # drops 'Other' in gender
        self.df = self.df.dropna().reset_index(drop = True) # dropping entries with NaN values
    
    
    # JODIE
    def clean_df_2(self, df):
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
        category = pd.cut(self.df.age,bins=[0,60,99],labels=["Not Senior", "Senior"])
        self.df.insert(2, "is_Old", category)
        self.df["is_Old"] = self.df["is_Old"].map({
            "Not Senior": 0,
            "Senior": 1,
        })
        
        # ADD COMMENT
        category2 = pd.cut(healthcare.bmi,bins=[0,30,100],labels=["Not Overweight", "Overweight"])
        self.df.insert(2, "is_Overweight", category2)
        self.df["is_Overweight"] = self.df["is_Overweight"].map({
            "Not Overweight": 0,
            "Overweight": 1,
        })
        
        # ADD COMMENT
        category3 = pd.cut(healthcare.avg_glucose_level, bins=[0,150,300], labels=["Normal", "High"])
        self.df.insert(2, "has_high_glucose", category3)
        self.df["has_high_glucose"] = self.df["has_high_glucose"].map({
            "Normal": 0,
            "High": 1,
        })
        
        # DROP STUFF
        self.df = self.df.drop(['age'], axis = 1)
        self.df = self.df.drop(['avg_glucose_level'], axis = 1)
        self.df = self.df.drop(['bmi'], axis = 1)
    
    
    # SANDRA
    def train_test_split(self):
        '''
        Args:
            none
        Returns:
            none
        '''
        
        # function to split data into testing and training and compute the scores for both
        y = self.df['stroke'] # stroke outcome
        X = self.df.drop(['stroke'], axis=1) # drop stroke so we don't cheat, X = (features) subset of healthcare
        
        # set aside 25% of samples for testing the model later on 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
        
        return X_train, X_test, y_train, y_test
    
        
# JAEU        
def make_histogram(df, f):
    '''
    Args:
        df: ??
        f: list of features
    Returns:
        none
    '''
    # exception handling SANDRA
    if len(f) != 3:
        raise ValueError("Wrong number of features")
        
    # explain
    stroke_true = df["stroke"] == 1
    stroke_false = df["stroke"] == 0

    # ADD COMMENT
    fig, ax = plt.subplots(1, len(f), figsize = (16, 8))

    # ADD COMMENT
    for i in range(len(f)):
        ax[i].hist(df[stroke_true][f[i]], alpha = 0.6, density = True)
        ax[i].hist(df[stroke_false][f[i]], alpha = 0.6, density = True)
        ax[i].set(xlabel = f[i], ylabel = "case")
        ax[i].legend(("Stroke", "No Stroke"))
        
