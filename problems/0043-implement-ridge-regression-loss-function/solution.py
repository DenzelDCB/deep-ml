import numpy as np

def ridge_loss(X: np.ndarray, w: np.ndarray, y_true: np.ndarray, alpha: float) -> float:
    X = list(X)
    w = list(w)
    y_true = list(y_true)
    predictions = []
    mse = []
    for idx, item in enumerate(X):
        row_prediction = 0
        for feature_idx in range(len(item)):
            feature = item[feature_idx]
            weight = w[feature_idx]

            row_prediction += feature * weight

        predictions.append(row_prediction)
        mse.append((predictions[idx] - y_true[idx]) ** 2)

    avg = sum(mse) / len(X)
    weight_squared_sum = 0
    
    for weight in w:
        weight_squared_sum += weight * weight
        
    penalty = weight_squared_sum * alpha

    return avg+penalty


