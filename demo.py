# create file of classes and functions

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
        
            
# TRANSLATE YOUR SECTION TO A FUNCTION OR FUNCTIONS

# THIS PART IS CLEANING THE DATA
# explain this
def clean_df():
    '''
    Args:
        none
    Returns:
        none
     '''
     pass
    
    
# THIS PART IS FINDING THE COEFFICENTS AND COEFFICIENT GRAPH (FIGURE 1)    
# explain this
def logreg():
    '''
    Args:
        none
    Returns:
        none
    '''
    pass
    

# THIS PART IS CREATING THE HISTOGRAMS (FIGURE 2)
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
def bargraph():
    '''
    Args:
        none
    Returns:
        none
    '''
    pass
  

# MACHINE LEARNING COMPONENT (OPTIONAL)
