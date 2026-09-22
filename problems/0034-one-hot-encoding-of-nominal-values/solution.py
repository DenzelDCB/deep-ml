import numpy as np

def to_categorical(x, n_col=None):
	columns = max(x)+1
	result = []
	for idx, item in enumerate(x):
		column = [0]*columns
		column[item] = 1
		result.append(column)

	return result