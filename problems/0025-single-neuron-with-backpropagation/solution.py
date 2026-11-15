import numpy as np

def train_neuron(features: np.ndarray, labels: np.ndarray, initial_weights: np.ndarray,
                 initial_bias: float, learning_rate: float, epochs: int) -> (np.ndarray, float, list[float]):

    w = initial_weights
    b = initial_bias
    N = len(labels)

    mse_values = []

    for _ in range(epochs):
        # 1. forward pass sur tout le batch
        z = features @ w + b
        y_hat = 1 / (1 + np.exp(-z))

        # 2. MSE avant la mise à jour
        mse_values.append(np.mean((y_hat - labels) ** 2))

        # 3. delta_k = 2 (ŷ - y) ŷ (1 - ŷ)
        delta = 2 * (y_hat - labels) * y_hat * (1 - y_hat)
        # 4. gradients moyennés sur le batch
        grad_w = features.T @ delta / N
        grad_b = np.mean(delta)

        # 5. une seule mise à jour par epoch
        w = w - learning_rate * grad_w
        b = b - learning_rate * grad_b

    updated_weights = np.round(w, 4)
    updated_bias = round(float(b), 4)
    mse_values = [round(float(m), 4) for m in mse_values]

    return updated_weights, updated_bias, mse_values