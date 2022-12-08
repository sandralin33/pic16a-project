import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt

class DataPreparation:
    '''
    Takes in a dataframe. Cleans it for data visualization and logistic regression. # something about train_test_split
    '''
    def __init__(self, df):
        '''
        initialize with a dataframe
        Args:
            df: a dataframe
        Returns:
            none
        '''
        self.df = df # save df as self.df
           
    def clean_df(self):
        '''
        cleans the data by changing qualitative features to binary values, drops 'id' and NaN values
        '''
        # change ever_married and gender to binary values
        le = preprocessing.LabelEncoder()
        self.df['ever_married'] = le.fit_transform(self.df['ever_married']) # married = 1, unmarried = 0
        self.df = self.df[self.df['gender'] != 'Other'] # drops 'Other' in gender
        self.df['gender'] = le.fit_transform(self.df['gender']) # male = 1, female = 0
        
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
        
        self.df = self.df.drop(['id'], axis = 1) # drop 'id'
        self.df = self.df.dropna().reset_index(drop = True) # drop entries with NaN values
    
    # JODIE
    def clean_df_2(self, df):
        ''' Change quantitative variables to binary categories for machine learning
        Args:
            df: dataframe cleaned from calling clean_df first
        Returns:
            none
        '''
        
        # Create a new column Is_Old and sort ages into "Not Senior" and "Senior" for age ranges (0,60] and (60,99] respectively
        # convert "Not Senior" and "Senior" categories to 0 and 1
        category = pd.cut(self.df.age,bins=[0,60,99],labels=["Not Senior", "Senior"])
        self.df.insert(2, "is_Old", category)
        self.df["is_Old"] = self.df["is_Old"].map({
            "Not Senior": 0,
            "Senior": 1,
        })
        
        # Create a new column is_Overweight and sort bmi into "Not Overweight" and "Overweight" for ranges (0,30] and (30,100]
        # convert "Not Overweight" and "Overweight" categories to 0 and 1
        category2 = pd.cut(healthcare.bmi,bins=[0,30,100],labels=["Not Overweight", "Overweight"])
        self.df.insert(2, "is_Overweight", category2)
        self.df["is_Overweight"] = self.df["is_Overweight"].map({
            "Not Overweight": 0,
            "Overweight": 1,
        })
        
        # Create a new column has_high_glucose and sort avg_glucose_level into "Normal" and "High" for ranges (0,150] and (150,300]
        # convert "Normal" and "High" categories to 0 and 1
        category3 = pd.cut(healthcare.avg_glucose_level, bins=[0,150,300], labels=["Normal", "High"])
        self.df.insert(2, "has_high_glucose", category3)
        self.df["has_high_glucose"] = self.df["has_high_glucose"].map({
            "Normal": 0,
            "High": 1,
        })
        
        # Drop original columns that have continuous values
        self.df = self.df.drop(['age'], axis = 1)
        self.df = self.df.drop(['avg_glucose_level'], axis = 1)
        self.df = self.df.drop(['bmi'], axis = 1)
        
    # SANDRA
    def train_test_split(self):
        '''
        description
        Args:
            none
        Returns:
            X: 
            y: 
            X_train: 
            X_test: 
            y_train: 
            y_test: 
        '''
        # splits data into testing and training and compute the scores for both
        y = self.df['stroke'] # stroke outcome
        X = self.df.drop(['stroke'], axis=1) # drop stroke so we don't cheat, X = (features) subset of healthcare
        
        # set aside 25% of samples for testing the model later on 
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
        
        return X, y, X_train, X_test, y_train, y_test
    
         
# JAEU        
def make_histogram(df, f):
    '''
    Description: Prints histograms of number of stroke cases, based on input features
    Args:
        df: the data that will be represented in histograms. In this project, it would be the csv file with stroke cases vs features.
        f: the list of quantitative features that are represented in x axis of the histograms
    Returns:
        none
    '''
    # exception handling SANDRA
    if len(f) != 3:
        raise ValueError("Wrong number of features")
    
    # exception handling of when the input x values aren't quantitative
    QuantitativeData = False
    for i in range(len(df)):
        for j in range(len(f)):
            if df.loc[i][f[j]] > 2:
                QuantitativeData = True
    if QuantitativeData == False:
        raise TypeError("This function only accepts quantitative x values. The" + ', '.join(f) + "is qualitative")
        
    # separating rows with stroke cases and non-stroke cases
    stroke_true = df["stroke"] == 1
    stroke_false = df["stroke"] == 0

    # preparing for histograms
    fig, ax = plt.subplots(1, len(f), figsize = (16, 8))

    # looping through features in the list f, creates histograms of number of stroke cases and non-stroke cases of features.
    # The stroke and non-stroke cases histograms are stacked and normalized with total density = 1 for easier comparison
    for i in range(len(f)):
        ax[i].hist(df[stroke_true][f[i]], alpha = 0.6, density = True)
        ax[i].hist(df[stroke_false][f[i]], alpha = 0.6, density = True)
        ax[i].set(xlabel = f[i], ylabel = "case")
        ax[i].legend(("Stroke", "No Stroke"))
        
