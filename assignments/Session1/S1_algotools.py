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


"""
#the input list
input_list = [1,2,3,4,-7]
# Call the function
result = average_above_zero(input_list)
message = 'The average of positive smaples of {input_list} is {result} and {youpi}'.format(input_list=input_list, result = result)
print(message)
"""