##
# @author : Remi Dupuy, LP DIM
# @brief : A set of generic functions for data management

# imports
import numpy
import time


def average_above_zero(input_list):
    # init criticals variables
    positive_values_sum = 0
    positive_values_counter = 0

    # compute the average of positive elements of a list
    for item in input_list:
        if (item > 0):
            positive_values_sum += item
            positive_values_counter += 1
    average = float(positive_values_sum) / float(positive_values_counter)
    print('Positive elements average is ' + str(average))
    return float(average)


def max_value(input_list):
    ##
    # basic function able to return the max value of a list
    # @param input_list : the ipnut list to be scanned
    # @throws an exception (ValueError) on an empty list

    # first check of provided list is empty
    if len(input_list) == 0:
        raise ValueError('provided list is empty')

    max_value = input_list[0]
    max_index = 0

    # compute the average of positive elements of a list
    for index, item in enumerate(input_list):
        if (item > max_value):
            max_value = item
            max_index = index

    print('Max index {index} and max value {value}').format(index=max_index, value=max_value)
    return float(max_value)


def reverse_table(input_list):
    ##
    # basic function able to reverse a list
    # @param input_list : the input list to be scanned
    # @throws an exception (ValueError) on an empty list

    # first check of provided list is empty
    if len(input_list) == 0:
        raise ValueError('provided list is empty')

    for idx in xrange(len(input_list) / 2):
        temp = input_list[idx]
        input_list[idx] = input_list[len(input_list) - idx - 1]
        input_list[len(input_list) - idx - 1] = temp

    return input_list


def roi_bbox(img):
    #initialize variables
    list_ones_row = []
    list_ones_col = []

    for row in xrange(img.shape[0]):
        for col in xrange(img.shape[1]):
            if (img[row, col] == 1):
                list_ones_row.append(row)
                list_ones_col.append(col)

    #return only extremums
    return (min(list_ones_row), max(list_ones_row)), (min(list_ones_col), max(list_ones_col))


"""
#the input list
input_list = [1,2,3,4,-7]
# Call the function
result = average_above_zero(input_list)
message = 'The average of positives samples of {input_list} is {result}'.format(input_list=input_list, result = result)
print(message)
"""

"""
#the input list
input_list = [1,2,3,4,7]
# Call the function
result = max_value(input_list)
message = 'The max value of {input_list} is {result}'.format(input_list=input_list, result = result)
print(message)
"""

"""
#the input list
input_list = [1,3,4,7]
# Call the function
result = reverse_table(input_list)
message = 'The reverse table of {input} is {result}'.format(input=input_list, result=result)
print(message)
"""

"""
# the input list
init_time = time.time()
# Call the function
size_rows = 10
size_cols = 10
mtx = numpy.zeros([size_rows, size_cols])
mtx[4:7, 7:9] = numpy.ones([3, 2])
mtx[2:4, 5:8] = numpy.ones([2, 3])

result = roi_bbox(mtx)
"""