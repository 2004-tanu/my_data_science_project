import numpy as np
import matplotlib.pyplot as plt

data = np.array([1, 2, 3, 4, 5])

print("Mean:", np.mean(data))
print("Median:", np.median(data))

plt.plot(data)
plt.title("Data Visualization")
plt.show()
