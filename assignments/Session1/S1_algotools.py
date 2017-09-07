##
# @author : Remi Dupuy, LP DIM
# @brief : A set of generic functions for data management

def average_above_zero(input_list):

    #init criticals variables
    positive_values_sum=0
    positive_values_counter=0

    #compute the average of positive elements of a list
    for item in input_list:
        if(item > 0):
            positive_values_sum += item
            positive_values_counter += 1
    average = float(positive_values_sum)/float(positive_values_counter)
    print('Positive elements average is '+str(average))
    return float(average)

def max_value(input_list):
    ##
    # basic function able to return the max value of a list
    # @param input_list : the ipnut list to be scanned
    # @throws an exception (ValueError) on an empty list

    #first check of provided list is empty
    if len(input_list) == 0 :
        raise ValueError('provided list is empty')

    max_value=input_list[0]
    max_index = 0

    #compute the average of positive elements of a list
    for index, item in enumerate(input_list):
        if(item > max_value):
            max_value = item
            max_index = index

    print('Max index {index} and max value {value}').format(index = max_index, value = max_value)
    return float(max_value)



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