import math
import numpy as np

def softmax(scores: list[float]) -> list[float]:

    exp_s = np.exp(scores - np.max(scores))

    return (exp_s / np.sum(exp_s)).tolist()