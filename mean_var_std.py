import numpy as np

def calculate(numbers):
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")
    
    arr = np.array(numbers).reshape(3, 3)
    
    mean_axis1 = arr.mean(axis=1).tolist() 
    mean_axis2 = arr.mean(axis=0).tolist()  
    mean_flat = arr.mean().tolist()       

    variance_axis1 = arr.var(axis=1).tolist() 
    variance_axis2 = arr.var(axis=0).tolist() 
    variance_flat = arr.var().tolist()        

    stddev_axis1 = arr.std(axis=1).tolist()  
    stddev_axis2 = arr.std(axis=0).tolist() 
    stddev_flat = arr.std().tolist()         

    max_axis1 = arr.max(axis=1).tolist() 
    max_axis2 = arr.max(axis=0).tolist()  
    max_flat = arr.max().tolist()         

    min_axis1 = arr.min(axis=1).tolist()  
    min_axis2 = arr.min(axis=0).tolist() 
    min_flat = arr.min().tolist()      

    sum_axis1 = arr.sum(axis=1).tolist()  # Sum along rows
    sum_axis2 = arr.sum(axis=0).tolist()  # Sum along columns
    sum_flat = arr.sum().tolist()         # Sum of all elements

    # Return the results as a dictionary with float precision
    return {
        'mean': [mean_axis1, mean_axis2, mean_flat],
        'variance': [variance_axis1, variance_axis2, variance_flat],
        'standard deviation': [stddev_axis1, stddev_axis2, stddev_flat],
        'max': [max_axis1, max_axis2, max_flat],
        'min': [min_axis1, min_axis2, min_flat],
        'sum': [sum_axis1, sum_axis2, sum_flat]
    }
