import numpy as np

n_data = len(versicolor_petal_length)
n_bins = np.sqrt(n_data)
n_bins = int(n_bins)

_ = plt.hist(versicolor_petal_length, bins=n_bins)
_ = plt.xlabel('petal length (cm)')
_ = plt.ylabel('count')

plt.show()
