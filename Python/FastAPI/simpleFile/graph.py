import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(42)
random_numbers = np.random.random(size=4)

s = pd.Series(random_numbers)
fig, ax = plt.subplots()
s.plot.bar()
fig.savefig('my_plot.png')

