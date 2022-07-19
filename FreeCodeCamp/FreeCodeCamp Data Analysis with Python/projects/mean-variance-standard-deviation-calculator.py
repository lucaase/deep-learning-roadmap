# Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix

# The input of the function should be a list containing 9 digits. 
# The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

import numpy as np

def calculate(list):
    answer_dict = {}
    # check if the list contains 9 elements
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")


    # convert the list into a 3 x 3 Numpy array
    array = np.array(list).reshape(3,3)

    # calculate the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix
    answer_dict['mean'] = [np.mean(array,axis=0).tolist(), np.mean(array,axis=1).tolist(), np.mean(array.flatten())]
    answer_dict['variance'] = [np.var(array,axis=0).tolist(), np.var(array,axis=1).tolist(), np.var(array.flatten())]
    answer_dict['standard deviation'] = [np.std(array,axis=0).tolist(), np.std(array,axis=1).tolist(), np.std(array.flatten())]
    answer_dict['max'] = [np.max(array,axis=0).tolist(), np.max(array,axis=1).tolist(), np.max(array.flatten())]
    answer_dict['min'] = [np.min(array,axis=0).tolist(), np.min(array,axis=1).tolist(), np.min(array.flatten())]
    answer_dict['sum'] = [np.sum(array,axis=0).tolist(), np.sum(array,axis=1).tolist(), np.sum(array.flatten())]

    return answer_dict

# test the function
print(calculate([0,1,2,3,4,5,6,7,8]))


test_list = [0,1,2,3,4,5,6,7,8]
test_array = np.array(test_list).reshape(3,3)
print(np.mean(test_array,axis=0))
print(np.var(test_array,axis=0))
print(np.std(test_array,axis=0))
print(np.max(test_array,axis=0))
print(np.min(test_array,axis=0))
print(np.sum(test_array,axis=0))
