import numpy as np
import matplotlib.pyplot as plt

demand = np.random.logistic(loc=30, scale=10, size=1000)  # Peak at day 30
plt.hist(demand, bins=30, color='orange', alpha=0.6)
plt.title("Product Demand Over Time")
plt.show()