import math

def single_neuron_model(features: list[list[float]], labels: list[int], weights: list[float], bias: float) -> (list[float], float):
	probabilities = []
	for idx, item in enumerate(features):
		score = 0
		for fidx, fitem in enumerate(features[idx]):
			score+=(fitem*weights[fidx])
		final_score = score+bias

		prob = 1 / (1 + math.exp(-final_score))
		probabilities.append(round(prob, 4))
	
	mse = []
	for idx2, item2 in enumerate(probabilities):
		mse.append((item2-labels[idx2])**2)
	
	mse = round(sum(mse)/len(labels),4)

	return probabilities, mse