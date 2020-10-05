
import numpy as np

###################
# PART 1 - BASICS :
###################

# column vector:
def column_vector(n):
    array=np.arange(0,n).reshape(n)
    return array

# random matrix:
def random_array(parms):
    array=np.random.random((parms))
    return array

# replace 0's with blue, 1 with red
def color_replace(x):
    new = x.astype('str') 
    new = np.where(new=='1.0', 'red',new)
    new = np.where(new=='0.0', 'blue',new)
    return(new)

# sum the dot-product of Trues, Falses
def true_false_sum(a,b):
    result_dict={}
    result_dict['True']=np.dot(a,b)
    result_dict['False']=np.dot(a,~b)
    return result_dict

# select from two arrays:
def select_from_two_arrays(x, y, b):
    return x*b + y*~b    


# sum_of_squared_differences
def ssd(a,b):
    return ((a-b)**2).sum()


#####################
# PART 2 - ADVANCED :
#####################

def mean_it(x,label):
    """
    Returns the mean of either the row or the column of a 2-dimensional matrix:
    -----
    Args:
        x: a matrix
        label: either Row or Column
    """

    if label=="rows":
        return np.mean(x,axis=1)
    if label=="row":
        return np.mean(x,axis=1)
    if label=="columns":
        return np.mean(x,axis=0)
    if label=="column":
        return np.mean(x,axis=0)


def ones_above_and_below_diagonal(x)
    


