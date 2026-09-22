import numpy as np

def make_diagonal(x):
	array = []
	x = list(x)

	for idx, item in enumerate(x):
		trial = ([0]*len(x))
		trial[idx] = item
		array.append(trial)

	return array