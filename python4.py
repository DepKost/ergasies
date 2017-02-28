import sys
import numpy as np
import random as rd

random_input = rd.sample(range(0, 10), 10)
print random_input


maxindx = np.argmax(random_input)
#print max_indx

new = np.delete(random_input, maxindx)
minindx = np.argmin(new)
new = np.delete(new, minindx)
print new

new = np.delete(random_input, maxindx)
minindx = np.argmin(new)
new = np.delete(new, minindx)
print new

def function_std(array):
maxval = max(random_input)
    #print max_val
maxindx = np.argmax(random_input)
    #print max_indx
minval = min(random_input)
new = np.delete(random_input, maxindx)
minindx = np.argmin(new)
new = np.delete(new, minindx)
result = np.std(new)
    #print result
return result
	
random_input = rd.sample(range(0, 10), 10)
print random_input

function_std(random_input)
