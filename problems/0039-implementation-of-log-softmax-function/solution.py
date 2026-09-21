import numpy as np

def log_softmax(scores: list) -> np.ndarray:
	maximum = max(scores)
	result = []
	for i in scores:
		result.append(np.exp(i-maximum))

	pass2 = np.log(np.sum(result))
	return_value = []
	for i in range(len(scores)):
		return_value.append(scores[i]-maximum-pass2)


	return np.array(return_value)