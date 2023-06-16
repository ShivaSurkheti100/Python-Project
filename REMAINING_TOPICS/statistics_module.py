# statistics is a built-in module that you can use to calculate mathematical statistics of numeric data.

''' statistics Methods

Method	Description
statistics.harmonic_mean()	    Calculates the harmonic mean (central location) of the given data
statistics.mean()	            Calculates the mean (average) of the given data
statistics.median()	            Calculates the median (middle value) of the given data
statistics.mode()	            Calculates the mode (central tendency) of the given numeric or nominal data
statistics.variance()	        Calculates the variance from a sample of data
statistics.stdev()	            Calculates the standard deviation from a sample of data

'''

## importing statistics library
import statistics
print(statistics.mean([1, 3, 5, 7, 9, 11, 13]))
print(statistics.median([1, 3, 5, 7, 9, 13]))
print(statistics.mode([1, 3, 3, 3, 5, 6, 7, 7,9, 11, 0, 0]))
print(statistics.harmonic_mean([40, 60, 80]))
print(statistics.stdev([1, 3, 5, 7, 9, 11]))



## list, tuple, dictionary, set are built-in data types in Python which are used to store collections of data

## list is used to store multiple items in a single variable
# tuple is used to store multiple items in a single variable
# set is used to store multiple items in a single variable
# dictionary is used to store data values in key:value pairs
