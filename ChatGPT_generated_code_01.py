import numpy as np
import matplotlib.pyplot as plt

def ewma(x, y, alpha):
    return (1 - alpha) * x + alpha * y

def simulate_ewma(n, alpha, k, num_simulations):
    arls = []
    for i in range(num_simulations):
        x = np.random.normal(0, 1, n)
        ewma_stat = np.zeros(n)
        ewma_stat[0] = x[0]
        for j in range(1, n):
            ewma_stat[j] = ewma(x[j], ewma_stat[j-1], alpha)
        control_limit = k * np.std(x)
        run_length = 0
        for j in range(n):
            if np.abs(ewma_stat[j]) > control_limit:
                run_length = j + 1
                break
        arls.append(run_length)
    return np.mean(arls)

n = 1000
alpha = 0.1
k = 3
num_simulations = 10000

arl = simulate_ewma(n, alpha, k, num_simulations)
print("Zero-state ARL:", arl)
