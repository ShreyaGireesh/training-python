import numpy as np
import matplotlib.pyplot as plt

goals = np.random.binomial(n=10, p=0.3, size=1000)  # 10 shots, 30% chance
plt.hist(goals, bins=10, color='g', alpha=0.6)
plt.title("Football Goals Distribution")
plt.show()