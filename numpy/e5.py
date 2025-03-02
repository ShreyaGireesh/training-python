import numpy as np
import matplotlib.pyplot as plt

areas = np.random.uniform(low=1, high=10, size=1000)  # Areas 1 to 10
plt.hist(areas, bins=10, color='purple', alpha=0.6)
plt.title("Random Delivery Area Assignment")
plt.show()