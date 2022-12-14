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

## Instruction
Download the files from github, and make sure the entire files are stored in one folder, and run the demo ipynb file. It should run fine without installing additional packages or datasets.

## Detailed Description
### Data Preparation (Part 1)
To prep our data for exploratory analysis, we called clean_df to convert all of our qualitative features to binary values. 

### Data Visualization
![](https://user-images.githubusercontent.com/93099994/206872616-79fa4a6e-cc98-46d1-8ac9-10964ec44a41.png)<br />
The histogram between quantitative health features and stroke cases.<br />
The age and average glucose level show some possible correlation with number of stroke cases.<br /><br />
![](https://user-images.githubusercontent.com/93099994/206872618-fb0a3c32-457e-4ae4-8270-844c60297864.png)<br />
The bar chart of the health features and their correlation coefficients.<br />
The employment status, heart disease, hypertension, age, and high glucose level show high correlation with the stroke cases.

### Data Preparation (Part 2)
After exploratory analysis, we called clean_df_2 and converted quantitative features (age, bmi, and avg_glucose_level) to binary categories for machine learning.

### Comparing Models
Since our data contains binary labels (stroke, no stroke), we have a classification problem. We trained our data with a logistic regression model and decision tree classifier model and computed the cross-validation scores for both. The models performed equally well; both have a cross-validation score of 0.95.

### Logistic Regression
After computing the correlation coefficients and odds ratio for each feature based on the logistic regression model, we concluded glucose level, age, hypertension, and heart disease have a strong positive correlation with getting a stroke, while employment status has a strong negative correlation. We also used odds ratio to measure stroke risk in relation to these features. For example, individuals that get a stroke are about 2 times more likely to have heart disease than to not have heart disease.

## Scope and Limitations
Our current figures only give us an idea of how one particular feature relates to getting a stroke. To add to our data exploration section, we could include a Decision Tree Classifier flowchart to see which groups of people are predisposed to getting a stroke. For example, we can examine how many women with heart disease get a stroke as opposed to only exploring each feature independently. There is also label imbalance in this dataset which could have skewed our model’s performance–most people recorded in the data have no stroke. To address this, we can compute stratified cross-validation scores or stratified train test splits. We computed odds ratio for each feature to determine their relevance to stroke prediction. But the odds ratio is overly  simplistic in describing real world situations. A positive OR may not necessarily mean a statistically significant result. Our next steps could be calculating confidence intervals and p-values. Our objective is ethical as we want to examine features most correlated with stroke to measure stroke risk for new patients. 

## License and Terms of Use
Usage of the dataset is only allowed for educational purpose.

## Acknowledgement
We would like to thank Professor Harlin Lee for all the help and guidance she provided us in creating this project for our PIC 16A class.

## References
https://www.philchodrow.com/PIC16A/project/
https://github.com/inwayi2/Penguin-Project
https://github.com/JiayunMeng/group_project_pic16a
https://www.youtube.com/watch?v=4DnWYK88-E4
https://scikit-learn.org/stable/auto_examples/inspection/plot_linear_model_coefficient_interpretation.html
https://quantifyinghealth.com/interpret-logistic-regression-coefficients/
https://journalfeed.org/article-a-day/2018/idiots-guide-to-odds-ratios/
