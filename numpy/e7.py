import numpy as np

votes = np.random.multinomial(n=1000, pvals=[0.4, 0.35, 0.25])
print(f"Votes received by each candidate: {votes}")