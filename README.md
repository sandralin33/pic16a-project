# Stroke Prediction

## Collaborators
Sandra Lin, Jaeu Choi, Jodie Chen

## Short Description
The goal of this project is to determine which features of an individual’s health data are highly predictive of whether the individual would get a stroke or not.

## Dataset
The dataset we used was “[Stroke Prediction Dataset”](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset?page=2) from kaggle.com. The dataset was created by [fedesoriano](https://www.kaggle.com/fedesoriano) from kaggle.com, and the source of the data is confidential. The dataset allows its use only for educational purposes.

## Python Packages
pandas 1.4.2<br />
numpy 1.21.5<br />
math<br />
seaborn 0.11.2<br />
pyplot from matplotlib 3.5.1<br />
train_test_split, cross_val_score, tree, preprocessing, LogisticRegression, classification_report, confusion_matrix from sklearn 1.0.2

## Detailed Description
include instructions on how to run it, output with 2 figures, explanations or interpretations of the result

### Data Preparation (Part 1)
explain

### Data Visualization
figures

### Data Preparation (Part 2)
explain

### Comparing Models
results

### Logistic Regression
results

## Scope and Limitations
Our current figures only give us an idea of how one particular feature relates to getting a stroke. To add to our data exploration section, we could include a Decision Tree Classifier flowchart to see which groups of people are predisposed to getting a stroke. For example, we can examine how many women with heart disease get a stroke as opposed to only exploring each feature independently. There is also label imbalance in this dataset which could have skewed our model’s performance–most people recorded in the data have no stroke. To address this, we can compute stratified cross-validation scores or stratified train test splits. We computed odds ratio for each feature to determine their relevance to stroke prediction. But the odds ratio is overly  simplistic in describing real world situations. A positive OR may not necessarily mean a statistically significant result. Our next steps could be calculating confidence intervals and p-values. Our objective is ethical as we want to examine features most correlated with stroke to measure stroke risk for new patients. 


## Acknowledgement
We would like to thank Professor Harlin Lee for all the help and guidance she provided us in creating this project for our PIC 16A class.

## References
penguins project

## Demo Video
link
