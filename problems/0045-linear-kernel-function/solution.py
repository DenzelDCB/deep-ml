import numpy as np

def kernel_function(x1, x2):

	result = 0
	for i in range(len(x1)):
		result+=x1[i]*x2[i]

	return result
