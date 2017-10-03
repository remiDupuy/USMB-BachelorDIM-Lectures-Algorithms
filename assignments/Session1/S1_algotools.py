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

    if positive_values_counter == 0 :
        return 0
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
    ##
    # basic function able to get bounding box
    # @param input_list : the matrix img to scan

    #initialize variables
    list_ones_row = []
    list_ones_col = []

    for row in xrange(img.shape[0]):
        for col in xrange(img.shape[1]):
            if (img[row, col] == 1):
                list_ones_row.append(row)
                list_ones_col.append(col)

    if(len(list_ones_row) == 0):
        raise ValueError('empty array')

    if(len(list_ones_col) == 0):
        raise ValueError('empty array')

    #return only extremums
    return (min(list_ones_row), max(list_ones_row)), (min(list_ones_col), max(list_ones_col))


def random_fill_sparse(input_array, num_fill):
    ##
    # basic function able to parse a list with random char
    # @param input_list : the input list to be scanned
    # @param num_fill : number of randoms X

    if(num_fill > input_array.shape[0] * input_array.shape[1]):
        raise ValueError()



    for idx in xrange(num_fill):
        isUsed = True
        x_rand = 0
        y_rand = 0
        while(isUsed) :
            x_rand = numpy.random.random_integers(input_array.shape[0]-1)
            y_rand = numpy.random.random_integers(input_array.shape[1]-1)

            if(input_array[x_rand][y_rand] != 'X'):
                isUsed = False

        input_array[x_rand][y_rand] = 'X'


    return input_array

def remove_whitespace(string):
    ##
    # basic function to remove white space in a string
    # @param string : input string
    # @return string

    if string.isspace():
        return ""

    clean_str = ""

    for character in string:
        if not character.isspace():
            clean_str += character

    return clean_str

def shuffle(list):
    ##
    # basic function to shuffle randomly a list
    # @param : input list
    if(len(list) == 0):
        raise ValueError()

    len_list = len(list)
    for idx in reversed(xrange(len_list)):
        j = numpy.random.randint(idx, len_list)
        cur_value = list[j]
        list[j] = list[idx]
        list[idx] = cur_value

    return list


"""
1. Selective sorting
(a) Inital vector 10 15 7 1 3 3 9
    1. Extrama = max = 15 / We exchange 15 with 10 and idx = 1
    15 10 7 1 3 3 9
    
    2. Extrama = max = 10 / We exchange 10 with 10 and idx = 2
    15 10 7 1 3 3 9
    
    3. Extrama = max = 9 / We exchange 9 with 7 and idx = 3
    15 10 9 1 3 3 7
    
    4. Extrama = max = 7 / We exchange 7 with 1 and idx = 4
    15 10 9 7 3 3 1
    
    5. Extrama = max = 3 / We exchange 3 with 3 and idx = 5
    15 10 9 7 3 3 1
    
    6. Extrama = max = 3 / We exchange 3 with 3 and idx = 6
    15 10 9 7 3 3 1
    
    7. Extrama = max = 1 / We exchange 1 with 1 and idx = 7
    15 10 9 7 3 3 1
    
(b) No, it doesn't depend on the content only the length
(c) number of iterations = length of vector = 7
(d) 7
(e) 7*6/2 = 21
(f) The complexity is O(n+1)!
    
"""

def sort_selective(list) :
    ## Function able to sort a list with the selective method
    # @param : input list
    list_len = len(list)
    for idx in xrange(list_len - 1):
        max_idx = idx

        for idx_j in xrange(idx, list_len):
            if(list[max_idx] < list[idx_j]) :
                max_idx = idx_j

        if(max_idx != idx):
            temp = list[idx]
            list[idx] = list[max_idx]
            list[max_idx] = temp

    return list




"""
input_list = [10, 15, 7, 1, 3, 3, 9]
print sort_selective(input_list)
"""

"""
1. Bubble sorting
(a) Inital vector 10 15 7 1 3 3 9
    10 7 15 1 3 3 9
    10 7 1 15 3 3 9
    10 7 1 3 15 3 9
    10 7 1 3 3 15 9
    10 7 1 3 3 9 15
    Loop again on list
    7 10 1 3 3 9 15
    7 1 10 3 3 9 15
    7 1 3 10 3 9 15
    7 1 3 3 10 9 15
    7 1 3 3 9 10 15
    Loop again
    1 7 3 3 9 10 15
    1 3 7 3 9 10 15
    1 3 3 7 9 10 15
    List sorted !!!    

(b) Yes, it does depend on the content only the length
(c) 
(d) 13 permutations are applied
(e) 24 comparasions are applied
(f) The complexity is O(n^2)

"""
def sort_bubble(list) :
    ## Function able to sort a list with the bubble method
    # @param : input list
    for idx in reversed(xrange(1, len(list))):
        for idx_j in xrange(idx):
            if list[idx_j + 1] < list[idx_j] :
                temp = list[idx_j + 1]
                list[idx_j + 1] = list[idx_j]
                list[idx_j] = temp


    return list

"""
input_list = [10, 15, 7, 1, 3, 3, 9]
print sort_bubble(input_list)
"""

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


size_rows = 10
size_cols = 10
mtx = numpy.zeros([size_rows, size_cols], dtype=str)

print(random_fill_sparse(mtx, 4))


"""
string = "test td sf    dsqdsd"
result = remove_whitespace(string)
message = "The message : {string} without spaces equals : {clean_string}".format(string=string, clean_string=result)
print message
"""

"""
input_list = [1,3,4,7]
result = shuffle(input_list)
message = "The input list : [1,3,4,7] , after shuffle : {result}".format(input=input_list, result=result)
print message
"""